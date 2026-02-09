import streamlit as st
from vision_analyzer import analyze_chart

st.set_page_config(page_title="AI Trading Assistant", layout="centered")
st.title("Professional AI Trading Assistant")

st.warning("""
⚠️ **Financial Disclaimer**

This AI tool is provided strictly for educational and informational purposes only.  
It does NOT constitute financial advice, investment recommendations, or trading signals.

We do NOT guarantee accuracy, profitability, or future results.

Trading involves substantial risk, and you are solely responsible for your investment decisions.
""")

st.markdown(
    "[👉 View Source Code on GitHub](https://github.com/jatin-wig/Trade-Validator-AI)",
)

st.divider()


st.subheader("Trade Context")

col1, col2 = st.columns(2)

with col1:
    asset = st.text_input("Asset", placeholder="e.g., BTCUSDT, S&P 500")
    timeframe = st.selectbox(
        "Timeframe",
        ["1m", "5m", "15m", "1H", "4H", "Daily", "Weekly"]
    )

with col2:
    style = st.selectbox(
        "Trading Style",
        ["Scalping", "Intraday", "Swing", "Positional"]
    )
    risk = st.selectbox(
        "Risk Per Trade",
        ["0.5%", "1%", "2%", "3%", "5%"]
    )

entry = st.text_input("Planned Entry Price (optional)")
indicators = st.text_input(
    "Indicators Used",
    placeholder="e.g., RSI, MACD, VWAP"
)

st.divider()
uploaded_file = st.file_uploader(
    "Upload Trading Chart",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    st.image(uploaded_file, use_container_width=True)

    if st.button("Run Professional Analysis"):

        trade_data = {
            "asset": asset,
            "timeframe": timeframe,
            "style": style,
            "risk": risk,
            "entry": entry,
            "indicators": indicators
        }

        with st.spinner("Running institutional-grade analysis..."):
            result = analyze_chart(uploaded_file, trade_data)

        st.success("Analysis Ready")

        st.text_area("Trading Desk Insight", result, height=350)