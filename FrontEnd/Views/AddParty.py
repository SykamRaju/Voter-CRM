import streamlit as st
from typing import Callable

class AddParty:
    def __init__(self, add_party: Callable[[str, str], bool], get_states: Callable[[str, str], bool]):
        st.header("Add New Political Party")

        states = get_states()
        state_details = {state["State_Name"]: {key: value for key, value in state.items() if key != "State_Name"} for state in states}
        state_names = [state["State_Name"] for state in states]

        form = st.form("new_party")
        party_name = form.text_input("Party Name")
        party_symbol = form.text_input("Party Symbol")
        party_status = form.text_input("Party Status")
        party_state = form.selectbox("Select a State", state_names)
        State_Code = state_details[party_state]['State_Id']
        # party_state = form.text_input("Party State")
        party_president = form.text_input("Party President")

        if form.form_submit_button("Add New Political Party"):
            party_details = {
                "Party_Name": party_name,
                "Party_Symbol": party_symbol,
                "Party_Status": party_status,
                "Party_State": State_Code,
                "Party_President": party_president
            }
            success = add_party(party_details)
            if success:
                st.success("Political Party Added Successfully")
            else:
                st.error("Error adding Political Party!")
