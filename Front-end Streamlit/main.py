import streamlit as st
from Views.AddState import AddState
from Views.DisplayStates import DisplayStates
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


# st.title("Voter CRM Admin Portal")
# st.write(authentication_token)

# value = cookie_manager.get("token")
# st.write(value)

# response = cookie_manager.get("response")
# st.write(response)

# if True:
#     response = api.is_logged_in()
#     st.write(response)
if api.is_logged_in():
    # st.subheader("Welcome")
    # st.write("______________")
    # AddState(api.add_state)
    # st.write("___________")
    # DisplayStates(api.get_states)

    with st.sidebar:
        selected = option_menu(
            menu_title="Actions",
            options=["Log out"]
        )


    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["States","Districts","Constituencies","Parites"]
        )


    if selected == "States":
        DisplayStates(api.get_states)
    # if selected == "Districts":
    #     DisplayStates(api.get_districts)        
    # if selected == "Constituencies":
    #     DisplayStates(api.get_constituencies)    


else:
    Login(manage_login)
