import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIGURATION ---
# Set the page configuration. This is the first Streamlit command to be run.
st.set_page_config(
    page_title="WanderBot - Your Travel AI",
    page_icon="✈️",
    layout="centered"
)

# --- API AND MODEL CONFIGURATION ---
# Configure the generative AI model with the API key from Streamlit secrets.
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)
    # Initialize the Gemini model. Using 'gemini-1.5-flash' for faster responses.
    model = genai.GenerativeModel('gemini-1.5-flash')
except (KeyError, FileNotFoundError):
    st.error("🚨 Google API Key not found. Please add it to your Streamlit secrets (`.streamlit/secrets.toml`).")
    st.stop()

# --- CHATBOT PERSONA AND INITIALIZATION ---
# Define the persona for the chatbot. This guides the model's tone and responses.
CHATBOT_PERSONA = """
You are WanderBot, a friendly and enthusiastic travel expert chatbot. Your goal is to help users plan their dream vacations.
- Provide inspiring travel suggestions and practical tips.
- Use a cheerful and encouraging tone.
- Use emojis to make the conversation more engaging.
- Ask clarifying questions to better understand the user's needs.
- Structure responses with markdown for readability (e.g., use lists, bold text).
"""

# Initialize the chat session in Streamlit's session state.
# This ensures that the chat history is preserved across user interactions.
if "messages" not in st.session_state:
    # Start with a welcoming message from the chatbot.
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello there! 👋 I'm WanderBot. Where in the world are you dreaming of going today?"}
    ]

# --- UI AND INTERACTION ---
st.title("WanderBot ✈️")
st.caption("Your AI-Powered Travel Planning Assistant")

# Display the past chat messages from the session state.
for message in st.session_state.messages:
    # Use st.chat_message to display messages in a chat-like format.
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# The chat input widget for the user to type their message.
if prompt := st.chat_input("Ask about your next adventure!"):
    # 1. Add the user's message to the session state.
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 2. Display the user's message in the chat interface.
    with st.chat_message("user"):
        st.markdown(prompt)

    # 3. Generate and display the assistant's response.
    with st.chat_message("assistant"):
        # Show a thinking spinner while waiting for the model's response.
        with st.spinner("WanderBot is charting a course..."):
            # Construct the full prompt including the persona and the user's query.
            full_prompt = f"{CHATBOT_PERSONA}\n\nUser Question: {prompt}"

            # Call the generative model.
            try:
                response = model.generate_content(full_prompt)
                response_text = response.text
            except Exception as e:
                response_text = f"Sorry, I ran into a little turbulence. Please try again! Error: {e}"

            # Display the response with a streaming effect.
            st.markdown(response_text)

    # 4. Add the assistant's response to the session state.
    st.session_state.messages.append({"role": "assistant", "content": response_text})