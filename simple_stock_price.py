import yfinance as yf
import streamlit as st
import pandas as pd 
import datetime as dt


st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google, Apple, Tesla, or any Company !
""")


#pruebas

#symbol selector
options = st.selectbox('Symbol',options=['GOOGL','AAPL','TSLA','Other'])
#if other is selected, a single line text input appears
if options == 'Other':
    options = st.text_input('Enter symbol').upper()


#dates selector
appointment = st.slider(
"Date Range",
value=(dt.date(2000,1,1), dt.date.today()))



# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
period = st.selectbox('Period',options=['Daily','Weekly','Monthly','Cuarter','Six Months','Yearly','Two Years','Five Years','Ten Years','Year to Date','max'])

if period == 'Daily':
    period = '1d'
elif period == 'Weekly':
    period = '5d'
elif period == 'Monthly':
    period = '1mo'
elif period == 'Cuarter':
    period = '3mo'
elif period == 'Six Months':
    period = '6mo'
elif period == 'Yearly':
    period = '1y'
elif period == 'Two Years':
    period = '2y'
elif period == 'Five Years':
    period = '5y'
elif period == 'Ten Years':
    period = '10t'
elif period == 'Year to Date':
    period = 'ytd'




#define ticker symbol
tickerSymbol = options
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get historical prices for this ticker
tickerDf = tickerData.history(period=period,start=appointment[0], end = appointment[1])

#closing price graph
st.write(f"""### {options} Closing Price""")
st.line_chart(tickerDf.Close)
#volume graph
st.write(f"""### {options} Volume""")
st.bar_chart(tickerDf.Volume)

