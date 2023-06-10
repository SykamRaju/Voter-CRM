import streamlit as st
from typing import Callable
from PIL import Image

class Login:
    def __init__(self, on_login: Callable[[object], bool], on_signup: Callable[[object], bool]):
        _col1, _col2, col3, col4, _col5, _col6 = st.columns([0.1, 0.1, 0.2, 0.4, 0.1, 0.1])
        with col3:
            st.image(Image.open('assets/voterCRM.png'), width=125)
        with col4:
            st.title("VoterCRM")
        font_css = """
            <style>
            button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"]  > p {
            min-width: 25vw;
            }

            button[data-baseweb="tab"]:hover {
            background-color: rgba(128,128,128,0.1)
            }
            </style>
        """

        st.write(font_css, unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["Login", "Sign Up"])
      
        with tab1:
            self.Display_Login(on_login)
        with tab2:
            self.Display_Signup(on_signup)

    def Display_Login(self, on_login: Callable[[object], bool]):
        self.on_login = on_login
        self.login_username = st.text_input("Username", key='login_username')
        self.login_password = st.text_input("Password", type="password", key='login_password')
        self.login_isadmin = st.checkbox("Log-in as Administrator")

        col1, _col2, col3 = st.columns([0.2, 0.725, 0.25])
        with col1:
            st.button("Login", on_click=self.LogIn_Clicked)
        with col3:
            st.button("Forgot Password", on_click=self.Fetch_Password)

    def Display_Signup(self, on_signup: Callable[[object], bool]):
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
        self.sign_isadmin = st.checkbox("Sign Up as Administrator")
        if st.button("Sign Up"):
            self.SignUp_Clicked()

    def LogIn_Clicked(self):
        self.login_details = {
            'Username': self.login_username,
            'Password': self.login_password,
            'IsAdmin': self.login_isadmin
        }
        success = self.on_login(self.login_details)
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
            'IsAdmin': self.sign_isadmin,
            'Gender': self.sign_gender,
            'Phone_No': self.sign_phone,
            'Address': self.sign_address
        }
        success = self.on_signup(self.signup_details)
        if success:
            st.success("Sign up Successful! Please Login.")
        else:
            st.error("Sign up Failed! Please try again.")

    def Fetch_Password(self):
        st.error("Please contact the System administrator to reset your password.")
        st.stop()
