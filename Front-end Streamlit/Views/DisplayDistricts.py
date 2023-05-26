import streamlit as st
from typing import Callable
import pandas as pd 
from streamlit_option_menu import option_menu
from Views.AddDistrict import AddDistrict
from API import API

class DisplayDistricts:
    def __init__(self,get_districts:Callable[[],list]):
        st.header("List of Districts")
        districts=get_districts()
        if districts is None:
            st.error("error getting districts")
        else:
            st.table(districts)


        

        
            