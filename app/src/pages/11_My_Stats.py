import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title("📊 My Stats")
st.write("Track your best personal stats to compare with friends.")

API_BASE = "http://web-api:4000"
player_id = st.session_state.get('player_id', 3)

try:
    r = requests.get(f"{API_BASE}/casual/players/{player_id}/stats")
    if r.status_code == 200:
        data = r.json()
        if data:
            df = pd.DataFrame(data)
            visible = df[df['is_visible'] == 1] if 'is_visible' in df.columns else df
            st.subheader("Your Tracked Stats")
            st.dataframe(visible, use_container_width=True)
        else:
            st.info("No stats tracked yet.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
st.subheader("🏅 Best Legends & Weapons")
try:
    r = requests.get(f"{API_BASE}/casual/players/{player_id}/best-legends-weapons")
    if r.status_code == 200:
        data = r.json()
        if data:
            st.dataframe(pd.DataFrame(data), use_container_width=True)
        else:
            st.info("No legend/weapon data found.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
st.subheader("🙈 Hide a Stat Entry")
with st.form("hide_stat"):
    stat_id = st.number_input("Stat Entry ID to hide", min_value=1, step=1)
    if st.form_submit_button("Hide Stat"):
        try:
            r = requests.put(f"{API_BASE}/casual/players/stats/{stat_id}/hide")
            if r.status_code == 200:
                st.success("Stat hidden successfully!")
                st.rerun()
            else:
                st.error(f"Error: {r.json()}")
        except Exception as e:
            st.error(f"Could not connect to API: {e}")
