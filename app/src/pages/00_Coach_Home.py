import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title(f"Welcome, Coach {st.session_state['first_name']}! 🎯")
st.write("### What would you like to analyze today?")
st.write("Use the sidebar or buttons below to navigate.")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🧩 Team Compositions", use_container_width=True, type='primary'):
        st.switch_page('pages/01_Team_Compositions.py')
with col2:
    if st.button("🗺️ Death Heatmap", use_container_width=True, type='primary'):
        st.switch_page('pages/02_Death_Heatmap.py')
with col3:
    if st.button("🎯 Player Accuracy", use_container_width=True, type='primary'):
        st.switch_page('pages/03_Player_Accuracy.py')
