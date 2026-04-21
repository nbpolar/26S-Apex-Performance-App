import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title("📈 Performance Trends")
st.write("Track your performance over time to see whether you're improving.")

API_BASE = "http://web-api:4000"
player_id = st.session_state.get('player_id', 1)

st.subheader("Overall Performance Summary")
try:
    r = requests.get(f"{API_BASE}/competitive/players/{player_id}/performance")
    if r.status_code == 200:
        data = r.json()
        if data:
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Kills", data.get('total_kills', 'N/A'))
            col2.metric("Avg Accuracy", f"{data.get('average_accuracy', 0):.1f}%")
            col3.metric("Win Rate", f"{data.get('win_percentage', 0):.1f}%")
        else:
            st.info("No performance data found.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
st.subheader("Performance Over Time")
try:
    r = requests.get(f"{API_BASE}/competitive/players/{player_id}/performance-history")
    if r.status_code == 200:
        data = r.json()
        if data:
            df = pd.DataFrame(data)
            df['match_date'] = pd.to_datetime(df['match_date'])
            df = df.sort_values('match_date')

            tab1, tab2, tab3 = st.tabs(["Kills Over Time", "Damage Over Time", "Accuracy Over Time"])
            with tab1:
                st.line_chart(df.set_index('match_date')['kills'])
            with tab2:
                st.line_chart(df.set_index('match_date')['damage'])
            with tab3:
                st.line_chart(df.set_index('match_date')['accuracy_pct'])
        else:
            st.info("No match history to show trends.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
st.subheader("🔫 Weapon Performance")
try:
    r = requests.get(f"{API_BASE}/competitive/players/{player_id}/weapon-stats")
    if r.status_code == 200:
        data = r.json()
        if data:
            st.dataframe(pd.DataFrame(data), use_container_width=True)
        else:
            st.info("No weapon stats found.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")
