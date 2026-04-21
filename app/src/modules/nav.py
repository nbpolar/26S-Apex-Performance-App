import streamlit as st


def home_nav():
    st.sidebar.page_link("Home.py", label="Home")


#Coach
def coach_home_nav():
    st.sidebar.page_link("pages/00_Coach_Home.py", label="Coach Home")

def team_compositions_nav():
    st.sidebar.page_link("pages/01_Team_Compositions.py", label="Team Compositions")

def death_heatmap_nav():
    st.sidebar.page_link("pages/02_Death_Heatmap.py", label="Death Heatmap")

def player_accuracy_nav():
    st.sidebar.page_link("pages/03_Player_Accuracy.py", label="Player Accuracy")


#Casual
def casual_home_nav():
    st.sidebar.page_link("pages/10_Casual_Home.py", label="Casual Home")

def my_stats_nav():
    st.sidebar.page_link("pages/11_My_Stats.py", label="My Stats")

def goals_nav():
    st.sidebar.page_link("pages/12_Goals.py", label="My Goals")

def meta_hub_nav():
    st.sidebar.page_link("pages/13_Meta_Hub.py", label="Meta Hub")


#Competitive
def competitive_home_nav():
    st.sidebar.page_link("pages/20_Competitive_Home.py", label="Competitive Home")

def leaderboard_nav():
    st.sidebar.page_link("pages/21_Leaderboard.py", label="Leaderboard")

def match_history_nav():
    st.sidebar.page_link("pages/22_Match_History.py", label="Match History")

def performance_trends_nav():
    st.sidebar.page_link("pages/23_Performance_Trends.py", label="Performance Trends")


#Admin
def admin_home_nav():
    st.sidebar.page_link("pages/30_Admin_Home.py", label="Admin Home")

def player_management_nav():
    st.sidebar.page_link("pages/31_Player_Management.py", label="Player Management")

def audit_flags_nav():
    st.sidebar.page_link("pages/32_Audit_Flags.py", label="Audit Flags")

def season_archive_nav():
    st.sidebar.page_link("pages/33_Season_Archive.py", label="Season Archive")


# Side Bar
def SideBarLinks(show_home=False):
    st.sidebar.image("assets/logo.png", width=150)

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        home_nav()

    if st.session_state["authenticated"]:

        if st.session_state["role"] == "coach":
            coach_home_nav()
            team_compositions_nav()
            death_heatmap_nav()
            player_accuracy_nav()

        if st.session_state["role"] == "casual":
            casual_home_nav()
            my_stats_nav()
            goals_nav()
            meta_hub_nav()

        if st.session_state["role"] == "competitive":
            competitive_home_nav()
            leaderboard_nav()
            match_history_nav()
            performance_trends_nav()

        if st.session_state["role"] == "administrator":
            admin_home_nav()
            player_management_nav()
            audit_flags_nav()
            season_archive_nav()

    if st.session_state["authenticated"]:
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
