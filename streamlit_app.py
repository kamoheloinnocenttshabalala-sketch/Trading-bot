import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Entry Bot - Gold 0.10 | NAS 0.05")

market = st.selectbox("Market", ["Gold XAUUSD", "NAS100"])
symbol = "GC=F" if "Gold" in market else "^NDX"
lots = 0.10 if "Gold" in market else 0.05

try:
    data = yf.download(symbol, period="5d", interval="1h", progress=False, auto_adjust=True)
    if data is None or len(data) == 0:
        st.warning("Market data loading... refresh page")
        st.stop()

    col = 'Close' if 'Close' in data.columns else data.columns[-1]
    closes = data[col]
    close_price = float(closes.iloc[-1])
    ma = float(closes.rolling(20).mean().iloc[-1]) if len(closes) > 20 else close_price
    signal = "BUY" if close_price > ma else "SELL"

    st.metric("Price", f"{close_price:.2f}")
    st.metric("Signal", signal)
    st.write(f"Lot size: {lots}")
    st.line_chart(closes.tail(50))

except Exception as e:
    st.error("Loading... click Refresh. Market may be closed.")
    st.write(str(e))
