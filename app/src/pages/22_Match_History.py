import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title("📋 Match History")
st.write("View and manage your match history. Include or exclude matches from your analysis.")

API_BASE = "http://web-api:4000"
player_id = st.session_state.get('player_id', 1)

try:
    r = requests.get(f"{API_BASE}/competitive/players/{player_id}/match-history")
    if r.status_code == 200:
        data = r.json()
        if data:
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No match history found.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("❌ Exclude Match from Analysis")
    with st.form("exclude_form"):
        perf_id = st.number_input("Performance ID to exclude", min_value=1, step=1)
        if st.form_submit_button("Exclude Match", type='primary'):
            try:
                r = requests.put(
                    f"{API_BASE}/competitive/players/{player_id}/matches/{perf_id}/exclude"
                )
                if r.status_code == 200:
                    st.success("Match excluded from analysis.")
                    st.rerun()
                else:
                    st.error(f"Error: {r.json()}")
            except Exception as e:
                st.error(f"Could not connect to API: {e}")

with col2:
    st.subheader("✅ Re-include Match in Analysis")
    with st.form("include_form"):
        perf_id = st.number_input("Performance ID to include", min_value=1, step=1)
        if st.form_submit_button("Include Match", type='primary'):
            try:
                r = requests.put(
                    f"{API_BASE}/competitive/players/{player_id}/matches/{perf_id}/include"
                )
                if r.status_code == 200:
                    st.success("Match re-included in analysis.")
                    st.rerun()
                else:
                    st.error(f"Error: {r.json()}")
            except Exception as e:
                st.error(f"Could not connect to API: {e}")
