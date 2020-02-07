# Define Recommender class to predict strains from user input.

# Imports
import basilica
from joblib import load
import numpy as np
import os


class Suggester():
    """
    Generate five strain suggestions from user input.
    """
    def __init__(self):
        self.scaler = load('assets/scaler.pkl')
        self.pca = load('assets/pcaer.pkl')
        self.normalizer = load('assets/normd.pkl')
        self.nn = load('assets/nnmodel.pkl')
        self.API_KEY = os.getenv('API_KEY')

    def strain_suggester(self, input, neighbors=5):
        """
        Use Basilica to embed input from user and return strains.
        Input run through a process that includes a Standard Scaler,PCA to
        reduce dimensionality down to 75, normalize input, then a
        nearest neighbors model that returns 5
        recommended strains id's.
        """
        with basilica.Connection(self.API_KEY) as c:
            embedded_sentence = c.embed_sentence(input)

        embedded = np.stack([embedded_sentence], axis=0)
        scaled = self.scaler.transform(embedded)
        pcaed = self.pca.transform(scaled)
        normalized = self.normalizer.transform(pcaed)

        results = self.nn.kneighbors(normalized, neighbors)[1][0].tolist()

        return results
