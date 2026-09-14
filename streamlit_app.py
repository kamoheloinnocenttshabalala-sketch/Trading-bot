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
        st.warning("No data - Market closed or refresh")
        st.stop()

    col = 'Close' if 'Close' in data.columns else data.columns[-1]
    closes = data[col]

    # Fix Series issue
    last = closes.iloc[-1]
    if isinstance(last, pd.Series):
        last = last.iloc[0]
    close_price = float(last)

    ma_series = closes.rolling(20).mean().iloc[-1]
    if isinstance(ma_series, pd.Series):
        ma_series = ma_series.iloc[0]
    ma = float(ma_series) if pd.notna(ma_series) else close_price

    signal = "BUY" if close_price > ma else "SELL"

    st.metric("Price", f"{close_price:.2f}")
    st.metric("Signal", signal)
    st.write(f"Lot size: {lots}")
    st.line_chart(closes.tail(50))

except Exception as e:
    st.error(f"Retry refresh: {e}")
