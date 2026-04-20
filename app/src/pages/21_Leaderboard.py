import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title("🥇 Leaderboard")
st.write("See where you stand against other players.")

API_BASE = "http://web-api:4000"

limit = st.slider("Number of players to show", 5, 50, 20)

try:
    r = requests.get(f"{API_BASE}/competitive/leaderboard?limit={limit}")
    if r.status_code == 200:
        data = r.json()
        if data:
            df = pd.DataFrame(data)
            df.index = df.index + 1
            df.index.name = "Rank"
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No leaderboard data available.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
st.subheader("📊 Meta Trends")
season = st.selectbox("Season", ["Season 18", "Season 19", "Season 20", "Season 21"])
try:
    r = requests.get(f"{API_BASE}/competitive/meta/trends?season={season}")
    if r.status_code == 200:
        data = r.json()
        if data:
            st.dataframe(pd.DataFrame(data), use_container_width=True)
        else:
            st.info("No meta trend data available.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")
