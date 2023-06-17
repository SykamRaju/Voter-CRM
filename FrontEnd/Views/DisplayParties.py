import streamlit as st
from typing import Callable

class DisplayParties:
    def __init__(self,get_parties:Callable[[],list]):
        st.header("List of Political Parties")
        parties=get_parties()
        if parties is None:
            st.error("Political Parties Record is empty!")
        else:
            st.table(parties)    