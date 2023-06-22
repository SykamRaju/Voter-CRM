import streamlit as st
from API import API
import extra_streamlit_components as stx
from streamlit_option_menu import option_menu
import toml
import os

from Views.AddState import AddState
from Views.DisplayStates import DisplayStates
from Views.EditState import EditState
from Views.DeleteState import DeleteState

from Views.AddDistrict import AddDistrict
from Views.DisplayDistricts import DisplayDistricts
from Views.EditDistrict import EditDistrict
from Views.DeleteDistrict import DeleteDistrict

from Views.AddConstituency import AddConstituency
from Views.DisplayConstituencies import DisplayConstituencies
from Views.EditConstituency import EditConstituency
from Views.DeleteConstituency import DeleteConstituency

from Views.DisplayParties import DisplayParties
from Views.AddParty import AddParty
from Views.DeleteParty import DeleteParty

from Views.ChangePassword import ChangePassword
from Views.RegisterAgent import RegisterAgent
from Views.Login import Login

from Views.VotersList import DisplayVoters

config = toml.load(".streamlit/config.toml")
api_base_url = "http://{}:8000/".format(
    os.getenv('SERVER_URL', '127.0.0.1')
)

st.markdown("""
        <style>
            .main .block-container {
                margin-top: -4rem;
            }

            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
        """, unsafe_allow_html=True)

cookie_manager = stx.CookieManager()
cookies = cookie_manager.get_all()
authentication_token = cookies.get(
    "token") if type(cookies) == dict else cookies

api = API(api_base_url, authentication_token)


def manage_login(login_details):
    token = api.login(login_details)
    cookie_manager.set("token", token)
    return token is not None


def manage_signup(signup_details):
    return api.signup(signup_details)


def manage_changepassword(password_details):
    return api.change_password(password_details)


def register_agent(agent_details):
    return api.signup(agent_details)


if api.is_logged_in():

    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["States", "Districts", "Constituencies",
                     "Political Parties", "Display Voters List", "Register Agent", "Change Password", "Log Out"],
            icons=['patch-check', 'patch-check', 'patch-check', 'patch-check',
                   'patch-check', 'person-plus', 'shuffle', 'box-arrow-left'],
            menu_icon="app-indicator",
            styles={
                "container": {"padding": "5px !important"},
                "icon": {"font-size": "24px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                             "--hover-color": "rgba(128,128,128,0.25)"}
            }
        )

    ###############################################################
    #
    #   L O G O U T
    #
    ###############################################################
    if selected == "Log Out":
        if api.admin_logout():
            st.success("Logging out!")
            st.session_state.runpage = Login(manage_login, manage_signup)
            st.experimental_rerun()
        else:
            st.error("An error occurred during logout!")

    ###############################################################
    #
    #   C H A N G E  P A S S W O R D
    #
    ###############################################################

    if selected == "Change Password":
        ChangePassword(manage_changepassword)

    ###############################################################
    #
    #   S T A T E S
    #
    ###############################################################
    if selected == "States":
        tab1, tab2, tab3, tab4 = st.tabs(
            ["View States", "Add State", "Edit State", "Delete State"])

        with tab1:
            # List States
            DisplayStates(api.get_states)

        with tab2:
            # Add a State
            AddState(api.add_state)

        with tab3:
            # Edit State
            EditState(api.get_states, api.edit_state)

        with tab4:
            # Delete State
            DeleteState(api.get_states, api.delete_state)

    ###############################################################
    #
    #   D I S T R I C T S
    #
    ###############################################################
    if selected == "Districts":
        tab1, tab2, tab3, tab4 = st.tabs(
            ["View Districts", "Add District", "Edit District", "Delete District"])

        with tab1:
            # List Districts
            DisplayDistricts(api.get_states,api.get_districts_for_given_state)

        with tab2:
            # Add a District
            AddDistrict(api.get_states, api.add_district)

        with tab3:
            # Edit District
            EditDistrict(api.get_states,api.get_districts_for_given_state, api.edit_district)

        with tab4:
            # Delete District
            DeleteDistrict(api.get_states,api.get_districts_for_given_state, api.delete_district)

    ###############################################################
    #
    #   C O N S T I T U E N C I E S
    #
    ###############################################################
    if selected == "Constituencies":
        tab1, tab2, tab3, tab4 = st.tabs(
            ["View Constituencies", "Add Constituency", "Edit Constituency", "Delete Constituency"])

        with tab1:
            # List Constituencies
            # DisplayConstituencies(api.get_constituencies)
            DisplayConstituencies(api.get_states,api.get_districts_for_given_state,api.get_constituencies_for_given_district)
            


        with tab2:
            # Add a Constituency
            AddConstituency(api.get_states,api.get_districts_for_given_state,api.add_constituency)

        with tab3:
            # Edit Constituency
            st.write('tab 3')
            # EditConstituency(api.get_constituencies_for_given_district, api.edit_constituency)

        with tab4:
            # Delete Constituency
            st.write('tab 4')
            # DeleteConstituency(api.get_constituencies_for_given_district, api.delete_constituency)

    ###############################################################
    #
    #   D I S P L A Y   V O T E R S   L I S T
    #
    ###############################################################
    if selected == "Display Voters List":
        DisplayVoters(api.get_voters)

    ###############################################################
    #
    #   R E G I S T E R   A N   A G E N T
    #
    ###############################################################
    if selected == "Register Agent":
        RegisterAgent(register_agent)

    ###############################################################
    #
    #   P O L I T I C A L  P A R T I E S
    #
    ###############################################################
    if selected == "Political Parties":
        tab1, tab2, tab3 = st.tabs(
            ["View Political Parties", "Add Political Party", "Delete Political Party"])

        with tab1:
            # List Political Parties
            DisplayParties(api.get_parties)

        with tab2:
            # Add a Political Party
            AddParty(api.add_party,api.get_states)

        with tab3:
            # Delete a Political Party
            DeleteParty(api.get_parties, api.delete_party)


elif api.is_agent_logged_in():
    with st.sidebar:
        agent_selected = option_menu(
            menu_title="Main Menu",
            options=["Upload Voter Details", "Display Voters List", "Change Password", "Log Out"],
            icons=['file-arrow-up', 'patch-check', 'shuffle', 'box-arrow-left'],
            menu_icon="app-indicator",
            styles={
                "container": {"padding": "5px !important"},
                "icon": {"font-size": "24px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                             "--hover-color": "rgba(128,128,128,0.25)"}
            }
        )

    ###############################################################
    #
    #   L O G O U T
    #
    ###############################################################
    if agent_selected == "Log Out":
        if api.agent_logout():
            st.success("Logging out!")
            st.session_state.runpage = Login(manage_login, manage_signup)
            st.experimental_rerun()
        else:
            st.error("An error occurred during logout!")

    ###############################################################
    #
    #   C H A N G E  P A S S W O R D
    #
    ###############################################################

    if agent_selected == "Change Password":
        ChangePassword(manage_changepassword)

    ###############################################################
    #
    #   D I S P L A Y  V O T E R S  L I S T
    #
    ###############################################################
    if agent_selected == "Display Voters List":
        DisplayVoters(api.get_voters)

else:
    Login(manage_login, manage_signup)
