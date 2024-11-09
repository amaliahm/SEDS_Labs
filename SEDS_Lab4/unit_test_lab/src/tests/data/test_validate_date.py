import pandas as pd
import os

def is_row_valid(row):
    if row.isnull().any():
        return False
    return True

def load_data():
    file_path = '/home/mina/esi/tp/SEDS_Labs/SEDS_Lab4/unit_test_lab/data/raw/housePrice.csv'
    return pd.read_csv(file_path)
    
     

def test_is_row_valid():
    df = load_data()
    
    for i, row in df.iterrows():
        assert isinstance(is_row_valid(row), bool)  

