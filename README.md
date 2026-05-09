# 🎬 Movie Feedback Sentiment Analysis

An AI-powered **Movie Review Sentiment Analysis Web Application** developed using **Natural Language Processing (NLP)** and **Machine Learning** techniques.  
The system classifies movie reviews as **Positive 😊** or **Negative 😡** using a trained **Random Forest Classifier** with **TF-IDF Vectorization**.

---

# 🚀 Features

✅ Sentiment prediction using Machine Learning  
✅ NLP-based text preprocessing pipeline  
✅ Multiple input formats supported:

- ✍️ Manual text input
- 📄 TXT file upload
- 📊 CSV file upload
- 📕 PDF file upload

✅ Real-time sentiment analytics dashboard  
✅ Download prediction results as CSV  
✅ Interactive and responsive UI using Streamlit  

---

# 📊 Dataset Information

This project uses the **IMDB Movie Reviews Dataset** from Kaggle.

## 📁 Dataset Details

- Dataset Name: IMDB Dataset of 50K Movie Reviews
- Total Reviews: 50,000
- Categories:
  - Positive
  - Negative

## 📌 Dataset Purpose

The dataset contains real-world movie reviews labeled according to sentiment polarity and is commonly used for NLP and sentiment classification tasks.

---

# 🧹 NLP Preprocessing Pipeline

The following preprocessing techniques are applied before model training:

- HTML tag removal
- Lowercase text conversion
- Special character removal
- Tokenization
- Stopword removal
- Negation handling (`not`, `never`, `no`)
- Stemming using Porter Stemmer

---

# 🧠 Machine Learning Model

## 🔹 Algorithm Used
- Random Forest Classifier

## 🔹 Feature Extraction
- TF-IDF Vectorization

## ✅ Why Random Forest?

- Handles high-dimensional text data efficiently
- Reduces overfitting
- Provides strong classification performance
- Works well with sparse TF-IDF vectors

---

# ⚙️ Workflow

```text
User Input → NLP Preprocessing → TF-IDF Vectorization →
Random Forest Prediction → Sentiment Result & Analytics
```

---

# ☁️ Model File Handling

Due to GitHub file size limitations, the trained model files (`clf.pkl` and `tfidf.pkl`) were not uploaded directly to the repository.

Instead, the model files were stored on **Google Drive** and integrated inside `app.py`.  
The application automatically accesses and loads these files during execution, allowing the Streamlit app to run successfully without exceeding GitHub storage limits.

---

# 📂 Project Structure

```text
Movie-Feedback-Sentiment-Analysis/
│── app.py
│── requirements.txt
│── README.md
│── SentimentAnalysisWithNLTK.ipynb
│── .gitignore
```

---

# 🛠️ Tech Stack

## 💻 Frontend & Backend
- Streamlit

## 🐍 Programming Language
- Python

## 📚 Libraries Used
- pandas
- nltk
- scikit-learn
- PyPDF2
- pickle
- streamlit

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/movie-feedback-sentiment-analysis.git
cd movie-feedback-sentiment-analysis
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

# 📥 Input Formats

## ✅ Manual Text Input
Enter one or multiple movie reviews manually.

## ✅ CSV File Upload
CSV file must contain a column named:

```text
review
```

## ✅ TXT File Upload
Plain text reviews supported.

## ✅ PDF File Upload
PDF reviews are automatically extracted and analyzed.

---

# 📈 Output

The application provides:

- Sentiment Prediction
  - Positive 😊
  - Negative 😡

- Real-Time Analytics
  - Positive Percentage
  - Negative Percentage

- Downloadable CSV Results

---

# 🎯 Applications

- Movie review analysis
- Product feedback analysis
- Customer opinion mining
- Social media sentiment tracking
- NLP learning projects

---

# 🔥 Future Enhancements

- Add Neutral sentiment classification
- Deep Learning integration (LSTM / BERT)
- Multi-language sentiment analysis
- Cloud deployment support
- User authentication system

---

# 👨‍💻 Author

## Mobasshir Hussain

AI & Machine Learning Enthusiast

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📜 License

This project is licensed under the MIT License.
