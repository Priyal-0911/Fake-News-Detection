#Fake News Detection

This repository contains a Streamlit application for detecting fake news using a PassiveAggressiveClassifier model. The application allows users to input news articles and predicts whether they are real or fake.

##Project Overview
This project demonstrates a simple machine learning application for fake news detection. It uses a machine learning algorithm to classify news articles as real or fake based on their text content. The model is trained on a dataset of news articles, where each article is labeled as either real or fake. The training process involves learning patterns and features from the text of these articles that help distinguish between real and fake news.

##Installation
To run this project, you will need Python 3.x and the following Python libraries:

numpy
pandas
scikit-learn
joblib
streamlit
You can install these dependencies using pip:

```bash
pip install numpy pandas scikit-learn joblib streamlit
```

##Usage
Clone the repository:
```bash
git clone https://github.com/yourusername/fake-news-detection.git
cd fake-news-detection
```

Run the Streamlit application:
```bash
streamlit run main.py
```
Open your web browser and go to http://localhost:8501 to view the application.

##Features
Input News Article: Users can input a news article text into the application.
Real/Fake Prediction: The model predicts whether the input news article is real or fake based on its text content.
Interactive Interface: Streamlit provides an interactive web interface for easy input and prediction.

##File Structure
The project directory is structured as follows:

```bash
fake-news-detection/
│
├── main.py            # Streamlit application script
├── model.pkl          # Pre-trained model file (PassiveAggressiveClassifier)
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

##Model Training

The model.pkl file contains a pre-trained PassiveAggressiveClassifier model. This model has been trained on a labeled dataset of news articles. You can find more details about the dataset and training process in the main.py script.

##Contributions
Contributions are welcome! If you want to contribute to this project, feel free to fork the repository and submit a pull request with your improvements. 
