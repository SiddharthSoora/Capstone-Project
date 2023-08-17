from transformers import T5ForConditionalGeneration, T5Tokenizer 
import torch
import spacy
from sense2vec import Sense2Vec
from nltk import FreqDist
from nltk.corpus import brown
from similarity.normalized_levenshtein import NormalizedLevenshtein
import numpy


class Qgen:
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained('t5-base')
        model = T5ForConditionalGeneration.from_pretrained('Parth/result') # Importing Pretraining  
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)

        self.device = device
        self.model = model
        self.nlp = spacy.load('en_core_web_sm')
        
        self.s2v = Sense2Vec().from_disk("s2v_old")
        self.fdist = FreqDist(brown.words())
        self.normalized_levenshtein = NormalizedLevenshtein()
        self.set_seed(42)

    def set_seed(self, seed):
        numpy.random.seed(seed)
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)