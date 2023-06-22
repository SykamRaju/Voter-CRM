import streamlit as st
from typing import Callable
import pandas as pd 
from streamlit_option_menu import option_menu
from Views.AddConstituency import AddConstituency
from API import API




class DeleteConstituency:

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
        selected_district  = district_place.selectbox("Select a District", district_names,key="del_con_1")
        # st.write(districts)
        # st.table(data)

        return selected_district,district_names,districts


    def get_constituencies(self,selected_option,
                           get_constituencies_for_given_district,
                           constituency_place,
                           constituency_place_2):
        constituencies = get_constituencies_for_given_district(selected_option)
        # st.table(data)

        if constituencies is not None:
            constituencies_names = [constituency["Constituency_Name"] for constituency in constituencies if constituency is not None]
        else:
            constituencies_names = []
        
        selected_constituency = constituency_place.selectbox("Select a Constituency", constituencies_names,key="con_11")
        # constituency_place.write(constituencies_names)
        # constituency_place_2.write(get_constituencies_for_given_district)
        # constituency_place.write(get_constituencies_for_given_district)
        # constituency_place.table(data)
        return constituencies,constituencies_names,selected_constituency

    def __init__(self,get_states: Callable[[str], bool],get_districts_for_given_state: Callable[[str], bool],get_constituencies_for_given_district: Callable[[str], bool],delete_constituency: Callable[[str], bool]):
        
        st.header("Delete Constituency")

        states=get_states()
        state_details = {state["State_Name"]: {key: value for key, value in state.items() if key != "State_Name"} for state in states}

        # st.write(state_details)
        if states is not None:
            state_names = [state["State_Name"] for state in states]
            # form = st.form("edit_district")
            Existing_State_Name = st.selectbox("Select a state", state_names,key="del_con_2")

            district_place = st.empty()    

            constituency_place = st.empty()  

            constituency_place_2 = st.empty()

            # Call the function whenever the state box value changes
            selected_district,district_names,districts = self.get_districts(states,Existing_State_Name,get_districts_for_given_state,district_place)

            # Call the function whenever the district box value changes
            constituencies,constituencies_names,selected_constituency = self.get_constituencies(selected_district,
                                                     get_constituencies_for_given_district,
                                                     constituency_place,
                                                     constituency_place_2)



            if districts is not None:
                district_details = {district["District_Name"]: {key: value for key, value in district.items() if key != "District_Name"} for district in districts}
            else:
                district_details = []

            if constituencies is not None:
                constituencies_details = {constituency["Constituency_Name"]: {key: value for key, value in constituency.items() if key != "Constituency_Name"} for constituency in constituencies}
            else:
                constituencies_details = []    

            if st.button('Delete Constituency',key="del_con_3"):
                # st.write("DistrictName: ",selected_district)
                Constituency_Id = constituencies_details[selected_constituency]['Constituency_Id']
                # st.write("selected_constituency: ",selected_constituency," ",Constituency_Id)
                # st.write(constituencies_names)
                # st.write(constituencies)
                # st.write(constituencies_details)
                # st.write(constituencies_names)
                message = delete_constituency(Constituency_Id)
                st.success(message)
                    
                

        

        
            