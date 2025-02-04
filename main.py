import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

# Load the model and vectorizer
model_path = "model.pkl"
vectorizer_path = "vectors.pkl"

loaded_pac = joblib.load(model_path)
loaded_tfidf = joblib.load(vectorizer_path)

# Streamlit UI
st.title("Fake News Detection")
st.write("Enter a news article to predict if it's real or fake.")

# Text area for input
user_input = st.text_area("News Article", height=200)

if st.button("Predict"):
    if user_input:
        # Transform the input using the loaded TfidfVectorizer
        example_tfidf = loaded_tfidf.transform([user_input])
        
        # Predict using the loaded model
        example_pred = loaded_pac.predict(example_tfidf)
        
        # Display the prediction
        prediction = "Real" if example_pred[0] else "Fake"
        st.write(f'Prediction: {prediction}')
    else:
        st.write("Please enter a news article to predict.")
