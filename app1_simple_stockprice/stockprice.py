#data driven web application 1 

import yfinance as yf 
import streamlit as st
import pandas as pd
#yfinance - stock market data downloader
#streamlit -> framework for app of datascience and ML

st.write("""
# Simple Stock Price App



Shown are the stocks **Closing Price** and ***Volume*** of Google
         """)
#here is the basic code you need to collect historical stock data for Microsoft:

#define the ticker symbol
# GOOGL is for Google shares traded on stock market
# AAPL is for Apple shares traded on stock market
# MSFT for microsoft
tickerSymbol = 'GOOGL'
#Ticker Symbol is the use of letters to represent shares that are traded on the stock market

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

#draw graph on web page
st.write("""
## Closing Price
        """)
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
        """)
st.line_chart(tickerDf.Volume)
