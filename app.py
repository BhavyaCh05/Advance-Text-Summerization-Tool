import streamlit as st
from transformers import pipeline

st.title("Text Analysis Tool")

@st.cache_resource
def load_classification_model():
    return pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis")

@st.cache_resource
def load_ner_model():
    return pipeline("ner", grouped_entities=True)

classification_model = load_classification_model()
sentiment_model = load_sentiment_model()
ner_model = load_ner_model()

st.header("Text Classification")
classification_input = st.text_area("Enter text for classification:", height=100)
if classification_input:
    classification_result = classification_model(classification_input)
    st.write("Classification Result:")
    st.json(classification_result)

st.header("Sentiment Analysis")
sentiment_input = st.text_area("Enter text for sentiment analysis:", height=100)
if sentiment_input:
    sentiment_result = sentiment_model(sentiment_input)
    st.write("Sentiment Analysis Result:")
    st.json(sentiment_result)

st.header("Named Entity Recognition (NER)")
ner_input = st.text_area("Enter text for NER:", height=100)
if ner_input:
    ner_result = ner_model(ner_input)
    st.write("NER Result:")
    st.json(ner_result)

