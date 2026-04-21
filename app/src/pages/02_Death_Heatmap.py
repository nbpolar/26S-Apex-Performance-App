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
    <h1 style='margin:0; color:#E8EDF2;'>Death Heatmap & Team Analysis</h1>
    <p style='color:#8B9CB0; margin:0;'>Identify dangerous zones and analyze team performance</p>
</div>
""", unsafe_allow_html=True)

API_BASE = "http://web-api:4000"
team_id = st.number_input("Team ID", min_value=1, value=st.session_state.get('team_id', 1), step=1)

tab1, tab2, tab3 = st.tabs(["Death Heatmap", "Placement vs Kills", "Damage to Kills"])

with tab1:
    try:
        r = requests.get(f"{API_BASE}/coach/teams/{team_id}/death-heatmap")
        if r.status_code == 200:
            data = r.json()
            if data:
                df = pd.DataFrame(data)
                col1, col2 = st.columns([3, 2])
                with col1:
                    st.markdown("### Death Locations")
                    st.dataframe(df, use_container_width=True, hide_index=True)
                with col2:
                    st.markdown("### Top 10 Hotspots")
                    top = df.sort_values('death_count', ascending=False).head(10)
                    st.bar_chart(top.set_index('location_name')['death_count'])
            else:
                st.info("No death location data found for this team.")
        else:
            st.error(f"Error: {r.status_code}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")

with tab2:
    st.markdown("### Placement vs Kills/Damage")
    st.write("Identifies whether the current meta favors aggressive or passive playstyles.")
    try:
        r = requests.get(f"{API_BASE}/coach/teams/{team_id}/placement-vs-kills")
        if r.status_code == 200:
            data = r.json()
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True, hide_index=True)
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Avg Kills by Placement**")
                    st.bar_chart(df.set_index('placement')['avg_kills'])
                with col2:
                    st.markdown("**Avg Damage by Placement**")
                    st.bar_chart(df.set_index('placement')['avg_damage'])
            else:
                st.info("No placement data found.")
        else:
            st.error(f"Error: {r.status_code}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")

with tab3:
    st.markdown("### Damage to Kills Ratio")
    st.write("Identifies players securing meaningful frags vs those just doing poke damage.")
    try:
        r = requests.get(f"{API_BASE}/coach/teams/{team_id}/damage-to-kills")
        if r.status_code == 200:
            data = r.json()
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df, use_container_width=True, hide_index=True)
            else:
                st.info("No damage data found.")
        else:
            st.error(f"Error: {r.status_code}")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")
