from textblob import TextBlob

def extract_sentiment(text: str):
    text = TextBlob(text)

    return text.sentiment.polarity
