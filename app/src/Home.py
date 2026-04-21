import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide', page_title='Apex Performance App')

st.session_state['authenticated'] = False

SideBarLinks(show_home=True)

logger.info("Loading the Home page of the app")

st.title('Apex Performance App')
st.write('### Welcome! Please select a user to log in as:')
st.write('')

if st.button("Act as Bill — Esports Coach",
             type='primary',
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'coach'
    st.session_state['first_name'] = 'Bill'
    st.session_state['team_id'] = 1
    logger.info("Logging in as Coach persona")
    st.switch_page('pages/00_Coach_Home.py')

if st.button("Act as Ryan — Casual Player",
             type='primary',
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'casual'
    st.session_state['first_name'] = 'Ryan'
    st.session_state['player_id'] = 3
    logger.info("Logging in as Casual Player persona")
    st.switch_page('pages/10_Casual_Home.py')

if st.button("Act as Daniel — Competitive Player",
             type='primary',
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'competitive'
    st.session_state['first_name'] = 'Daniel'
    st.session_state['player_id'] = 1
    logger.info("Logging in as Competitive Player persona")
    st.switch_page('pages/20_Competitive_Home.py')

if st.button("Act as James — System Administrator",
             type='primary',
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'administrator'
    st.session_state['first_name'] = 'James'
    logger.info("Logging in as Admin persona")
    st.switch_page('pages/30_Admin_Home.py')
