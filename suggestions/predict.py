""" Define predict function to predict strains from user input. """

# Imports
from joblib import load
import pandas as pd

# Load pickled models
nn = load('assets/baseline_compressed.pkl')
tfidf = load('assets/tfidf.pkl')


def suggest_strains(input):
    """
    Generate strain suggestions from user input.
    Inputs JSON, outputs a bracketed string of 5 strains.
    """
    series_input = pd.Series(input)
    vect_input = tfidf.transform(series_input)
    score, recommended_strains = nn.kneighbors(vect_input.todense())
    return recommended_strains
