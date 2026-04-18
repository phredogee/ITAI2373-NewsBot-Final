# NewsBot Intelligence System 2.0

## Overview

The NewsBot Intelligence System 2.0 is an end-to-end Natural Language Processing (NLP) system that transforms raw news articles into structured insights.

This project demonstrates how modern NLP techniques can be integrated into a single pipeline capable of:

- understanding text
- extracting meaning
- identifying trends
- generating summaries

It is designed to simulate a real-world news intelligence platform used in media analytics and business decision-making.

## Objectives
- Build an end-to-end NLP pipeline for news analysis
- Apply machine learning models for classification and sentiment detection
- Extract meaningful entities and relationships from text
- Discover hidden topics within news data
- Integrate modern language models for summarization
- Demonstrate real-world applicability of NLP techniques

## Features
🔹 Text Processing
- Text cleaning and normalization
- Tokenization and stop word removal
- Lemmatization for improved semantic consistency
🔹 Feature Engineering
- TF-IDF vectorization
- Bag-of-words representation
🔹 News Classification
- Logistic Regression
- Linear Support Vector Machine (SVM)
- Naive Bayes
- Model evaluation and comparison
🔹 Sentiment Analysis
- Rule-based sentiment scoring
- Polarity classification (positive, neutral, negative)
🔹 Named Entity Recognition (NER)
- Rule-based entity extraction
- Transformer-based NER using Hugging Face models
- Comparative analysis of approaches
🔹 Topic Modeling
- Latent Dirichlet Allocation (LDA)
- Discovery of hidden themes across articles
🔹 Language Model Integration
- Text summarization using transformer models
- Automatic generation of concise article summaries
🔹 Multilingual & Conversational (Prototype)
- Basic language detection
- Simple natural language query interface

## Dataset
Source: BBC News Dataset
Categories: Business, Entertainment, Politics, Sport, Tech
Type: Text-based news articles

## Project Structure
ITAI2373-NewsBot-Final/
├── README.md                      # Project overview and instructions
├── requirements.txt              # Python dependencies
├── .gitignore                    # Files and folders to ignore in version control
│
├── data/
│   └── raw/
│       └── bbc-text.csv          # Original dataset used for analysis
│
├── notebooks/
│   └── NewsBot_Intelligence_System_Final.ipynb
│                                  # Main notebook containing full NLP pipeline
│
├── reports/
│   ├── FP_TechnicalDoc_YourName_GroupName_ITAI2373.pdf
│   ├── FP_ExecutiveSummary_YourName_GroupName_ITAI2373.pdf
│   └── FP_ReflectiveJournal_GroupName_ITAI2373.pdf
│                                  # Final project deliverables
│
├── slides/
│   └── FP_Presentation_YourName_GroupName_ITAI2373.pptx
│                                  # Presentation slides
│
├── src/
│   └── utils.py                  # Optional helper functions (future expansion)
│
└── images/
    └── screenshots/
        └── (optional visuals)    # Graphs and output screenshots for README

## spaCy
python -m spacy download en_core_web_sm

## Installation
pip install -r requirements.txt

## Run
Open notebooks/NewsBot_Intelligence_System_Final.ipynb in Jupyter or Colab.

🧠 System Architecture

The system is structured as a modular NLP pipeline:

- Preprocessing Layer – Cleans and standardizes raw text
- Feature Extraction Layer – Converts text into numerical features
- Analysis Layer – Classification, sentiment, NER, topic modeling
- Language Model Layer – Summarization and advanced NLP
- Interaction Layer – Query-based exploration (prototype)

## Results
- 📌 High classification accuracy using TF-IDF + linear models
- 📌 Topic modeling successfully identified category themes
- 📌 Transformer NER improved flexibility over rule-based methods
- 📌 Summarization reduced article length while preserving meaning

## Author / Team
Alfredo Garza / Alexia Chavez
ITAI 2373 – Natural Language Processing
Houston City College

## Notes
This project was developed as part of a final course assignment and demonstrates applied NLP techniques aligned with industry practices and system design expectations.
