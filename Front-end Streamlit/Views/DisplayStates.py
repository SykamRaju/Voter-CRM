import streamlit as st
from typing import Callable
import pandas as pd 
from streamlit_option_menu import option_menu
from Views.AddState import AddState
from API import API

class DisplayStates:
    def __init__(self,get_states:Callable[[],list]):
        st.header("List of States")
        states=get_states()
        if states is None:
            st.error("error getting states")
        else:
            st.table(states)


        

        
            