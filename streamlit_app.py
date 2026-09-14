import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Aggressive Skull Bot",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - Aggressive Skull Theme
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stButton>button { background: linear-gradient(90deg, #ff0000, #8b0000); color: white; font-weight: bold; border-radius: 10px; }
    h1 { color: #ff0000; text-shadow: 2px 2px 4px #000; }
</style>
""", unsafe_allow_html=True)

st.title("💀 AGGRESSIVE SKULL TRADING BOT")
st.markdown("### 🔥 AI Powered • Auto Trading • Live Signals")

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=100)
    st.header("⚙️ Bot Controls")
    symbol = st.selectbox("Symbol", ["BTC/USD", "ETH/USD", "XRP/USD", "SOL/USD", "GOLD"])
    amount = st.number_input("Amount ($)", 10, 10000, 100)
    risk = st.slider("Risk Level", 1, 10, 7)
    auto_trade = st.toggle("🤖 Auto Trade ON/OFF", value=False)
    
    if st.button("🚀 START BOT"):
        st.success("Bot Started!")
    
    st.divider()
    st.metric("Balance", "$1,247.50", "+12.5%")
    st.metric("Today Profit", "+$84.30", "+6.8%")

# Main dashboard
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("BTC Price", f"${random.randint(62000, 68000)}", f"{random.uniform(-2, 5):.2f}%")
with col2:
    st.metric("Signal", "BUY 🔼" if random.random() > 0.5 else "SELL 🔽", "Strong")
with col3:
    st.metric("Win Rate", "78.4%", "+2.1%")
with col4:
    st.metric("Active Trades", "3", "2 open
