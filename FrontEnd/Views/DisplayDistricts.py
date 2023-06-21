import streamlit as st
from typing import Callable

class DisplayDistricts:
    def __init__(self,get_states: Callable[[str], bool],get_districts_for_given_state: Callable[[str], bool]):
        st.header("List of Districts")

        states=get_states()
        state_details = {state["State_Name"]: {key: value for key, value in state.items() if key != "State_Name"} for state in states}

        # st.write(state_details)
        if states is not None:
            state_names = [state["State_Name"] for state in states]
            form = st.form("view_districts")
            Existing_State_Name = form.selectbox("Select a state", state_names)

            if form.form_submit_button("Show Districts"):
                
                State_Code = state_details[Existing_State_Name]['State_Id']
                # st.write("State_Code: ",State_Code)
                
                # st.write(state_details)
                data = get_districts_for_given_state(State_Code)
                # st.write("data:",data)
                if not data:
                    st.error("No districts available in the state")
                else:                    
                    st.table(data)
                    
                