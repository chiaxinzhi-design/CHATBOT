import streamlit as st

# --- 1. Set up the Form Container ---
# Wrap all your current input widgets inside st.form
with st.form(key='solo_travel_form'):
    st.title("Let's Solo Travel!!! ✈️ 🌎 ☀️ 🛳️")

    # --- 2. Input Widgets (Your Existing Code Goes Here) ---

    # Guide Selection (Example of your current code)
    guide_mode = st.radio(
        "💁Your tour guide will be...",
        ('Friendly', 'Formal', 'Funny')
    )

    # Country Selection
    country = st.selectbox(
        "🌐THE country is...",
        ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia (Czech Republic)", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See (Vatican City)", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "São Tomé and Príncipe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"] # Use your actual list of countries
    )

    # Needs Selection
    needs = st.multiselect(
        "✊I need...",
        ['Transportation', 'Accommodation', 'Visa Help', 'Luggage Checklist', 'Travel Insurance']
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
        "💰 Budget",
        min_value=500,
        max_value=50000,
        value=10000,
        step=500,
        format='MYR %d'
    )
    

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