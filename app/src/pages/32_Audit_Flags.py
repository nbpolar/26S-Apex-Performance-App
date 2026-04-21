import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title("Audit Flags")
st.write("Review flagged accounts with impossible stats for potential cheating.")

API_BASE = "http://web-api:4000"

status_filter = st.selectbox("Filter by Status", ["All", "Pending", "Reviewed", "Cleared", "Banned"])
params = {} if status_filter == "All" else {"status": status_filter}

try:
    r = requests.get(f"{API_BASE}/admin/audit-flags", params=params)
    if r.status_code == 200:
        data = r.json()
        if data:
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
            st.write(f"**Total flagged accounts:** {len(df)}")
        else:
            st.info("No flagged accounts found.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
st.subheader("Update Flag Status")
with st.form("update_flag"):
    col1, col2 = st.columns(2)
    with col1:
        flag_id = st.number_input("Audit Flag ID", min_value=1, step=1)
    with col2:
        new_status = st.selectbox("New Status", ["Pending", "Reviewed", "Cleared", "Banned"])
    if st.form_submit_button("Update Flag", type='primary'):
        try:
            r = requests.put(f"{API_BASE}/admin/audit-flags/{flag_id}",
                             json={"review_status": new_status})
            if r.status_code == 200:
                st.success(f"Flag {flag_id} updated to '{new_status}'.")
                st.rerun()
            else:
                st.error(f"Error: {r.json()}")
        except Exception as e:
            st.error(f"Could not connect to API: {e}")
