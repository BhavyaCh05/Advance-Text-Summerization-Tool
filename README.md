# Advance-Text-Summerization-Tool

# Text Analysis Tool

This project is a web-based text analysis tool built using Streamlit and Hugging Face Transformers. The tool provides three main functionalities: text classification, sentiment analysis, and named entity recognition (NER).

## Features

- **Text Classification:** Classifies text into predefined categories.
- **Sentiment Analysis:** Analyzes the sentiment of the input text.
- **Named Entity Recognition (NER):** Identifies and categorizes entities (e.g., names, organizations) in the input text.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/text-analysis-tool.git
   cd text-analysis-tool
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the Streamlit application, run the following command:

```bash
streamlit run app.py
```

This will start a local server and provide a URL where you can access the application in your web browser.

## Code Overview

The main script (`app.py`) contains the following sections:

1. **Importing Libraries:**
   ```python
   import streamlit as st
   from transformers import pipeline
   ```

2. **Loading Models:**
   The models for text classification, sentiment analysis, and NER are loaded using Streamlit's `@st.cache_resource` decorator to ensure they are cached and not reloaded unnecessarily.
   ```python
   @st.cache_resource
   def load_classification_model():
       return pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

   @st.cache_resource
   def load_sentiment_model():
       return pipeline("sentiment-analysis")

   @st.cache_resource
   def load_ner_model():
       return pipeline("ner", grouped_entities=True)
   ```

3. **Application Layout:**
   The Streamlit application layout is defined with sections for text classification, sentiment analysis, and NER.
   ```python
   st.title("Text Analysis Tool")

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
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to customize this README file as per your project's specific details and requirements.
