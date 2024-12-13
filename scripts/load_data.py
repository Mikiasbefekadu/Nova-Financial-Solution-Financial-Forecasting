import pandas as pd

def loaddata(file_path):
    """Load dataset and preprocess columns."""
    df = pd.read_csv(file_path)
    return df
