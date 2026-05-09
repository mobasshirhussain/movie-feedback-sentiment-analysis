import streamlit as st
import pandas as pd
import pickle
import re
import nltk
import PyPDF2
import os
import requests
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

# ---------------- DOWNLOAD MODEL ----------------
import gdown

clf_url = "https://drive.google.com/uc?id=111bVS1WgQGdpDWTIXoIC1lJjclY2bfMl"
tfidf_url = "https://drive.google.com/uc?id=1BpBp4uf8MTGdOdpZPZGXQgIUNUCXnVdD"

if not os.path.exists("clf.pkl"):
    gdown.download(clf_url, "clf.pkl", quiet=False)

if not os.path.exists("tfidf.pkl"):
    gdown.download(tfidf_url, "tfidf.pkl", quiet=False)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MovieMood AI",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: #f1f5f9;
    font-family: 'Segoe UI', sans-serif;
}
.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 900;
    color: #f8fafc;
}
.sub-title {
    text-align: center;
    color: #cbd5f5;
    margin-bottom: 25px;
}
.stTextArea textarea {
    background: #020617 !important;
    color: #f1f5f9 !important;
    border-radius: 14px !important;
    border: 2px solid #334155 !important;
    padding: 14px !important;
}
[data-testid="stFileUploader"] {
    background: #020617;
    border: 1px solid #334155;
    border-radius: 14px;
    padding: 10px;
}
.stButton button {
    border-radius: 12px !important;
    height: 50px !important;
    font-weight: 700;
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: white;
    border: none;
}
.stButton button:hover {
    transform: scale(1.03);
    transition: 0.2s;
}
.result-positive {
    background: linear-gradient(135deg, #10b981, #059669);
    padding: 14px;
    border-radius: 12px;
    margin-top: 10px;
}
.result-negative {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    padding: 14px;
    border-radius: 12px;
    margin-top: 10px;
}
[data-testid="metric-container"] {
    background: #020617;
    border: 1px solid #334155;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}
.footer {
    text-align: center;
    margin-top: 40px;
    color: #94a3b8;
}
@media (max-width: 768px) {
    .main-title { font-size: 1.8rem !important; }
    .sub-title { font-size: 0.9rem !important; }
    .stTextArea textarea { height: 140px !important; }
    .stButton button { height: 45px !important; font-size: 0.9rem !important; }
    [data-testid="metric-container"] { margin-bottom: 10px; }
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_engine():
    try:
        stopwords.words('english')
    except:
        nltk.download('stopwords')

    clf = pickle.load(open('clf.pkl', 'rb'))
    tfidf = pickle.load(open('tfidf.pkl', 'rb'))

    stop_words = set(stopwords.words('english'))
    negation_words = {'not', 'no', 'don', "don't", 'never', 'neither', 'nor'}
    final_stop_words = stop_words - negation_words

    return final_stop_words, PorterStemmer(), clf, tfidf

stop_words, stemmer, clf, tfidf = load_engine()

# ---------------- TEXT PROCESS ----------------
def process(text):
    text = re.sub(r'<[^>]*>', '', text)
    emojis = re.findall(r'(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub(r'[\W]+', ' ', text.lower()) + ' ' + ' '.join(emojis).replace('-', '')
    tokens = text.split()

    clean = [
        stemmer.stem(word)
        for word in tokens
        if word not in stop_words
    ]

    return " ".join(clean)

# ---------------- SESSION ----------------
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

def reset_callback():
    st.session_state["my_input"] = ""

# ---------------- HEADER ----------------
st.markdown('<div class="main-title">🎬 MovieMood AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">AI Powered Movie Review Sentiment Analyzer</div>', unsafe_allow_html=True)

# ---------------- INPUT ----------------
user_input = st.text_area("", height=180, placeholder="Enter movie reviews (one per line)...", key="my_input")

# ---------------- FILE ----------------
st.markdown("### 📂 Upload File")
uploaded_file = st.file_uploader("Upload CSV, TXT or PDF", type=["csv", "txt", "pdf"])

if uploaded_file:
    st.success("File uploaded successfully!")

# ---------------- BUTTONS ----------------
col1, col2 = st.columns(2, gap="small")

with col1:
    analyze = st.button("🔍 Analyze Sentiment", use_container_width=True)

with col2:
    st.button("🔄 Reset", use_container_width=True, on_click=reset_callback)

# ---------------- ANALYSIS ----------------
if analyze:

    if user_input.strip():
        reviews = [r.strip() for r in user_input.split('\n') if r.strip()]
        clean_reviews = [process(r) for r in reviews]

        vectors = tfidf.transform(clean_reviews)
        preds = clf.predict(vectors)

        st.markdown("## 📊 Results")

        for i, (review, pred) in enumerate(zip(reviews, preds), 1):
            if pred == 1:
                st.markdown(f'<div class="result-positive">😊 Positive {i}<br>{review}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="result-negative">😡 Negative {i}<br>{review}</div>', unsafe_allow_html=True)

    elif uploaded_file:
        file_type = uploaded_file.name.split('.')[-1].lower()

        if file_type == "csv":
            df = pd.read_csv(uploaded_file)
            df.columns = [c.lower() for c in df.columns]

        elif file_type == "txt":
            text = uploaded_file.read().decode("utf-8")
            reviews = [r.strip() for r in text.splitlines() if r.strip()]
            df = pd.DataFrame({"review": reviews})

        elif file_type == "pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                try:
                    text += page.extract_text() or ""
                except:
                    continue
            reviews = [r.strip() for r in text.splitlines() if r.strip()]
            df = pd.DataFrame({"review": reviews})

        if 'review' not in df.columns:
            st.error("File must contain 'review' column")
        else:
            df = df[df['review'].astype(str).str.strip() != ""]
            st.dataframe(df.head())

            clean = df['review'].astype(str).apply(process)
            vectors = tfidf.transform(clean)
            preds = clf.predict(vectors)

            df['Sentiment'] = pd.Series(preds).map({1: "Positive", 0: "Negative"})

            st.markdown("## 📊 Analytics")

            col1, col2 = st.columns(2, gap="large")

            with col1:
                st.markdown("### 🟢 Positive")
                st.metric("", f"{(df['Sentiment']=='Positive').mean()*100:.2f}%")

            with col2:
                st.markdown("### 🔴 Negative")
                st.metric("", f"{(df['Sentiment']=='Negative').mean()*100:.2f}%")

            st.dataframe(df)

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button("📥 Download Results", csv, file_name="sentiment_results.csv", mime="text/csv")

    else:
        st.warning("Please enter text or upload a file")

# ---------------- FOOTER ----------------
st.markdown('<div class="footer">Made by Mobasshir Hussain</div>', unsafe_allow_html=True)
