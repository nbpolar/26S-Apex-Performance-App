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
    <h1 style='margin:0; color:#E8EDF2;'>Performance Trends</h1>
    <p style='color:#8B9CB0; margin:0;'>Track your improvement over time</p>
</div>
""", unsafe_allow_html=True)

API_BASE = "http://web-api:4000"
player_id = st.session_state.get('player_id', 1)

# Player profile section
st.markdown("### Player Profile")
try:
    r = requests.get(f"{API_BASE}/competitive/players/{player_id}")
    if r.status_code == 200:
        data = r.json()
        if data:
            col1, col2, col3, col4 = st.columns(4)
            col1.markdown(f"""<div style='background:#1A2434; border:1px solid #2A3F55; border-radius:8px; padding:1rem; text-align:center;'>
                <div style='color:#8B9CB0; font-size:0.75rem;'>USERNAME</div>
                <div style='color:#E8EDF2; font-size:1.2rem; font-weight:700;'>{data.get('username','—')}</div></div>""", unsafe_allow_html=True)
            col2.markdown(f"""<div style='background:#1A2434; border:1px solid #2A3F55; border-radius:8px; padding:1rem; text-align:center;'>
                <div style='color:#8B9CB0; font-size:0.75rem;'>RANK</div>
                <div style='color:#E8373E; font-size:1.2rem; font-weight:700;'>{data.get('current_rank','—')}</div></div>""", unsafe_allow_html=True)
            col3.markdown(f"""<div style='background:#1A2434; border:1px solid #2A3F55; border-radius:8px; padding:1rem; text-align:center;'>
                <div style='color:#8B9CB0; font-size:0.75rem;'>RANK POINTS</div>
                <div style='color:#E8373E; font-size:1.2rem; font-weight:700;'>{data.get('current_rank_points','—')}</div></div>""", unsafe_allow_html=True)
            col4.markdown(f"""<div style='background:#1A2434; border:1px solid #2A3F55; border-radius:8px; padding:1rem; text-align:center;'>
                <div style='color:#8B9CB0; font-size:0.75rem;'>REGION</div>
                <div style='color:#E8EDF2; font-size:1.2rem; font-weight:700;'>{data.get('region','—')}</div></div>""", unsafe_allow_html=True)
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()

# Overall stats
st.markdown("### Overall Performance")
try:
    r = requests.get(f"{API_BASE}/competitive/players/{player_id}/performance")
    if r.status_code == 200:
        data = r.json()
        if data:
            col1, col2, col3 = st.columns(3)
            col1.markdown(f"""<div style='background:#1A2434; border:1px solid #2A3F55; border-radius:8px; padding:1.2rem; text-align:center;'>
                <div style='color:#8B9CB0; font-size:0.8rem; text-transform:uppercase;'>Total Kills</div>
                <div style='color:#E8373E; font-size:2rem; font-weight:700;'>{data.get('total_kills', 0)}</div></div>""", unsafe_allow_html=True)
            col2.markdown(f"""<div style='background:#1A2434; border:1px solid #2A3F55; border-radius:8px; padding:1.2rem; text-align:center;'>
                <div style='color:#8B9CB0; font-size:0.8rem; text-transform:uppercase;'>Avg Accuracy</div>
                <div style='color:#E8373E; font-size:2rem; font-weight:700;'>{float(data.get('average_accuracy', 0)):.1f}%</div></div>""", unsafe_allow_html=True)
            col3.markdown(f"""<div style='background:#1A2434; border:1px solid #2A3F55; border-radius:8px; padding:1.2rem; text-align:center;'>
                <div style='color:#8B9CB0; font-size:0.8rem; text-transform:uppercase;'>Win Rate</div>
                <div style='color:#E8373E; font-size:2rem; font-weight:700;'>{float(data.get('win_percentage', 0)):.1f}%</div></div>""", unsafe_allow_html=True)
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.markdown("<br>", unsafe_allow_html=True)

# Performance history charts
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
except Exception as e:
    st.error(f"Could not connect to API: {e}")

st.divider()
st.markdown("### Weapon Performance")
try:
    r = requests.get(f"{API_BASE}/competitive/players/{player_id}/weapon-stats")
    if r.status_code == 200:
        data = r.json()
        if data:
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
        else:
            st.info("No weapon stats found.")
except Exception as e:
    st.error(f"Could not connect to API: {e}")
