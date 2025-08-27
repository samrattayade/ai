import pandas as pd

def load_data(filepath="spam.csv"):
    return pd.read_csv(filepath)
