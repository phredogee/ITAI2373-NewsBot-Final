# src/utils.py

import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Initialize stopwords once
STOPWORDS = set(stopwords.words("english"))

def basic_clean_text(text):
    """
    Perform basic cleaning on text.
    """
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


def advanced_clean_text(text):
    """
    Perform advanced cleaning on text.
    Removes punctuation, numbers, and extra whitespace.
    """
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


def preprocess_text(text):
    """
    Simple preprocessing pipeline.
    """
    text = basic_clean_text(text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in STOPWORDS and word.isalpha()]
    return tokens


def calculate_reduction(original_text, processed_tokens):
    """
    Calculate reduction percentage after preprocessing.
    """
    original_len = len(word_tokenize(original_text))
    processed_len = len(processed_tokens)

    reduction = ((original_len - processed_len) / original_len) * 100
    return round(reduction, 2)


def print_top_words(counter_obj, n=10):
    """
    Print top N words from a Counter object.
    """
    for word, count in counter_obj.most_common(n):
        print(f"{word}: {count}")
