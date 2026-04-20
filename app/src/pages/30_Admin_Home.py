import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}! 🖥️")
st.write("### System Administration Dashboard")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("👤 Player Management", use_container_width=True, type='primary'):
        st.switch_page('pages/31_Player_Management.py')
with col2:
    if st.button("🚩 Audit Flags", use_container_width=True, type='primary'):
        st.switch_page('pages/32_Audit_Flags.py')
with col3:
    if st.button("🗄️ Season Archive", use_container_width=True, type='primary'):
        st.switch_page('pages/33_Season_Archive.py')
