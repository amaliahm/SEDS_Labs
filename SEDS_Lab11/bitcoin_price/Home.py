import streamlit as st
import pandas as pd
import yfinance as yf
import json
import plotly.graph_objs as go
from Pages.file_1 import date_range_selector
from Pages.file_2 import select_and_plot_columns
from datetime import datetime
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Bitcoin Price",
    page_icon="💰",
    initial_sidebar_state="expanded",
)

st.title("Bitcoin :red[Price] :green[Analysis] :blue[App]")
st.header("SEDS lab")

st.text("This is a simple web app to view the Bitcoin price")

with open('data/bitcoin_price.json') as f:
    data = json.load(f)

btc_df_jsn = pd.DataFrame.from_dict(data)

start_date, end_date = date_range_selector()

if start_date and end_date:
    st.write(f"Fetching data from {start_date} to {end_date}...")
    btc_yf_df = yf.download('BTC-USD', start=start_date, end=end_date, interval='1d')
    
    if not btc_yf_df.empty:
        

        btc_yf_df.columns = ['_'.join(map(str, col)) for col in btc_yf_df.columns]

        btc_yf_df.columns = btc_yf_df.columns.str.lower()

        btc_yf_df = btc_yf_df.rename(columns={
            'date_': 'date',
            'adj close_btc-usd': 'adj close',
            'close_btc-usd': 'close',
            'high_btc-usd': 'high',
            'low_btc-usd': 'low',
            'open_btc-usd': 'open',
            'volume_btc-usd': 'volume'
        })

        btc_yf_df.columns = btc_yf_df.columns.str.lower()

        btc_df_jsn.rename(columns ={'time':'Date'}, inplace = True)
        btc_df_jsn['Date'] = pd.to_datetime(btc_df_jsn['Date'], unit='ms')
        btc_df_jsn.set_index('Date', inplace=True)
        
        btc_combined_df = pd.concat([btc_df_jsn, btc_yf_df], axis=0)

        if 'adj close' in btc_combined_df.columns:
            btc_combined_df.drop(columns=['adj close'], inplace=True)
        
        btc_combined_df['symbol'].fillna('UNKNOWN')

        numeric_df = btc_combined_df.select_dtypes(include='number')
        st.header('Numeric values')
        st.write(numeric_df.head())
        
        st.header('Time Series Plots')
        fig, ax = plt.subplots(figsize=(10, 6))
        btc_combined_df['open'].plot(label='Open Price', ax=ax)
        btc_combined_df['close'].plot(label='Close Price', ax=ax)
        ax.set_title('Bitcoin Price: Open vs Close')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price (USD)')
        ax.legend()
        
        st.pyplot(fig)

        select_and_plot_columns(btc_combined_df)
        
        st.header('Correlation Matrix')
        correlation_matrix = btc_combined_df[['open', 'close', 'high', 'low', 'volume']].corr()
        st.write(correlation_matrix)
        
        
        
        btc_combined_df.to_csv('data/cleaned_bitcoin_data.csv')
        
        st.write("Cleaned Data saved to 'cleaned_bitcoin_data.csv'")
        
        st.header('Cleaned DataFrame')
        st.write(btc_combined_df)
    else:
        st.warning("No data available for the selected date range.")