import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Entry Bot")
st.title("Entry Bot - Gold 0.10 | NAS 0.05")

market = st.selectbox("Market", ["Gold XAUUSD", "NAS100", "EURUSD"])
tickers = {"Gold XAUUSD": "GC=F", "NAS100": "NQ=F", "EURUSD": "EURUSD=X"}
lot = 0.05 if "NAS" in market else 0.10

ticker = tickers[market]
data = yf.download(ticker, period="2d", interval="5m", progress=False)

if len(data) > 20:
    close = float(data['Close'].iloc[-1])
    high_break = float(data['High'].rolling(20).max().iloc[-2])
    low_break = float(data['Low'].rolling(20).min().iloc[-2])
    st.metric("Price", f"{close:.2f}", f"Lot {lot}")
    st.line_chart(data['Close'].tail(100))
    if close > high_break:
        st.success(f"BUY LIMIT {high_break:.2f} | Lot {lot}")
    elif close < low_break:
        st.error(f"SELL LIMIT {low_break:.2f} | Lot {lot}")
    else:
        st.info(f"WAITING - Lot {lot}")
