import streamlit as st
from typing import Callable


class AddConstituency:

    def get_districts(self,states,selected_option,get_districts_for_given_state,district_place):
        # Code to be executed when the select box value changes
        state_details = {state["State_Name"]: {key: value for key, value in state.items() if key != "State_Name"} for state in states}
        State_Code = state_details[selected_option]['State_Id']
        districts = get_districts_for_given_state(State_Code)

        if districts is not None:
            district_names = [district["District_Name"] for district in districts if district is not None]
        else:
            district_names = []

        selected_district  = district_place.selectbox("Select a District", district_names,key="add_con_2")

        return selected_district,district_names,districts

    def __init__(self,
                 get_states: Callable[[str], bool],
                 get_districts_for_given_state: Callable[[str], bool],
                 add_constituency: Callable[[str], bool]):
        st.header("Add Constituency")

        states=get_states()
        state_details = {state["State_Name"]: {key: value for key, value in state.items() if key != "State_Name"} for state in states}

        # st.write(state_details)
        if states is not None:
            state_names = [state["State_Name"] for state in states]
            # form = st.form("edit_district")
            Existing_State_Name = st.selectbox("Select a state", state_names,key="add_con_1")

            district_place = st.empty()    

            new_constituency_name = st.text_input("Constituency name",key="add_con_4")
            new_constituency_number = st.text_input("Constituency number",key="add_con_5")

            # Call the function whenever the select box value changes
            selected_district,district_names,districts = self.get_districts(states,Existing_State_Name,get_districts_for_given_state,district_place)

            if districts is not None:
                district_details = {district["District_Name"]: {key: value for key, value in district.items() if key != "District_Name"} for district in districts}
            else:
                district_details = []

            if st.button('Add Constituency',key="add_con_3"):
                # st.write("DistrictName: ",selected_district)
                # st.write(district_details)
                District_Id = district_details[selected_district]['District_Id']
                # st.write(District_Id)
                # st.write(new_constituency_name)
                message = add_constituency(new_constituency_name, new_constituency_number,District_Id)
                st.success(message)
                    
                

        

        
            