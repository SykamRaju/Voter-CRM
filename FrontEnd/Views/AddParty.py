import streamlit as st
from typing import Callable

class AddParty:
    def __init__(self, on_submit: Callable[[str, str], bool]):
        st.header("Add New Political Party")

        form = st.form("new_party")
        party_name = form.text_input("Party Name")
        party_symbol = form.text_input("Party Symbol")
        party_status = form.text_input("Party Status")
        party_state = form.text_input("Party State")
        party_president = form.text_input("Party President")

        if form.form_submit_button("Add New Political Party"):
            party_details = {
                "Party_Name": party_name,
                "Party_Symbol": party_symbol,
                "Party_Status": party_status,
                "Party_State": party_state,
                "Party_President": party_president
            }
            success = on_submit(party_details)
            if success:
                st.success("Political Party Added Successfully")
            else:
                st.error("Error adding Political Party!")
