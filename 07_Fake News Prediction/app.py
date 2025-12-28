import streamlit as st
import joblib
import re
import string

# Load model & vectorizer
model = joblib.load("model/lr_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Simple text cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]|https?://\S+|www\.\S+|<.*?>', ' ', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    return text.strip()

# Prediction
def predict(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    return "Fake News" if model.predict(vec)[0] == 0 else "True News"

# Streamlit UI
st.title("📰 Fake News Detector")
news = st.text_area("Enter news here:")

if st.button("Predict"):
    if news:
        st.write(predict(news))
    else:
        st.warning("Please enter some news text!")
