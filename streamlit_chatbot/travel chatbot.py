import streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Let's Solo Travel!!! ✈️ 🌍 😊 🚢")

# Tour guide style
style = st.radio("🧑‍🏫 Your tour guide will be...", ["Friendly", "Formal", "Funny"])

# Country
country = st.selectbox("🛫 THE country is...", ["Malaysia", "Japan", "Thailand", "France", "USA"])

# Needs
needs = st.multiselect("✊ I need...", ["Transportations", "Hotels", "Food", "Attractions", "Guides"])

# Travel duration
days = st.slider("📅 Travels Duration (Days)", 1, 30, (5, 14))

# Budget
budget = st.slider("💰 Budget (MYR)", 1000, 20000, 10000)

# Button to generate
if st.button("✨ Generate My Travel Plan"):
    prompt = f"""
    You are a {style.lower()} travel guide.
    Suggest a solo travel plan for {country}.
    Needs: {', '.join(needs)}.
    Duration: {days[0]}–{days[1]} days.
    Budget: {budget} MYR.
    """

    response = model.generate_content(prompt)

    st.subheader("🗺️ Your Travel Suggestion:")
    st.write(response.text)
