import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="3 Pairs Signal Scanner", layout="centered")
st.title("📱 3 Pairs Entry Scanner")
st.caption("Gold | NAS100 | US30 - Entry + TP + SL")

# YOUR 3 PAIRS
PAIRS = {
    "GOLD (XAUUSD)": "GC=F",
    "NAS100 (NASDAQ)": "NQ=F", 
    "US30 (DOW)": "YM=F"
}

def get_signal(symbol):
    df = yf.download(symbol, period="5d", interval="15m", progress=False)
    if len(df) < 50:
        return None
    df['EMA20'] = df['Close'].ewm(span=20).mean()
    df['EMA50'] = df['Close'].ewm(span=50).mean()
    df['RSI'] = 100 - (100 / (1 + df['Close'].diff().clip(lower=0).ewm(14).mean() / (-df['Close'].diff().clip(upper=0).ewm(14).mean())))
    
    last = df.iloc[-1]
    prev = df.iloc[-2]
    price = float(last['Close'])
    
    # BUY LOGIC
    buy = last['EMA20'] > last['EMA50'] and prev['EMA20'] <= prev['EMA50'] and last['RSI'] > 50
    # SELL LOGIC
    sell = last['EMA20'] < last['EMA50'] and prev['EMA20'] >= prev['EMA50'] and last['RSI'] < 50
    
    if buy:
        sl = price * 0.995  # 0.5% SL for Gold, adjust
        if "NQ" in symbol or "YM" in symbol:
            sl = price * 0.998
        tp = price + (price - sl) * 2  # 1:2 RR
        return "BUY 🟢", price, sl, tp
    elif sell:
        sl = price * 1.005
        if "NQ" in symbol or "YM" in symbol:
            sl = price * 1.002
        tp = price - (sl - price) * 2
        return "SELL 🔴", price, sl, tp
    else:
        return "WAIT ⚪", price, 0, 0

for name, ticker in PAIRS.items():
    try:
        signal, entry, sl, tp = get_signal(ticker)
        st.subheader(f"{name}")
        if signal.startswith("WAIT"):
            st.info(f"{signal} - Price: {entry:.2f}")
        else:
            st.success(f"""
            **SIGNAL: {signal}**
            Entry: {entry:.2f}
            Stop Loss: {sl:.2f}
            Take Profit: {tp:.2f}
            RR: 1:2
            """)
    except Exception as e:
        st.error(f"{name} - error loading: {e}")

st.divider()
st.write("How to use: BUY = enter long, SELL = enter short. SL and TP already calculated.")
if st.button("Refresh Scan"):
    st.rerun()
