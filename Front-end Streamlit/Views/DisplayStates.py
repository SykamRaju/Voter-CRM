import streamlit as st
from typing import Callable
import pandas as pd 
from streamlit_option_menu import option_menu

class DisplayStates:
    def __init__(self,get_states:Callable[[],list]):

        selected2 = option_menu(None, ["View States","Add State", "Edit State", "Delete State"], 
        
        menu_icon="cast", default_index=0, orientation="horizontal")
        selected2

        if selected2 == "View States":
            st.header("List of States")
            states=get_states()
            if states is None:
                st.error("error getting states")
            else:
                st.table(states)


        if selected2 == "Add State":
            st.write('Add State here....')

        if selected2 == "Edit State":
            st.write('Edit State here....')


        if selected2 == "Delete State":
            st.write('Delete State here....')        

        
            