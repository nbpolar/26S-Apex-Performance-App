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
    <h1 style='margin:0; color:#E8EDF2;'>Team Compositions</h1>
    <p style='color:#8B9CB0; margin:0;'>Most used legend combinations in competitive play</p>
</div>
""", unsafe_allow_html=True)

API_BASE = "http://web-api:4000"

st.markdown("### Top Compositions")
try:
    r = requests.get(f"{API_BASE}/coach/team-compositions")
    if r.status_code == 200:
        data = r.json()
        if data:
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
        else:
            st.info("No team compositions found.")
    else:
        st.error(f"Error fetching data: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Add Composition")
    with st.form("add_comp_form"):
        match_id = st.number_input("Match ID", min_value=1, step=1)
        team_id  = st.number_input("Team ID",  min_value=1, step=1)
        legend_1 = st.number_input("Legend 1 ID", min_value=1, max_value=27, step=1)
        legend_2 = st.number_input("Legend 2 ID", min_value=1, max_value=27, step=1)
        legend_3 = st.number_input("Legend 3 ID", min_value=1, max_value=27, step=1)
        if st.form_submit_button("Add", type='primary'):
            payload = {"match_id": match_id, "team_id": team_id,
                       "legend_1": legend_1, "legend_2": legend_2, "legend_3": legend_3}
            try:
                r = requests.post(f"{API_BASE}/coach/team-compositions", json=payload)
                if r.status_code == 201:
                    st.success("Composition added!")
                    st.rerun()
                else:
                    st.error(f"Error: {r.json()}")
            except Exception as e:
                st.error(f"Could not connect to API: {e}")

with col2:
    st.markdown("### Update Composition")
    with st.form("update_comp_form"):
        comp_id  = st.number_input("Composition ID", min_value=1, step=1)
        legend_1 = st.number_input("New Legend 1 ID", min_value=1, max_value=27, step=1)
        legend_2 = st.number_input("New Legend 2 ID", min_value=1, max_value=27, step=1)
        legend_3 = st.number_input("New Legend 3 ID", min_value=1, max_value=27, step=1)
        if st.form_submit_button("Update", type='primary'):
            payload = {"legend_1": legend_1, "legend_2": legend_2, "legend_3": legend_3}
            try:
                r = requests.put(f"{API_BASE}/coach/team-compositions/{comp_id}", json=payload)
                if r.status_code == 200:
                    st.success("Composition updated!")
                    st.rerun()
                else:
                    st.error(f"Error: {r.json()}")
            except Exception as e:
                st.error(f"Could not connect to API: {e}")

with col3:
    st.markdown("### Delete Composition")
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
