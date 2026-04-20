import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title("🔥 Meta Hub")
st.write("See the current top performing legends and weapons without doing the research yourself.")

API_BASE = "http://web-api:4000"

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔫 Top Weapons")
    try:
        r = requests.get(f"{API_BASE}/casual/meta/top-weapons")
        if r.status_code == 200:
            data = r.json()
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True)
                st.bar_chart(df.set_index('weapon_name')['avg_kd'])
            else:
                st.info("No weapon data available.")
        else:
            st.error(f"Error: {r.status_code}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")

with col2:
    st.subheader("🦸 Top Legends")
    try:
        r = requests.get(f"{API_BASE}/casual/meta/top-legends")
        if r.status_code == 200:
            data = r.json()
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True)
                st.bar_chart(df.set_index('legend_name')['avg_win_rate'])
            else:
                st.info("No legend data available.")
        else:
            st.error(f"Error: {r.status_code}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")

st.divider()
st.subheader("🔔 My Notifications")
player_id = st.session_state.get('player_id', 3)
try:
    r = requests.get(f"{API_BASE}/casual/players/{player_id}/notifications")
    if r.status_code == 200:
        data = r.json()
        if data:
            st.dataframe(pd.DataFrame(data), use_container_width=True)
        else:
            st.info("No notifications.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")
