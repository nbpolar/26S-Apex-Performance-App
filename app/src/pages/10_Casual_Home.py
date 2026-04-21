import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}!")
st.write("### What would you like to do today?")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("My Stats", use_container_width=True, type='primary'):
        st.switch_page('pages/11_My_Stats.py')
with col2:
    if st.button("My Goals", use_container_width=True, type='primary'):
        st.switch_page('pages/12_Goals.py')
with col3:
    if st.button("Meta Hub", use_container_width=True, type='primary'):
        st.switch_page('pages/13_Meta_Hub.py')
