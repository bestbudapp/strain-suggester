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
    df = pd.DataFrame(vect_input.todense())
    score, recommended_strains = nn.kneighbors(df)
    return recommended_strains
