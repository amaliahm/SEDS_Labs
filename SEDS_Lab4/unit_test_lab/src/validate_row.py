import pandas as pd
import os

def is_row_valid(row):
    if row.isnull().any():
        return False
    
    return True

def load_data(filepath):
    file_path = os.path.join(os.path.dirname(__file__), '../../data/raw/housing_price.csv')
    return pd.read_csv(filepath)

