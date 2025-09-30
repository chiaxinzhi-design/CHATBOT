import streamlit as st

# --- 1. Set up the Form Container ---
# Wrap all your current input widgets inside st.form
with st.form(key='solo_travel_form'):
    st.title("Let's Solo Travel!!! ✈️ 🌎 ☀️ 🛳️")

    # --- 2. Input Widgets (Your Existing Code Goes Here) ---

    # Guide Selection (Example of your current code)
    guide_mode = st.radio(
        "Your tour guide will be...",
        ('Friendly', 'Formal', 'Funny')
    )

    # Country Selection
    country = st.selectbox(
        "THE country is...",
        ['Afghanistan', 'USA', 'Japan'] # Use your actual list of countries
    )

    # Needs Selection
    needs = st.multiselect(
        "I need...",
        ['Transportations', 'Accommodation', 'Visa Help'],
        default=['Transportations']
    )

    # Duration Slider
    duration = st.slider(
        "📅 Travels Duration (Days)",
        min_value=5,
        max_value=30,
        value=(5, 14)
    )

    # Budget Slider
    budget = st.slider(
        "💰 Budget (MYR)",
        min_value=1000,
        max_value=30000,
        value=10000,
        step=500,
        format='MYR %d'
    )
    
    # Placeholder for the prompt/search box (moved inside the form)
    st.text_input("Where are we heading to?", disabled=True, placeholder="This is for decoration for now...")


    # --- 3. The Submit Button ---
    # The button MUST be the last element inside the st.form block
    submit_button = st.form_submit_button(label='🗺️ Generate My Solo Plan')


# --- 4. Conditional Result Display and Logic ---

# This entire block of code will ONLY execute when the submit_button is clicked
if submit_button:
    
    st.balloons() # Just for fun!

    st.header("✨ Your Custom Solo Travel Plan ✨")
    st.subheader(f"Trip to {country} with a {guide_mode} guide!")

    # Perform your planning logic based on the collected variables
    # The variables (guide_mode, country, needs, duration, budget) retain their values
    
    # Summary Table
    st.metric("Destination", country)
    st.metric("Duration", f"{duration[0]} to {duration[1]} Days")
    st.metric("Max Budget", f"MYR {budget:,}")
    st.metric("Key Focus", ", ".join(needs))
    
    # A simple example of the plan output
    st.markdown("---")
    st.markdown(
        f"""
        Based on your selections:
        
        1. **Mode of Travel:** Since you selected **{', '.join(needs)}**, the plan prioritizes reliable local transportation and booking.
        2. **Guide Personality:** Your **{guide_mode}** guide will ensure all interactions are fun and lighthearted.
        3. **Budget Analysis:** With a budget of **MYR {budget:,}** for up to **{duration[1]} days**, we can look for mid-range accommodations.
        """
    )

    st.success("Your detailed itinerary is now loading below...")
    # Add your heavy-duty processing or function calls here