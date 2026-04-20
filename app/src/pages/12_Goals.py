import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title("🎯 My Goals")
st.write("Set and track your personal gameplay goals.")

API_BASE = "http://web-api:4000"
player_id = st.session_state.get('player_id', 3)

try:
    r = requests.get(f"{API_BASE}/casual/players/{player_id}/goals")
    if r.status_code == 200:
        data = r.json()
        if data:
            st.subheader("Your Current Goals")
            st.dataframe(pd.DataFrame(data), use_container_width=True)
        else:
            st.info("No goals set yet. Add one below!")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
st.subheader("➕ Add New Goal")
with st.form("add_goal"):
    col1, col2 = st.columns(2)
    with col1:
        goal_type = st.selectbox("Goal Type", [
            "Wins This Month", "Kills This Week",
            "Top 5 Finishes", "Damage Per Match",
            "Accuracy Goal", "Ranked Points Goal"
        ])
        target_value = st.number_input("Target Value", min_value=1, step=1)
    with col2:
        start_date = st.date_input("Start Date")
        end_date   = st.date_input("End Date")
    if st.form_submit_button("Add Goal", type='primary'):
        payload = {
            "goal_type": goal_type,
            "target_value": target_value,
            "start_date": str(start_date),
            "end_date": str(end_date)
        }
        try:
            r = requests.post(f"{API_BASE}/casual/players/{player_id}/goals", json=payload)
            if r.status_code == 201:
                st.success("Goal added!")
                st.rerun()
            else:
                st.error(f"Error: {r.json()}")
        except Exception as e:
            st.error(f"Could not connect to API: {e}")

st.divider()
st.subheader("🗑️ Delete a Goal")
with st.form("delete_goal"):
    goal_id = st.number_input("Goal ID to delete", min_value=1, step=1)
    if st.form_submit_button("Delete Goal", type='primary'):
        try:
            r = requests.delete(f"{API_BASE}/casual/players/{player_id}/goals/{goal_id}")
            if r.status_code == 200:
                st.success("Goal deleted.")
                st.rerun()
            else:
                st.error(f"Error: {r.json()}")
        except Exception as e:
            st.error(f"Could not connect to API: {e}")
