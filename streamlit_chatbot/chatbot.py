import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

# --- PAGE CONFIGURATION ---
# Set the page configuration as the very first Streamlit command.
st.set_page_config(
    page_title="Let's Solo Travel!",
    page_icon="✈️",
    layout="wide"
)

# --- API CONFIGURATION ---
# Configure the Gemini API using Streamlit's secrets management
try:
    # Recommended: Use st.secrets for secure API key storage
    GOOGLE_API_KEY = st.secrets["AIzaSyBcdzk9G7nJdiMa4twA-UdZI5f3kifzLKM"]
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except (KeyError, FileNotFoundError):
    st.error("🚨 Google API Key not found. Please add it to your Streamlit secrets.")
    st.stop()


# --- MAIN APP LOGIC ---
def main():
    st.title("Let's Solo Travel!!! ✈🌎🌞🚢")
    st.write("Your adventure awaits! Select your preferences in the sidebar to generate a personalized travel plan.")

    # --- SIDEBAR FOR USER INPUTS ---
    with st.sidebar:
        st.title("✨ Your Dream Destination")

        # Input for the tour guide's persona
        tour_guide_persona = st.radio(
            "💁 Your tour guide will be...",
            ["Friendly", "Formal", "Funny"],
            index=0,
            help="Select the tone of your travel plan."
        )

        # Input for the destination country
        # A shorter, more manageable list for the example. You can replace this with your full list.
        countries = ["Japan", "Italy", "New Zealand", "Peru", "Thailand", "Egypt", "Canada", "Spain", "Australia", "Malaysia", "Vietnam", "United Kingdom", "United States", "France", "Germany"]
        selected_country = st.selectbox(
            "🗺️ THE country is...",
            countries,
            index=0
        )

        # Input for the required information
        needed_info = st.multiselect(
            "📋 I need information on...",
            ["Transportations", "Stays", "Luggage Checklist", "Local Delights", "Attractions", "Safety Tips", "Cultural Etiquette"],
            default=["Transportations", "Stays", "Attractions"],
            help="Choose the topics you want in your travel plan."
        )

        # Input for travel duration
        travel_duration = st.select_slider(
            "📆 Travel Duration (Days)",
            options=["1-4", "5-14", "15-30", "30+"],
            value="5-14"
        )

        # Input for budget
        budget = st.slider(
            "💰 Budget (MYR)",
            min_value=1000,
            max_value=50000,
            value=10000,
            step=500
        )

    # --- GENERATE AND DISPLAY THE TRAVEL PLAN ---

    # Only proceed if the user has selected at least one topic of interest
    if needed_info:
        st.subheader(f"🚀 Your Personalized Solo Travel Plan for {selected_country}")

        # Construct a detailed prompt for the AI model
        # Using an f-string to insert user selections directly into the prompt
        prompt = f"""
        Create a solo travel plan based on the following details:

        1.  **Destination:** {selected_country}
        2.  **Travel Duration:** {travel_duration} days.
        3.  **Budget:** Approximately {budget} MYR.
        4.  **Required Information:** Please provide details on the following topics: {', '.join(needed_info)}.
        5.  **Tone of Voice:** The response should be in a {tour_guide_persona} and encouraging tone, as if you are a personal tour guide.

        Please structure the output clearly with headings for each topic requested. Use markdown for formatting, including bolding key items and using bullet points for lists.
        """

        # Show a spinner while waiting for the response
        with st.spinner(f"Crafting your {tour_guide_persona} plan for {selected_country}... Please wait. ✨"):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred while generating the plan: {e}")

    else:
        st.info("Please select at least one topic you need information on from the sidebar to generate a plan.")


if __name__ == "__main__":
    main()