import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title("🗄️ Season Archive")
st.write("Archive old season data to keep current season queries fast.")

API_BASE = "http://web-api:4000"

st.subheader("📊 System Reports")
try:
    r = requests.get(f"{API_BASE}/admin/reports")
    if r.status_code == 200:
        data = r.json()
        if data:
            st.dataframe(pd.DataFrame(data), use_container_width=True)
        else:
            st.info("No report data available.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
st.subheader("📦 Archive a Season")
with st.form("archive_season"):
    season = st.selectbox("Season to Archive",
                          ["Season 18", "Season 19", "Season 20", "Season 21"])
    st.warning(f"This will archive all match data for **{season}**. This cannot be undone.")
    if st.form_submit_button("Archive Season", type='primary'):
        try:
            r = requests.post(f"{API_BASE}/admin/archive-season",
                              json={"season_name": season})
            if r.status_code == 201:
                result = r.json()
                st.success(f"Successfully archived {result.get('matches_archived', 0)} matches from {season}.")
            else:
                st.error(f"Error: {r.json()}")
        except Exception as e:
            st.error(f"Could not connect to API: {e}")

st.divider()
st.subheader("🔌 Data Sources")
try:
    r = requests.get(f"{API_BASE}/admin/data-sources")
    if r.status_code == 200:
        data = r.json()
        if data:
            st.dataframe(pd.DataFrame(data), use_container_width=True)
        else:
            st.info("No data sources found.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.subheader("➕ Add Data Source")
with st.form("add_source"):
    col1, col2 = st.columns(2)
    with col1:
        source_name = st.text_input("Source Name")
        source_type = st.selectbox("Type", ["API", "CSV", "Webhook", "Manual"])
    with col2:
        api_endpoint = st.text_input("API Endpoint (optional)")
        status       = st.selectbox("Status", ["active", "inactive", "pending"])
    if st.form_submit_button("Add Source", type='primary'):
        payload = {
            "source_name": source_name,
            "source_type": source_type,
            "api_endpoint": api_endpoint,
            "status": status
        }
        try:
            r = requests.post(f"{API_BASE}/admin/data-sources", json=payload)
            if r.status_code == 201:
                st.success(f"Data source '{source_name}' added!")
                st.rerun()
            else:
                st.error(f"Error: {r.json()}")
        except Exception as e:
            st.error(f"Could not connect to API: {e}")
