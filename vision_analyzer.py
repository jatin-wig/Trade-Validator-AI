import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash-lite")


def analyze_chart(image_file, trade_data):

    image = Image.open(image_file)

    prompt = f"""
You are an institutional-level trading analyst.

Analyze the chart using the provided professional trade context.

TRADE CONTEXT:
Asset: {trade_data['asset']}
Timeframe: {trade_data['timeframe']}
Trading Style: {trade_data['style']}
Risk Per Trade: {trade_data['risk']}
Planned Entry: {trade_data['entry']}
Indicators: {trade_data['indicators']}

Return ONLY in this structured format:

MARKET STRUCTURE:
(Bullish / Bearish / Ranging + explanation)

TRADE VALIDITY:
(Valid / Risky / Avoid)

OPTIMAL BIAS:
(Long / Short / Wait)

ENTRY QUALITY:
(Good / Chasing / Poor Location)

STOPLOSS LOGIC:
(Where and WHY — not just a number)

RISK ANALYSIS:
(Is the trader overexposed for this timeframe?)

PROFESSIONAL VERDICT:
(2–3 sharp sentences like a hedge fund analyst)

If the chart is unclear → say:
"Chart not clear enough for professional analysis."

Do NOT hallucinate.
Be precise.
Avoid generic advice.
"""

    response = model.generate_content([prompt, image])

    return response.text