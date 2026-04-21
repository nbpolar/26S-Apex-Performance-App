import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')
SideBarLinks()

st.title("Death Heatmap")
st.write("View where players are dying most frequently on each map.")

API_BASE = "http://web-api:4000"

team_id = st.session_state.get('team_id', 1)
selected_team = st.number_input("Team ID", min_value=1, value=team_id, step=1)

try:
    r = requests.get(f"{API_BASE}/coach/teams/{selected_team}/death-heatmap")
    if r.status_code == 200:
        data = r.json()
        if data:
            df = pd.DataFrame(data)
            st.subheader(f"Death Locations for Team {selected_team}")
            st.dataframe(df, use_container_width=True)

            st.subheader("Top 10 Death Locations")
            top = df.sort_values('death_count', ascending=False).head(10)
            st.bar_chart(top.set_index('location_name')['death_count'])
        else:
            st.info("No death location data found for this team.")
    else:
        st.error(f"Error: {r.status_code}")
except Exception as e:
    st.error(f"Could not connect to API: {e}")
