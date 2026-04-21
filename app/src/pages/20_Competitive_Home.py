import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}! 🏆")
st.write("### Ready to climb the ranks? Let's analyze your performance.")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Leaderboard", use_container_width=True, type='primary'):
        st.switch_page('pages/21_Leaderboard.py')
with col2:
    if st.button("Match History", use_container_width=True, type='primary'):
        st.switch_page('pages/22_Match_History.py')
with col3:
    if st.button("Performance Trends", use_container_width=True, type='primary'):
        st.switch_page('pages/23_Performance_Trends.py')
