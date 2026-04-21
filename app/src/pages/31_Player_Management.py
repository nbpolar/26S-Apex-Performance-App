import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title("👤 Player Management")
st.write("Add, update, and remove players from the system.")

API_BASE = "http://web-api:4000"

st.subheader("All Players")
try:
    r = requests.get(f"{API_BASE}/admin/players")
    if r.status_code == 200:
        data = r.json()
        if data:
            st.dataframe(pd.DataFrame(data), use_container_width=True)
        else:
            st.info("No players found.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
st.subheader("➕ Add New Player")
with st.form("add_player"):
    col1, col2 = st.columns(2)
    with col1:
        username   = st.text_input("Username")
        region     = st.selectbox("Region", ["NA", "EU", "APAC", "SA", "ME"])
        join_date  = st.date_input("Join Date")
    with col2:
        current_rank = st.selectbox("Rank", ["Bronze","Silver","Gold","Platinum","Diamond","Master","Predator"])
        team_id      = st.number_input("Team ID", min_value=1, step=1)
        rank_tier_id = st.number_input("Rank Tier ID", min_value=1, max_value=7, step=1)
    if st.form_submit_button("Add Player", type='primary'):
        payload = {
            "username": username, "region": region,
            "join_date": str(join_date), "current_rank": current_rank,
            "team_id": team_id, "rank_tier_id": rank_tier_id
        }
        try:
            r = requests.post(f"{API_BASE}/admin/players", json=payload)
            if r.status_code == 201:
                st.success(f"Player '{username}' added!")
                st.rerun()
            else:
                st.error(f"Error: {r.json()}")
        except Exception as e:
            st.error(f"Could not connect to API: {e}")

st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("✏️ Update Player")
    with st.form("update_player"):
        pid          = st.number_input("Player ID", min_value=1, step=1)
        new_rank     = st.selectbox("New Rank", ["Bronze","Silver","Gold","Platinum","Diamond","Master","Predator"])
        new_points   = st.number_input("New Rank Points", min_value=0, step=1)
        if st.form_submit_button("Update Player"):
            try:
                r = requests.put(f"{API_BASE}/admin/players/{pid}",
                                 json={"current_rank": new_rank, "current_rank_points": new_points})
                if r.status_code == 200:
                    st.success("Player updated!")
                    st.rerun()
                else:
                    st.error(f"Error: {r.json()}")
            except Exception as e:
                st.error(f"Could not connect to API: {e}")

with col2:
    st.subheader("🗑️ Delete Player")
    with st.form("delete_player"):
        pid = st.number_input("Player ID to delete", min_value=1, step=1)
        if st.form_submit_button("Delete Player", type='primary'):
            try:
                r = requests.delete(f"{API_BASE}/admin/players/{pid}")
                if r.status_code == 200:
                    st.success("Player deleted.")
                    st.rerun()
                else:
                    st.error(f"Error: {r.json()}")
            except Exception as e:
                st.error(f"Could not connect to API: {e}")
