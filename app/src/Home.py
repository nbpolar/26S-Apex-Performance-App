import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide', page_title='Apex Performance App')

st.session_state['authenticated'] = False
SideBarLinks(show_home=True)

st.markdown("""
<div style='text-align:center; padding: 2rem 0 1rem 0;'>
    <h1 style='font-size:3rem; font-weight:900; letter-spacing:2px;
               color:#E8373E; margin-bottom:0;'>
        APEX PERFORMANCE APP
    </h1>
    <p style='color:#8B9CB0; font-size:1.1rem; margin-top:0.5rem;'>
        Professional match analytics for Apex Legends
    </p>
</div>
<hr style='border-color:#1A2434; margin-bottom:2rem;'>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:#8B9CB0; margin-bottom:1.5rem;'>Select a persona to continue</h3>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style='background:#1A2434; border:1px solid #2A3F55; border-radius:8px;
                padding:1.5rem; text-align:center; margin-bottom:1rem;'>
        <div style='font-size:2rem;'>&#127919;</div>
        <div style='font-weight:700; font-size:1.1rem; color:#E8EDF2;'>Bill</div>
        <div style='color:#8B9CB0; font-size:0.85rem; margin-top:0.3rem;'>Esports Coach</div>
        <div style='color:#E8373E; font-size:0.75rem; margin-top:0.5rem;'>Team Analysis · Scouting</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Login as Coach", use_container_width=True, type='primary'):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'coach'
        st.session_state['first_name'] = 'Bill'
        st.session_state['team_id'] = 1
        st.switch_page('pages/00_Coach_Home.py')

with col2:
    st.markdown("""
    <div style='background:#1A2434; border:1px solid #2A3F55; border-radius:8px;
                padding:1.5rem; text-align:center; margin-bottom:1rem;'>
        <div style='font-size:2rem;'>&#127918;</div>
        <div style='font-weight:700; font-size:1.1rem; color:#E8EDF2;'>Ryan</div>
        <div style='color:#8B9CB0; font-size:0.85rem; margin-top:0.3rem;'>Casual Player</div>
        <div style='color:#E8373E; font-size:0.75rem; margin-top:0.5rem;'>Stats · Goals · Meta</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Login as Casual", use_container_width=True, type='primary'):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'casual'
        st.session_state['first_name'] = 'Ryan'
        st.session_state['player_id'] = 3
        st.switch_page('pages/10_Casual_Home.py')

with col3:
    st.markdown("""
    <div style='background:#1A2434; border:1px solid #2A3F55; border-radius:8px;
                padding:1.5rem; text-align:center; margin-bottom:1rem;'>
        <div style='font-size:2rem;'>&#127942;</div>
        <div style='font-weight:700; font-size:1.1rem; color:#E8EDF2;'>Daniel</div>
        <div style='color:#8B9CB0; font-size:0.85rem; margin-top:0.3rem;'>Competitive Player</div>
        <div style='color:#E8373E; font-size:0.75rem; margin-top:0.5rem;'>Rankings · Trends · History</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Login as Competitive", use_container_width=True, type='primary'):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'competitive'
        st.session_state['first_name'] = 'Daniel'
        st.session_state['player_id'] = 1
        st.switch_page('pages/20_Competitive_Home.py')

with col4:
    st.markdown("""
    <div style='background:#1A2434; border:1px solid #2A3F55; border-radius:8px;
                padding:1.5rem; text-align:center; margin-bottom:1rem;'>
        <div style='font-size:2rem;'>&#128187;</div>
        <div style='font-weight:700; font-size:1.1rem; color:#E8EDF2;'>James</div>
        <div style='color:#8B9CB0; font-size:0.85rem; margin-top:0.3rem;'>System Administrator</div>
        <div style='color:#E8373E; font-size:0.75rem; margin-top:0.5rem;'>Audit · Archive · Manage</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Login as Admin", use_container_width=True, type='primary'):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'administrator'
        st.session_state['first_name'] = 'James'
        st.switch_page('pages/30_Admin_Home.py')

st.markdown("""
<hr style='border-color:#1A2434; margin-top:2rem;'>
<p style='text-align:center; color:#4A5568; font-size:0.8rem;'>
    Apex Performance App — CS 3200 Spring 2026 — Team APA
</p>
""", unsafe_allow_html=True)
