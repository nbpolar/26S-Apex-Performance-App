import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title("🧩 Team Compositions")
st.write("View the most used team compositions in competitive play.")

API_BASE = "http://web-api:4000"

# ---- View compositions ----
st.subheader("Top Team Compositions")
try:
    r = requests.get(f"{API_BASE}/coach/team-compositions")
    if r.status_code == 200:
        data = r.json()
        if data:
            st.dataframe(data, use_container_width=True)
        else:
            st.info("No team compositions found.")
    else:
        st.error(f"Error fetching data: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()

# ---- Add a new composition ----
st.subheader("➕ Add New Team Composition")
with st.form("add_comp_form"):
    col1, col2 = st.columns(2)
    with col1:
        match_id = st.number_input("Match ID", min_value=1, step=1)
        team_id  = st.number_input("Team ID",  min_value=1, step=1)
    with col2:
        legend_1 = st.number_input("Legend 1 ID", min_value=1, max_value=27, step=1)
        legend_2 = st.number_input("Legend 2 ID", min_value=1, max_value=27, step=1)
        legend_3 = st.number_input("Legend 3 ID", min_value=1, max_value=27, step=1)
    submitted = st.form_submit_button("Add Composition")
    if submitted:
        payload = {"match_id": match_id, "team_id": team_id,
                   "legend_1": legend_1, "legend_2": legend_2, "legend_3": legend_3}
        try:
            r = requests.post(f"{API_BASE}/coach/team-compositions", json=payload)
            if r.status_code == 201:
                st.success("Team composition added successfully!")
                st.rerun()
            else:
                st.error(f"Error: {r.json()}")
        except Exception as e:
            st.error(f"Could not connect to API: {e}")

st.divider()

# ---- Delete a composition ----
st.subheader("🗑️ Delete Team Composition")
with st.form("delete_comp_form"):
    comp_id = st.number_input("Composition ID to delete", min_value=1, step=1)
    if st.form_submit_button("Delete", type='primary'):
        try:
            r = requests.delete(f"{API_BASE}/coach/team-compositions/{comp_id}")
            if r.status_code == 200:
                st.success("Composition deleted.")
                st.rerun()
            else:
                st.error(f"Error: {r.json()}")
        except Exception as e:
            st.error(f"Could not connect to API: {e}")
