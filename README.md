# 🎬 Movie Feedback Sentiment Analysis

An **AI-powered Sentiment Analysis Web Application** built using **Natural Language Processing (NLP)** and a **Random Forest Classifier** to analyze and classify movie reviews as **Positive 😊 or Negative 😡**.

---

## 🚀 Features

* 🎯 Sentiment prediction using **Random Forest**
* 🧠 NLP-based text preprocessing
* 📂 Multiple input support:

  * Text input
  * CSV file
  * TXT file
  * PDF file
* 📊 Real-time analytics (Positive vs Negative %)
* 📥 Download results as CSV
* 💻 Clean and responsive UI using Streamlit

---

## 📊 Dataset

This project uses the **IMDB Movie Reviews Dataset** from Kaggle.

* 📁 Dataset: IMDB Dataset of 50K Movie Reviews
* 📦 Size: ~50,000 reviews
* 🏷️ Labels:

  * Positive
  * Negative

### 📌 Description

The dataset contains real-world movie reviews labeled by sentiment polarity. It is widely used for NLP and sentiment analysis tasks.

---

## 🧹 Data Preprocessing

* Removal of HTML tags
* Lowercasing text
* Removing special characters
* Tokenization
* Stopword removal
* Negation handling (*not, never, no*)
* Stemming using Porter Stemmer

---

## 🧠 Model Details

* 🤖 Algorithm: **Random Forest Classifier**
* 🔢 Feature Extraction: **TF-IDF Vectorization**

### ✅ Why Random Forest?

* Handles large text features efficiently
* Reduces overfitting
* Provides good accuracy on classification tasks

---

## ⚙️ How It Works

1. User enters text or uploads file
2. Text is preprocessed using NLP techniques
3. Converted into numerical vectors using TF-IDF
4. Random Forest model predicts sentiment
5. Results displayed with analytics dashboard

---

## 📂 Project Structure

```
Movie-Feedback-Sentiment-Analysis/
│── app.py
│── clf.pkl
│── tfidf.pkl
│── requirements.txt
│── README.md
│── IMDB Dataset.csv
│── SentimentAnalysisWithNLTK.ipynb
```

---

## 🛠️ Tech Stack

* **Frontend & Backend:** Streamlit
* **Language:** Python
* **Libraries:**

  * pandas
  * nltk
  * scikit-learn
  * PyPDF2
  * pickle

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/movie-feedback-sentiment-analysis.git
cd movie-feedback-sentiment-analysis
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Application

```bash
streamlit run app.py
```

---

## 📊 Input Format

### ✅ Text Input

Enter multiple reviews (one per line)

### ✅ CSV File

Must contain column:

```
review
```

---

## 📈 Output

* Sentiment classification (Positive / Negative)
* Percentage analytics
* Downloadable CSV results

---

## 🎯 Use Cases

* Movie review analysis
* Product feedback analysis
* Social media sentiment tracking
* NLP learning projects

---

## 🔥 Future Improvements

* Add Neutral sentiment
* Use Deep Learning (LSTM / BERT)
* Multi-language support
* Cloud deployment

---

## 👨‍💻 Author

**Mobasshir Hussain**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
