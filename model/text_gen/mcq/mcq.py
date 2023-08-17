import numpy as np # linear algebra
from nltk.tokenize import sent_tokenize
def tokenize_sentences(text):
    sentences = sent_tokenize(text)
    print(sentences)
    sentences = [y for x in sentences for y in x] # flatten list
    sentences = [sentence.strip() for sentence in sentences if len(sentence) > 20] # Remove all the sentenses with less than 20 letters
    return sentences

def get_keywords()