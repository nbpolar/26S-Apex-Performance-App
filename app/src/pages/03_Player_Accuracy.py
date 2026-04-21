import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title("Player Accuracy by Weapon")
st.write("Analyze player accuracy across different weapon types to recommend optimal loadouts.")

API_BASE = "http://web-api:4000"

player_id = st.number_input("Player ID", min_value=1, value=1, step=1)

try:
    r = requests.get(f"{API_BASE}/coach/players/{player_id}/accuracy-by-weapon")
    if r.status_code == 200:
        data = r.json()
        if data:
            df = pd.DataFrame(data)
            st.subheader(f"Accuracy Stats for Player {player_id}")
            st.dataframe(df, use_container_width=True)

            st.subheader("Average Accuracy by Weapon Type")
            df['avg_accuracy'] = pd.to_numeric(df['avg_accuracy'], errors='coerce')
            by_type = df.groupby('weapon_type')['avg_accuracy'].mean().reset_index()
            st.bar_chart(by_type.set_index('weapon_type')['avg_accuracy'])
        else:
            st.info("No accuracy data found for this player.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
st.subheader("Team Knockdown Efficiency")
team_id = st.session_state.get('team_id', 1)
selected_team = st.number_input("Team ID", min_value=1, value=team_id, step=1)

try:
    r = requests.get(f"{API_BASE}/coach/teams/{selected_team}/knockdown-efficiency")
    if r.status_code == 200:
        data = r.json()
        if data:
            st.dataframe(pd.DataFrame(data), use_container_width=True)
        else:
            st.info("No knockdown data found.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")
