import streamlit as st
from typing import Callable
from PIL import Image

class Login:
    def __init__(self, on_login: Callable[[str, str], bool], on_signup: Callable[[object], bool]):
        col1, col2 = st.columns([0.5, 0.5])
        with col1:
            st.image(Image.open('assets/voterCRM.png'), width=125)
        with col2:
            st.title("VoterCRM")
        options = ['Login', 'Sign Up']
        st.write(
            '<style>div.row-widget.stRadio > div{flex-direction:row; justify-content: space-around;}</style>', unsafe_allow_html=True)
        option = st.radio('options', options, horizontal=True,
                          label_visibility='hidden')

        if option == 'Login':
            self.Display_Login(on_login)
        else:
            self.Display_Signup(on_signup)

    def Display_Login(self, on_login: Callable[[str, str], bool]):
        self.on_login = on_login
        st.header("Login")
        self.username = st.text_input("Username", key='login_username')
        self.password = st.text_input(
            "Password", type="password", key='login_password')

        col1, _col2, col3 = st.columns([0.2, 0.8, 0.27])
        with col1:
            st.button("Login", on_click=self.LogIn_Clicked)
        with col3:
            st.button("Forgot Pasword", on_click=self.Fetch_Password)

    def Display_Signup(self, on_signup: Callable[[object], bool]):
        self.on_signup = on_signup
        st.header("Sign Up")
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
        if st.button("Sign Up"):
            self.SignUp_Clicked()

    def LogIn_Clicked(self):
        success = self.on_login(self.username, self.password)
        if success:
            st.success("Login Successful!")
        else:
            st.error("Incorrect Username and password combination. Please try again!")

    def SignUp_Clicked(self):
        if self.sign_password != self.sign_confirm_password:
            st.error("Passwords do not match! Please Re-enter the Passwords.")
        self.signup_details = {
            'First_name': self.sign_fname,
            'Last_name': self.sign_lname,
            'Username': self.sign_username,
            'Password': self.sign_password,
            'Email_Id': self.sign_mail,
            'IsAdmin': False,
            'Gender': self.sign_gender,
            'Phone_No': self.sign_phone,
            'Address': self.sign_address
        }
        success = self.on_signup(self.signup_details)
        if success:
            st.success("Sign up Successful!")
        else:
            st.error("Sign up Failed! Please try again.")

    def Fetch_Password(self):
        st.error("Please contact the System administrator to reset your password.")
        st.stop()
