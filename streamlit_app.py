import streamlit as st
import yfinance as yf
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Aggressive Skull Bot", page_icon="💀", layout="centered")

st.markdown("""
<style>
.stApp { background-color: #0a0a0a; }
h1, h2, h3, p, label { color: white!important; }
div[data-testid="stMetricValue"] { color: #00ff88!important; }
</style>
""", unsafe_allow_html=True)

st.title("💀 AGGRESSIVE SKULL BOT")
st.caption("Durban Edition - Gold 0.10 | NAS100 0.05")

tab1, tab2 = st.tabs(["🔴 LIVE SIGNALS", "📸 CHART SCANNER"])

with tab1:
    market = st.selectbox("Select Market", ["Gold XAUUSD", "NAS100"], key="live")
    symbol = "GC=F" if "Gold" in market else "^NDX"
    lot = 0.10 if "Gold" in market else 0.05

    try:
        data = yf.download(symbol, period="5d", interval="1h", progress=False, auto_adjust=True)
        if len(data) == 0:
            st.warning("Market closed, try again later")
        else:
            close_col = 'Close' if 'Close' in data.columns else data.columns[0]
            price = float(data[close_col].iloc[-1])
            ma = float(data[close_col].rolling(20).mean().iloc[-1])

            signal = "BUY" if price > ma else "SELL"

            if signal == "BUY":
                sl = price * 0.998
                tp = price * 1.005
                st.success(f"🟢 {signal} NOW - LOT {lot}")
            else:
                sl = price * 1.002
                tp = price * 0.995
                st.error(f"🔴 {signal} NOW - LOT {lot}")

            c1, c2, c3 = st.columns(3)
            c1.metric("ENTRY", f"{price:.2f}")
            c2.metric("SL", f"{sl:.2f}")
            c3.metric("TP", f"{tp:.2f}")

            st
