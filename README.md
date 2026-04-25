# NewsBot Intelligence System 2.0

## Overview

The NewsBot Intelligence System 2.0 is an end-to-end Natural Language Processing (NLP) system that transforms raw news articles into structured insights.

This project demonstrates how modern NLP techniques can be integrated into a single pipeline capable of:

- understanding text  
- extracting meaning  
- identifying trends  
- generating insights  

It is designed to simulate a real-world news intelligence platform used in media analytics and business decision-making.

---

## Objectives

- Build an end-to-end NLP pipeline for news analysis  
- Apply machine learning models for classification and sentiment detection  
- Extract meaningful entities and relationships from text  
- Discover hidden topics within news data  
- Demonstrate real-world applicability of NLP techniques  

---

## Final Results

- **Best Model:** Logistic Regression  
- **Accuracy:** 98.88%  
- **Vectorization:** TF-IDF  
- **Dataset:** BBC News  

Multiple models were evaluated, including Naive Bayes, Logistic Regression, and LinearSVC, with Logistic Regression achieving the highest performance.

---

## Features

### 🔹 Text Processing
- Text cleaning and normalization  
- Tokenization and stop word removal  
- Lemmatization using spaCy  

### 🔹 Feature Engineering
- TF-IDF vectorization  
- Bag-of-words representation  

### 🔹 News Classification
- Logistic Regression (**best performing model**)  
- Linear Support Vector Machine (SVM)  
- Multinomial Naive Bayes  
- Model evaluation and comparison  

### 🔹 Sentiment Analysis
- Sentiment scoring using NLTK (VADER) and transformer-based models  
- Polarity classification (positive, neutral, negative)  

### 🔹 Named Entity Recognition (NER)
- spaCy-based entity extraction  
- Transformer-based NER using Hugging Face models  

### 🔹 Topic Modeling
- Latent Dirichlet Allocation (LDA)  
- Discovery of hidden themes across articles  

### 🔹 Multilingual Capability (Prototype)
- Basic language detection  
- Translation-based pipeline for non-English text  

---

## Dataset

- **Source:** BBC News Dataset  
- **Categories:** Business, Entertainment, Politics, Sport, Tech  
- **Type:** Text-based news articles  

---

## 📁 Project Structure

```text
ITAI2373-NewsBot-Final/
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── raw/
│       └── bbc-text.csv
│
├── notebooks/
│   └── FP_Presentation_AlfredoGarza_PhredoLexus_ITAI2373.ipynb
│
├── presentation/
│   └── FP_Presentation_AlfredoGarza_PhredoLexus_ITAI2373.pptx
│
├── src/
│   └── utils.py
