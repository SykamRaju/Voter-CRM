import streamlit as st

from Views.AddState import AddState
from Views.DisplayStates import DisplayStates
from Views.EditState import EditState
from Views.DeleteState import DeleteState

from Views.AddDistrict import AddDistrict
from Views.DisplayDistricts import DisplayDistricts
from Views import EditDistrict
from Views.DeleteDistrict import DeleteDistrict

from Views.AddConstituency import AddConstituency
from Views.DisplayConstituencies import DisplayConstituencies
from Views import EditConstituency
from Views.DeleteConstituency import DeleteConstituency



from Views.Login import Login
from API import API
import extra_streamlit_components as stx
import json
from streamlit_option_menu import option_menu
import toml

config = toml.load(".streamlit/config.toml")
api_base_url = config['api_url']['api_base_url']


cookie_manager = stx.CookieManager()
cookies = cookie_manager.get_all()
authentication_token = cookies.get("token") if type(cookies) == dict else cookies
# authentication_token = ''

api = API(api_base_url, authentication_token)


def manage_login(username, password):
    token = api.login(username, password)
    cookie_manager.set("token", token)
    return token is not None




if api.is_logged_in():

    # with st.sidebar:
    #     selected = option_menu(
    #         menu_title="Actions",
    #         options=["Log out"]
    #     )


    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["States","Districts","Constituencies","Parites"]
        )
    
###############################################################
#
#   S T A T E S
#
###############################################################
    if selected == "States":
        tab1, tab2, tab3, tab4 = st.tabs(["View States", "Add State", "Edit State","Delete State"])

        with tab1:
            # List States
            DisplayStates(api.get_states)

        with tab2:
            # Add a State
            AddState(api.add_state)

        with tab3:
            # Edit State
            EditState(api.get_states,api.edit_state)

        with tab4:
            # Delete State
            DeleteState(api.get_states,api.delete_state)    

    
###############################################################
#
#   D I S T R I C T S
#
###############################################################
    if selected == "Districts":
        tab1, tab2, tab3, tab4 = st.tabs(["View Districts", "Add District", "Edit District","Delete District"])

        with tab1:
            # List Districts
            DisplayDistricts(api.get_districts)

        with tab2:
            # Add a District
            AddDistrict(api.get_states,api.add_district)

        with tab3:
            # Edit District
            EditDistrict(api.get_districts,api.edit_district)

        with tab4:
            # Delete District
            DeleteDistrict(api.get_districts,api.delete_district)    

    
###############################################################
#
#   C O N S T I T U E N C I E S
#
###############################################################
    if selected == "Constituencies":
        tab1, tab2, tab3, tab4 = st.tabs(["View Constituencies", "Add Constituency", "Edit Constituency","Delete Constituency"])

        with tab1:
            # List Constituencies
            DisplayConstituencies(api.get_constituencies)

        with tab2:
            # Add a Constituency
            AddConstituency(api.get_districts,api.add_constituency)

        with tab3:
            # Edit Constituency
            EditConstituency(api.get_constituencies,api.edit_constituency)

        with tab4:
            # Delete Constituency
            DeleteConstituency(api.get_constituencies,api.delete_constituency)    

        


    # if selected == "Districts":
    #     DisplayStates(api.get_districts)        
    # if selected == "Constituencies":
    #     DisplayStates(api.get_constituencies)    


else:
    Login(manage_login)
