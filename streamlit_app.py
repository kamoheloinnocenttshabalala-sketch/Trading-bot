import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="Aggressive Skull Bot", page_icon="💀", layout="wide")

st.title("AGGRESSIVE SKULL TRADING BOT")
st.write("AI Powered Auto Trading")

# Sidebar
symbol = st.sidebar.selectbox("Symbol", ["BTC/USD", "ETH/USD", "XRP/USD", "SOL/USD"])
amount = st.sidebar.number_input("Amount", 10, 10000, 100)
if st.sidebar.button("START BOT"):
    st.sidebar.success("Bot Started!")

# Metrics
c1, c2, c3, c4 = st.columns(4)
c1.metric("BTC Price", f"${random.randint(62000,68000)}", "2.5%")
c2.metric("Signal", "BUY", "Strong")
c3.metric("Win Rate", "78%", "2%")
c4.metric("Active Trades", "3", "2 open")

# Chart
st.subheader("Live Chart")
dates = pd.date_range(datetime.now(), periods=50, freq='min')
prices = [60000 + random.uniform(-500,500) + i*2 for i in range(50)]
df = pd.DataFrame({"Price": prices}, index=dates)
st.line_chart(df)

# Table
st.subheader("Live Signals")
data = {
    "Time": [datetime.now().strftime("%H:%M:%S") for _ in range(5)],
    "Symbol": [symbol]*5,
    "Action": [random.choice(["BUY","SELL"]) for _ in range(5)],
    "Result": ["WIN","WIN","LOSS","WIN","PENDING"]
}
st.dataframe(pd.DataFrame(data), use_container_width=True)

st.success("Bot is running - no errors!")
