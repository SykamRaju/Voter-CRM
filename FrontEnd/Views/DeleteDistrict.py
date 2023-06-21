import streamlit as st
from typing import Callable
import random

class DeleteDistrict:

    def get_districts(self,states,selected_option,get_districts_for_given_state,district_place):
        # Code to be executed when the select box value changes
        state_details = {state["State_Name"]: {key: value for key, value in state.items() if key != "State_Name"} for state in states}
        # st.write(state_details)
        # st.write("Selected option:", selected_option)
        State_Code = state_details[selected_option]['State_Id']
        districts = get_districts_for_given_state(State_Code)

        if districts is not None:
            district_names = [district["District_Name"] for district in districts if district is not None]
        else:
            district_names = []

        # district_place.write(districts)
        selected_district  = district_place.selectbox("Select a District", district_names,key="delete_dt_2")
        # district_place.text('hi')
        # district_place.selectbox('food',random.sample(range(10, 40), 4))
        # st.write(districts)
        # st.table(data)

        return selected_district,district_names,districts

    def __init__(self,get_states: Callable[[str], bool],
                 get_districts_for_given_state: Callable[[str], bool],
                 edit_district: Callable[[str], bool]):
        st.header("Edit a District")

        states=get_states()
        state_details = {state["State_Name"]: {key: value for key, value in state.items() if key != "State_Name"} for state in states}

        # st.write(state_details)
        if states is not None:
            state_names = [state["State_Name"] for state in states]
            # form = st.form("edit_district")
            Existing_State_Name = st.selectbox("Select a state", state_names,key="delete_dt_1")

            district_place = st.empty()    

            # Call the function whenever the select box value changes
            selected_district,district_names,districts = self.get_districts(states,Existing_State_Name,get_districts_for_given_state,district_place)

            if districts is not None:
                district_details = {district["District_Name"]: {key: value for key, value in district.items() if key != "District_Name"} for district in districts}
            else:
                district_details = []

            if st.button('Delete District',key="del_dt_button"):
                # st.write(district_details)
                # st.write(districts)
                # st.write(District_Id)
                # st.write(selected_district)
                message = edit_district(selected_district)
                st.success(message)
                    
                