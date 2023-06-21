import streamlit as st
from typing import Callable


class EditState:
    def __init__(self, get_states: Callable[[str], bool], on_submit2: Callable[[str], bool]):
        st.header("Edit State")
        states=get_states()
        state_details = {state["State_Name"]: {key: value for key, value in state.items() if key != "State_Name"} for state in states}

        if states is not None:
            state_names = [state["State_Name"] for state in states]
            form = st.form("edit_state")
            Existing_State_Name = form.selectbox("Select a state", state_names)
            Update_State_Name = form.text_input("New name for the State")

            if form.form_submit_button("Update State"):
                # st.write("Existing_State_Name: ",Existing_State_Name)
                # st.write("Update_State_Name: ",Update_State_Name)
                
                Update_State_No = state_details[Existing_State_Name]['State_No']
                # st.write("Update_State_No: ",Update_State_No)
                
                # st.write(state_details)
                success = on_submit2(Existing_State_Name,Update_State_Name,Update_State_No)
                if success:
                    st.success("State Updated Successfully")
                else:
                    st.error("Error updating state")
        else:
            st.error("States Record is empty!")