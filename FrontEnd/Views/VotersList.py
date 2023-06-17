import pandas as pd
# from io import BytesIO
# from pyxlsb import open_workbook as open_xlsb
import streamlit as st
from typing import Callable
from streamlit_option_menu import option_menu
from API import API


class DisplayVoters:
    def __init__(self, get_voters: Callable[[], list]):
        st.header("Voters List")
        voters = get_voters()
        if voters is None:
            st.error("Voters Record is empty!")
        else:
            st.table(voters)
