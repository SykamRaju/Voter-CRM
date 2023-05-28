import streamlit as st
from typing import Callable
import pandas as pd 
from streamlit_option_menu import option_menu
from Views.AddConstituency import AddConstituency
from API import API

class DisplayConstituencies:
    def __init__(self,get_constituencies:Callable[[],list]):
        st.header("List of Constituencies")
        constituencies=get_constituencies()
        if constituencies is None:
            st.error("Error getting Constituencies")
        else:
            st.table(constituencies)


        

        
            