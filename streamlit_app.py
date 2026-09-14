import streamlit as st
import yfinance as yf

st.set_page_config(page_title="3 Pairs Scanner FIXED", layout="centered")
st.title("📱 3 Pairs Entry Scanner")
st.caption("Gold | NAS100 | US30 - Entry + TP + SL")

PAIRS = {
    "GOLD (XAUUSD)": "GC=F",
    "NAS100 (NASDAQ)": "NQ=F", 
    "US30 (DOW)": "YM=F"
}

def get_signal(symbol):
    df = yf.download(symbol, period="5d", interval="15m", progress=False, auto_adjust=True)
    if df is None or len(df) < 50:
        return None
    
    # FIX: flatten yfinance columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    
    close = df['Close']
    
    ema20 = close.ewm(span=20).mean()
    ema50 = close.ewm(span=50).mean()
    
    # RSI calc
    delta = close.diff()
    gain = delta.clip(lower=0).ewm(alpha=1/14).mean()
    loss = -delta.clip(upper=0).ewm(alpha=1/14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    price = float(close.iloc[-1])
    e20_now = float(ema20.iloc[-1])
    e50_now = float(ema50.iloc[-1])
    e20_prev = float(ema20.iloc[-2])
    e50_prev = float(ema50.iloc[-2])
    rsi_now = float(rsi.iloc[-1])

    buy = e20_now > e50_now and e20_prev <= e50_prev and rsi_now > 50
    sell = e20_now < e50_now and e20_prev >= e50_prev and rsi_now < 50
    
    if buy:
        sl = price * 0.995
        if "NQ" in symbol or "YM" in symbol:
            sl = price * 0.998
        tp = price + (price - sl) * 2
        return "BUY 🟢", price, sl, tp
    elif sell:
        sl = price * 1.005
        if "NQ" in symbol or "YM" in symbol:
            sl = price * 1.002
        tp = price - (sl - price) * 2
        return "SELL 🔴", price, sl, tp
    else:
        return "WAIT ⚪", price, 0, 0

import pandas as pd

for name, ticker in PAIRS.items():
    try:
        result = get_signal(ticker)
        if result is None:
            st.warning(f"{name} - no data")
            continue
        signal, entry, sl, tp = result
        st.subheader(name)
        if "WAIT" in signal:
            st.info(f"{signal} - Price: {entry:.2f}")
        else:
            st.success(f"""
            **SIGNAL: {signal}**
            Entry: {entry:.2f}
            Stop Loss: {sl:.2f}
            Take Profit: {tp:.2f}
            RR 1:2
            """)
    except Exception as e:
        st.error(f"{name} - {e}")

if st.button("Refresh Scan"):
    st.rerun()
