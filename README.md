# 🛡️ SafeGuard AI

**SafeGuard AI** is a personal safety assistant built with [Streamlit](https://streamlit.io/).  
It helps users trigger emergency alerts and tracks how many people have used the system — perfect for quick deployment and real-time usage analytics.

---

## 🔗 Live Demo

Try the live app here:  
**[https://safeguard-ai-app-krw2hn6bd9qtoudqwblltk.streamlit.app](https://safeguard-ai-app-krw2hn6bd9qtoudqwblltk.streamlit.app)**

---

## ✨ Features

- **Emergency Alert Button**  
  Instantly trigger a simulated emergency response.

- **User Tracking**  
  Logs the total number of visitors and displays it in the app.

- **Lightweight Deployment**  
  Runs on free Streamlit Cloud — no server setup needed.

---

## 🧠 How It Works

- The app stores a `visit_counter.txt` file that increments every time someone accesses the app.
- The emergency alert is simulated with a warning message and timestamp.

---

## 🛠️ Run Locally

```bash
git clone https://github.com/Srijon25/safeguard-ai-streamlit.git
cd safeguard-ai-streamlit

# (Create a virtual environment if you want)
pip install streamlit
streamlit run safeguard_app.py
