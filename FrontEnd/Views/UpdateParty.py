import streamlit as st
from typing import Callable


class UpdateParty:
    def __init__(self,get_states: Callable[[str], bool],get_parties: Callable[[str], bool],edit_party: Callable[[str], bool]):
        
        st.header("Update Political Party")

        states=get_states()
        state_details = {state["State_Name"]: {key: value for key, value in state.items() if key != "State_Name"} for state in states}

        if states is not None:
            state_names = [state["State_Name"] for state in states]


        parties=get_parties()
        party_details = {party["Party_Name"]: {key: value for key, value in party.items() if key != "Party_Name"} for party in parties}

        if parties is not None:
            party_names = [party["Party_Name"] for party in parties]
            form = st.form("edit_party")
            Existing_Party_Name = form.selectbox("Select a Party", party_names)
            Update_Party_Name = form.text_input("New name for the Party")
            Update_Party_Symbol = form.text_input("New Symbol for the Party")
            Update_Party_Status = form.text_input("New Status for the Party")            
            Update_Party_State_Name = form.selectbox("Select a state", state_names)
            Update_Party_President = form.text_input("New President for the Party")

            if form.form_submit_button("Update Party details"):
                Update_Party_State = state_details[Update_Party_State_Name]['State_Id']
                # st.write(Update_Party_State)
                message = edit_party(Existing_Party_Name,Update_Party_Name,Update_Party_Symbol,Update_Party_Status,Update_Party_State,Update_Party_President)
                st.success(message)
        else:
            st.error("Political parties Record is empty!")