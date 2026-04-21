import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.markdown("""
<div style='border-left:4px solid #E8373E; padding-left:1rem; margin-bottom:1.5rem;'>
    <h1 style='margin:0; color:#E8EDF2;'>My Goals</h1>
    <p style='color:#8B9CB0; margin:0;'>Set and track your personal gameplay goals</p>
</div>
""", unsafe_allow_html=True)

API_BASE = "http://web-api:4000"
player_id = st.session_state.get('player_id', 3)

st.markdown("### Current Goals")
try:
    r = requests.get(f"{API_BASE}/casual/players/{player_id}/goals")
    if r.status_code == 200:
        data = r.json()
        if data:
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
        else:
            st.info("No goals set yet.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Add Goal")
    with st.form("add_goal"):
        goal_type    = st.selectbox("Goal Type", ["Wins This Month","Kills This Week",
                                                   "Top 5 Finishes","Damage Per Match",
                                                   "Accuracy Goal","Ranked Points Goal"])
        target_value = st.number_input("Target Value", min_value=1, step=1)
        start_date   = st.date_input("Start Date")
        end_date     = st.date_input("End Date")
        if st.form_submit_button("Add Goal", type='primary'):
            payload = {"goal_type": goal_type, "target_value": target_value,
                       "start_date": str(start_date), "end_date": str(end_date)}
            try:
                r = requests.post(f"{API_BASE}/casual/players/{player_id}/goals", json=payload)
                if r.status_code == 201:
                    st.success("Goal added!")
                    st.rerun()
                else:
                    st.error(f"Error: {r.json()}")
            except Exception as e:
                st.error(f"Could not connect to API: {e}")

with col2:
    st.markdown("### Update Goal Progress")
    with st.form("update_goal"):
        goal_id       = st.number_input("Goal ID", min_value=1, step=1)
        current_value = st.number_input("Current Progress", min_value=0, step=1)
        goal_status   = st.selectbox("Status", ["In Progress","Completed","Failed"])
        if st.form_submit_button("Update Goal", type='primary'):
            try:
                r = requests.put(f"{API_BASE}/casual/players/{player_id}/goals/{goal_id}",
                                 json={"current_value": current_value, "goal_status": goal_status})
                if r.status_code == 200:
                    st.success("Goal updated!")
                    st.rerun()
                else:
                    st.error(f"Error: {r.json()}")
            except Exception as e:
                st.error(f"Could not connect to API: {e}")

with col3:
    st.markdown("### Delete Goal")
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
