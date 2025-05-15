import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
import random

st.set_page_config(page_title="SafeGuard AI", layout="wide")
st.title("SafeGuard AI - Personal Safety Companion")

# Step 1: Crime Data Simulation (can be replaced with real API)
def get_crime_data(lat, lon):
    # Simulated risk level (1 to 10)
    return random.randint(1, 10)

# Step 2: Display Map with Risk Zones
st.header("Step 2: Crime Hotspot Map")

location = st.text_input("Enter a location (e.g., New York, NY):", "New York, NY")
map_button = st.button("Show Crime Map")

if map_button:
    geocode_url = f"https://nominatim.openstreetmap.org/search?q={location}&format=json"
    geocode_response = requests.get(geocode_url).json()
    if geocode_response:
        lat = float(geocode_response[0]['lat'])
        lon = float(geocode_response[0]['lon'])

        folium_map = folium.Map(location=[lat, lon], zoom_start=13)

        for _ in range(20):
            offset_lat = lat + random.uniform(-0.01, 0.01)
            offset_lon = lon + random.uniform(-0.01, 0.01)
            risk_level = get_crime_data(offset_lat, offset_lon)
            color = 'red' if risk_level > 7 else 'orange' if risk_level > 4 else 'green'
            folium.CircleMarker(
                location=[offset_lat, offset_lon],
                radius=7,
                color=color,
                fill=True,
                fill_opacity=0.6,
                popup=f"Risk level: {risk_level}"
            ).add_to(folium_map)

        st_data = st_folium(folium_map, width=700)
    else:
        st.error("Location not found. Try a different address.")

# Step 3: Safe Route Planning (Mockup)
st.header("Step 3: Safe Route Planning")
start = st.text_input("Start Location", "Times Square, NYC")
destination = st.text_input("Destination", "Central Park, NYC")
if st.button("Suggest Safe Route"):
    st.info(f"Safe route from {start} to {destination} avoiding crime hotspots (Feature under development).")

# Step 4: SOS Activation (Mockup)
st.header("Step 4: SOS & Emergency Alerts")
sos_button = st.button("Activate SOS")
if sos_button:
    st.warning("SOS Triggered! Alert sent to emergency contacts.")

# Step 5: AI Risk Score (Simulated)
st.header("Step 5: AI Risk Analysis")
if st.button("Get Current Risk Score"):
    risk_score = random.randint(1, 10)
    st.metric("Your Location Risk Score", risk_score, delta=None)
    if risk_score > 7:
        st.error("High Risk! Avoid this area.")
    elif risk_score > 4:
        st.warning("Moderate Risk. Stay alert.")
    else:
        st.success("Low Risk. You're safe.")


