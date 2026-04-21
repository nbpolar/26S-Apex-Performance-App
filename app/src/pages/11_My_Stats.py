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
    <h1 style='margin:0; color:#E8EDF2;'>My Stats</h1>
    <p style='color:#8B9CB0; margin:0;'>Your personal performance records</p>
</div>
""", unsafe_allow_html=True)

API_BASE = "http://web-api:4000"
player_id = st.session_state.get('player_id', 3)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Tracked Stats")
    try:
        r = requests.get(f"{API_BASE}/casual/players/{player_id}/stats")
        if r.status_code == 200:
            data = r.json()
            if data:
                df = pd.DataFrame(data)
                visible = df[df['is_visible'] == 1] if 'is_visible' in df.columns else df
                st.dataframe(visible, use_container_width=True, hide_index=True)
            else:
                st.info("No stats tracked yet.")
        else:
            st.error(f"Error: {r.status_code}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### Hide a Stat")
        with st.form("hide_stat"):
            stat_id = st.number_input("Stat Entry ID", min_value=1, step=1)
            if st.form_submit_button("Hide", type='primary'):
                try:
                    r = requests.put(f"{API_BASE}/casual/players/stats/{stat_id}/hide")
                    if r.status_code == 200:
                        st.success("Stat hidden!")
                        st.rerun()
                    else:
                        st.error(f"Error: {r.json()}")
                except Exception as e:
                    st.error(f"Could not connect to API: {e}")

    with col_b:
        st.markdown("### Delete a Stat")
        with st.form("delete_stat"):
            stat_id = st.number_input("Stat Entry ID to delete", min_value=1, step=1)
            if st.form_submit_button("Delete", type='primary'):
                try:
                    r = requests.delete(f"{API_BASE}/casual/players/{player_id}/stats/{stat_id}")
                    if r.status_code == 200:
                        st.success("Stat deleted!")
                        st.rerun()
                    else:
                        st.error(f"Error: {r.json()}")
                except Exception as e:
                    st.error(f"Could not connect to API: {e}")

with col2:
    st.markdown("### Best Legends & Weapons")
    try:
        r = requests.get(f"{API_BASE}/casual/players/{player_id}/best-legends-weapons")
        if r.status_code == 200:
            data = r.json()
            if data:
                st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
            else:
                st.info("No legend/weapon data found.")
        else:
            st.error(f"Error: {r.status_code}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")

    st.markdown("### Legend Performance")
    try:
        r = requests.get(f"{API_BASE}/casual/players/{player_id}/legend-performance")
        if r.status_code == 200:
            data = r.json()
            if data:
                st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
            else:
                st.info("No legend performance data found.")
        else:
            st.error(f"Error: {r.status_code}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")
