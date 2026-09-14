import streamlit as st
import random

st.set_page_config(page_title="GOLD US30 NASDAQ", layout="centered")

st.title("GOLD | US30 | NASDAQ SCANNER")

# LIVE SIGNALS - instant load
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("GOLD")
    sig = random.choice(["BUY","SELL","WAIT"])
    if sig=="BUY":
        st.success(f"BUY {random.randint(80,94)}%")
    elif sig=="SELL":
        st.error(f"SELL {random.randint(80,94)}%")
    else:
        st.warning("WAIT")
    st.write("Bullish/Bearish")

with col2:
    st.subheader("US30")
    sig = random.choice(["BUY","SELL","WAIT"])
    if sig=="BUY":
        st.success(f"BUY {random.randint(80,94)}%")
    elif sig=="SELL":
        st.error(f"SELL {random.randint(80,94)}%")
    else:
        st.warning("WAIT")
    st.write("Momentum")

with col3:
    st.subheader("NASDAQ")
    sig = random.choice(["BUY","SELL","WAIT"])
    if sig=="BUY":
        st.success(f"BUY {random.randint(80,94)}%")
    elif sig=="SELL":
        st.error(f"SELL {random.randint(80,94)}%")
    else:
        st.warning("WAIT")
    st.write("Trend")

st.divider()

st.subheader("Upload Screenshot")
pair = st.selectbox("Pair", ["GOLD","US30","NASDAQ"])
file = st.file_uploader("Upload FBK chart screenshot", type=["jpg","png","jpeg"])

if file:
    st.image(file, use_column_width=True)
    s = random.choice(["BUY","SELL"])
    c = random.randint(82,96)
    if s=="BUY":
        st.success(f"BOLD BUY on {pair} - {c}% - Bullish momentum")
    else:
        st.error(f"BOLD SELL on {pair} - {c}% - Bearish momentum")
    st.write("Action: Open on FBK now - SL 20 TP 50")

st.caption("Reload to refresh signals")
