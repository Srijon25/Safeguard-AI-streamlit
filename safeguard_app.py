import streamlit as st
from datetime import datetime

# ------------------- Sidebar: Project Roadmap -------------------
with st.sidebar.expander("🚧 Project Roadmap", expanded=False):
    st.markdown("""
### ✅ Step 1: Crime Data Collection & Integration *(In Progress)*
- Integrating real-time crime data sources (e.g., **CrimeoMeter**, **UNODC**, etc.)
- Fetching location-based crime statistics to fuel AI analysis and maps.

---

### 🔜 Step 2: Crime Hotspot Mapping *(Next)*
- Displaying high-risk zones on an interactive global map.
- Color-coded visualizations for crime density and threat levels.

---

### 🔜 Step 3: Safe Route Suggestion
- AI-assisted safe route planning using **Google Maps**.
- Dynamic rerouting in real-time to avoid crime-prone areas.

---

### 🔜 Step 4: SOS & Emergency Alerts
- **Voice-activated SOS trigger** (e.g., "Help me!") from anywhere in the app.
- Global emergency contact system (country-specific numbers auto-selected).
- Optional offline SOS mode with local alerting.

---

### 🔜 Step 5: AI Risk Analysis & Prediction
- AI-generated **risk scores** based on current and historical crime data.
- **Predictive alerts** for possible safety threats based on trends and patterns.
    """)

# ------------------- Main App Interface -------------------
st.title("SafeGuard AI")
st.subheader("Real-time AI-powered safety monitoring & alerts")

st.markdown("Welcome to **SafeGuard AI** – your personal safety assistant that helps predict, analyze, and alert you to possible dangers in real time.")

# Simulated user session tracking
if "visits" not in st.session_state:
    st.session_state.visits = 1
else:
    st.session_state.visits += 1

st.success(f"Session count: {st.session_state.visits} visits")

# Dummy Location Input
location = st.text_input("Enter your location (city or coordinates):", "New York")

# Simulated Crime Level Output
if location:
    st.write(f"Fetching safety data for **{location}**...")
    st.info("Current Crime Risk Level: **Moderate**")
    st.progress(50)

# SOS Button (simulation only)
if st.button("Trigger SOS"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.error(f"SOS Triggered at {timestamp}")
    st.balloons()

# Footer
st.caption("Built with Streamlit | AI for Public Safety | © 2025 SafeGuard AI")
