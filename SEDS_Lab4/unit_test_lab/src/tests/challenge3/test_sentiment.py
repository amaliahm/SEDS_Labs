from textblob import TextBlob
import pandas as pd
import pytest
import os

df = pd.read_csv('/home/mina/esi/tp/science de donnees/SEDS_Lab4/unit_test_lab/data/raw/soccer_sentiment_analysis.csv') 
testdata = df['Text'].tolist()

def extract_sentiment(text: str):
    text = TextBlob(text)

    return text.sentiment.polarity

# testdata =["Borussia Dortmund’s loss was heartbreaking as they failed to gain momentums from their  two goals advance. Very disappointing results for our Algerian player Bensebaini.", "Barcelona played brilliantly last Wednesday. Rafinia’s hat-trick was pure magic. Visca Barça!"]

@pytest.mark.parametrize('sample', testdata)

def test_extract_sentiment(sample):

    neg_sentiment = extract_sentiment(sample)

#    assert sample == testdata[0] or neg_sentiment > 0
#    if sample == testdata[0]:
#        assert neg_sentiment <= 0
#    else:
#        assert neg_sentiment > 0
        
    if 'loss' in sample or 'disappointing' in sample:
        assert neg_sentiment <= 0 
    else:
        assert neg_sentiment > 0
        
        


