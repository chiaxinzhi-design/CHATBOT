import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- Streamlit UI ---
st.title("🎶 Gemini Song Suggester from Image")

st.write("Upload an image and I'll suggest a song that matches the mood or feeling!")

uploaded_file = st.file_uploader("Upload your picture", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Suggest me a song 🎵"):
        with st.spinner("Analyzing image and finding the perfect song..."):
            model = genai.GenerativeModel("gemini-1.5-flash")

            response = model.generate_content(
                [
                    "You are a music recommender. Look at this image, guess the mood/feeling, and suggest ONE song that matches. Respond with only the song title and artist.",
                    uploaded_file
                ]
            )

            suggestion = response.text
            st.success(f"🎵 Suggested Song: {suggestion}")
