import streamlit as st
import requests

# 1. Configuration - Strictly using http:// for your Free Tier account
API_KEY = "5a4cb3067ff4231fd3bee05e5aaa714a"
BASE_URL = "http://api.weatherstack.com/current"

# 2. Page Configuration
st.set_page_config(page_title="Noman's Weather App", page_icon="🌤️")
st.title("🌤️ Global Weather Dashboard")
st.markdown(f"**Developer:** Muhammad Noman | **UET Taxila**")

# 3. Session State for History
if "history" not in st.session_state:
    st.session_state.history = []

# 4. User Input
city = st.text_input(
    "Enter City Name (e.g., Taxila, London, Tokyo):", "Taxila, Pakistan"
)

if st.button("Get Weather"):
    params = {
        "access_key": API_KEY,
        "query": city,
        "units": "m",  # Metric units for Celsius
    }

    try:
        # Making the call
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Check if the API returned an error
        if "error" in data:
            error_msg = data["error"]["info"]
            st.error(f"API Error: {error_msg}")
            if data["error"]["code"] == 615:
                st.warning(
                    "Tip: Try adding the country name (e.g., 'Taxila, Pakistan' instead of just 'Taxila')."
                )

            # Debugging tool for you
            with st.expander("Why did it fail?"):
                st.json(data)
        else:
            # 5. Success! Extracting data
            loc = data["location"]
            cur = data["current"]

            # Save to search history
            if loc["name"] not in st.session_state.history:
                st.session_state.history.append(loc["name"])

            st.header(f"Weather in {loc['name']}, {loc['country']}")

            # Creating a professional layout
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(cur["weather_icons"][0], width=100)
                st.write(f"**{cur['weather_descriptions'][0]}**")

            with col2:
                st.metric("Temperature", f"{cur['temperature']}°C")
                st.metric("Humidity", f"{cur['humidity']}%")

            with col3:
                st.metric("Wind Speed", f"{cur['wind_speed']} km/h")
                st.metric("Pressure", f"{cur['pressure']} mb")

            # Data Science Extra: Raw JSON Data
            with st.expander("View Raw Data Analysis"):
                st.json(data)

    except Exception as e:
        st.error("Could not connect to the weather service. Check your internet.")

# 6. Sidebar Search History
with st.sidebar:
    st.header("Recent Searches")
    for item in st.session_state.history[-5:]:
        st.write(f"📍 {item}")
