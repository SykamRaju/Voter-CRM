import streamlit as st
from typing import Callable

class DisplayDistricts:
    def __init__(self,get_districts:Callable[[],list]):
        st.header("List of Districts")
        districts=get_districts()
        if districts is None:
            st.error("Districts Record is empty!")
        else:
            st.table(districts)