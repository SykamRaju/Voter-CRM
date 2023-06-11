import streamlit as st
from typing import Callable

class RegisterAgent:
    def __init__(self, on_signup: Callable[[object], bool]):
        self.on_signup = on_signup
        st.header("Register Agent")
        self.on_signup = on_signup
        self.sign_username = st.text_input(
            "Preferred Username", key='sign_username')
        col1, col2 = st.columns([0.5, 0.5])
        with col1:
            self.sign_fname = st.text_input("First name", key='sign_fname')
        with col2:
            self.sign_lname = st.text_input("Last name", key='sign_lname')
        self.sign_mail = st.text_input("E-Mail", key='sign_mail')
        self.sign_phone = st.text_input("Phone Number", key='sign_phone')
        self.sign_address = st.text_area("Address", key='sign_address')
        self.sign_gender = st.radio(
            'Gender', ["Male", "Female", "Other"], horizontal=True)
        self.sign_password = st.text_input(
            "Password", type="password", key='sign_password')
        self.sign_confirm_password = st.text_input(
            "Confirm Password", type="password", key='sign_confirm_password')
        if st.button("Register Agent"):
            self.SignUp_Clicked()

    def SignUp_Clicked(self):
        if self.sign_password != self.sign_confirm_password:
            st.error("Passwords do not match! Please Re-enter the Passwords.")
        self.signup_details = {
            'First_name': self.sign_fname,
            'Last_name': self.sign_lname,
            'Username': self.sign_username,
            'Password': self.sign_password,
            'Email_Id': self.sign_mail,
            'IsAdmin': 0,
            'Gender': self.sign_gender,
            'Phone_No': self.sign_phone,
            'Address': self.sign_address
        }
        success = self.on_signup(self.signup_details)
        if success:
            st.success("Agent Registered Successfully!")
        else:
            st.error("Agent Registration Failed! Please try again.")
