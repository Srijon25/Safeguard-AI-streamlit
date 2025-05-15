import streamlit as st
import datetime
import os

# File to store visitor count
VISIT_FILE = "visit_counter.txt"

# Initialize counter file if it doesn't exist
if not os.path.exists(VISIT_FILE):
    with open(VISIT_FILE, "w") as f:
        f.write("0")

# Read and update visitor count
with open(VISIT_FILE, "r+") as f:
    count = int(f.read())
    count += 1
    f.seek(0)
    f.write(str(count))

# UI
st.set_page_config(page_title="SafeGuard AI", page_icon="🛡️")
st.title("🛡️ SafeGuard AI - Personal Safety Assistant")

st.markdown("Welcome to **SafeGuard AI** – your digital companion for personal safety.")

st.markdown("**Features:**")
st.markdown("- Trigger emergency alerts")
st.markdown("- Record when help is requested")
st.markdown("- Track how many people used this tool")

if st.button("🚨 Trigger Emergency Alert"):
    st.warning("Emergency alert triggered! Help is being dispatched.")
    st.info(f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

st.success(f"Total users who visited: **{count}**")
