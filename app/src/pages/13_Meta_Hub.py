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
    <h1 style='margin:0; color:#E8EDF2;'>Meta Hub</h1>
    <p style='color:#8B9CB0; margin:0;'>Current top performers and upcoming events</p>
</div>
""", unsafe_allow_html=True)

API_BASE = "http://web-api:4000"
player_id = st.session_state.get('player_id', 3)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Top Weapons")
    try:
        r = requests.get(f"{API_BASE}/casual/meta/top-weapons")
        if r.status_code == 200:
            data = r.json()
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True, hide_index=True)
                st.bar_chart(df.set_index('weapon_name')['avg_kd'])
            else:
                st.info("No weapon data available.")
        else:
            st.error(f"Error: {r.status_code}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")

with col2:
    st.markdown("### Top Legends")
    try:
        r = requests.get(f"{API_BASE}/casual/meta/top-legends")
        if r.status_code == 200:
            data = r.json()
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True, hide_index=True)
                st.bar_chart(df.set_index('legend_name')['avg_win_rate'])
            else:
                st.info("No legend data available.")
        else:
            st.error(f"Error: {r.status_code}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")

st.divider()
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Upcoming Game Events")
    try:
        r = requests.get(f"{API_BASE}/casual/events")
        if r.status_code == 200:
            data = r.json()
            if data:
                st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
            else:
                st.info("No upcoming events.")
        else:
            st.error(f"Error: {r.status_code}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")

with col2:
    st.markdown("### Notifications")
    try:
        r = requests.get(f"{API_BASE}/casual/players/{player_id}/notifications")
        if r.status_code == 200:
            data = r.json()
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True, hide_index=True)

                st.markdown("##### Mark Notification as Read")
                with st.form("mark_read"):
                    notif_id = st.number_input("Notification ID", min_value=1, step=1)
                    if st.form_submit_button("Mark as Read"):
                        try:
                            r2 = requests.put(
                                f"{API_BASE}/casual/players/{player_id}/notifications/{notif_id}",
                                json={"read_status": True}
                            )
                            if r2.status_code == 200:
                                st.success("Marked as read!")
                                st.rerun()
                            else:
                                st.error(f"Error: {r2.json()}")
                        except Exception as e:
                            st.error(f"Could not connect to API: {e}")
            else:
                st.info("No notifications.")
        else:
            st.error(f"Error: {r.status_code}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")
