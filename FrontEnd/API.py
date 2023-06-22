import requests
import extra_streamlit_components as stx
import toml

config = toml.load(".streamlit/config.toml")
api_path_auth_login = config['api_url']['auth_login']
api_path_is_logged_in = config['api_url']['is_logged_in']

api_path_agent_login = config['api_url']['agent_login']
api_path_is_agent_logged_in = config['api_url']['agent_is_logged_in']

api_path_auth_logout = config['api_url']['auth_logout']
api_path_agent_logout = config['api_url']['agent_logout']

api_path_auth_signup = config['api_url']['auth_signup']
api_path_agent_signup = config['api_url']['agent_signup']

api_path_auth_changepassword = config['api_url']['auth_changepassword']
api_path_agent_changepassword = config['api_url']['agent_changepassword']

api_path_add_state = config['api_url']['add_state']
api_path_list_states = config['api_url']['list_states']
api_path_update_state = config['api_url']['update_state']
api_path_delete_state = config['api_url']['delete_state']

api_path_add_district = config['api_url']['add_district']
api_path_list_districts = config['api_url']['list_districts']
api_path_update_district = config['api_url']['update_district']
api_path_delete_district = config['api_url']['delete_district']

api_path_add_constituency = config['api_url']['add_constituency']
api_path_list_constituencies = config['api_url']['list_constituencies']
api_path_update_constituency = config['api_url']['update_constituency']
api_path_delete_constituency = config['api_url']['delete_constituency']

api_path_list_voters = config['api_url']['list_voters']

api_path_list_parties = config['api_url']['list_parties']
api_path_add_party = config['api_url']['add_party']
api_path_delete_party = config['api_url']['delete_party']

class API:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.base_headers = {
            "Content-Type": "application/json",
            "token": token,
            "signupkey": "signupkey"
        }

    # States 

    def add_state(self,state_name,state_number):
        try:
            states = {
                "State_Name": state_name,
                "State_No": state_number
            }
            response = requests.post(self.base_url + api_path_add_state, json=states, headers=self.base_headers)
            if response.status_code == 200:
                return True
        except:
            return False

    def edit_state(self, Existing_State_Name,Update_State_Name,Update_State_No):
        try:
            states = {
                "Existing_State_Name": Existing_State_Name,
                "Update_State_Name": Update_State_Name,
                "Update_State_No": Update_State_No
            }
            response = requests.post(self.base_url + api_path_update_state, json=states, headers=self.base_headers)
            if response.status_code == 200:
                return True
        except:
            return False

    def delete_state(self, state_name):
        try:
            states = {
                "State_Name": state_name
            }
            response = requests.post(self.base_url + api_path_delete_state, json=states, headers=self.base_headers)
            if response.status_code == 200:
                return True
        except:
            return False

    def get_states(self):
        try:
            response = requests.get(self.base_url + api_path_list_states, headers=self.base_headers)
            return response.json()['states']
        except:
            return None

    # Districts 

    def get_districts(self):
        try:
            response = requests.get(self.base_url + api_path_list_districts,headers=self.base_headers)
            return response.json()['districts']
        except:
            return None
        
    def get_districts_for_given_state(self,state_no):
        try:
            state = {
                "State_Code": state_no
            }
            response = requests.post(self.base_url + api_path_list_districts,json=state, headers=self.base_headers)
            return response.json()['districts']
        except:
            return None

    def add_district(self, District_Name, District_No,State_Code):
        try:
            states = {
                "District_Name": District_Name,
                "District_No":District_No,
                "State_Code":State_Code
            }
            response = requests.post(self.base_url + api_path_add_district, json=states, headers=self.base_headers)
            if response.status_code == 200:
                return True
        except:
            return False

    def edit_district(self, Existing_District_Name,Update_District_Name,Update_District_No):
        try:
            data = {
                "Existing_District_Name": Existing_District_Name,
                "Update_District_Name": Update_District_Name,
                "Update_District_No": Update_District_No,
            }
            response = requests.post(self.base_url + api_path_update_district, json=data, headers=self.base_headers)
            if response.status_code == 200:
                return response.json()['message']
        except:
            return False

    def delete_district(self, District_Name):
        try:
            data = {
                "District_Name": District_Name,
            }
            response = requests.post(self.base_url + api_path_delete_district, json=data, headers=self.base_headers)
            if response.status_code == 200:
                return response.json()['message']
        except:
            return False

    # Constituencies 

    def get_constituencies_for_given_district(self,District_Name):
        try:
            data = {
                "District_Name": District_Name,
            }
            response = requests.post(self.base_url + api_path_list_constituencies,json=data, headers=self.base_headers)
            return response.json()['constituency']
        except:
            return None

    def add_constituency(self, Constituency_Name, Constituency_No,District_Code):
        try:
            data = {
                "Constituency_Name": Constituency_Name,
                "Constituency_No": Constituency_No,
                "District_Code" : District_Code
            }
            response = requests.post(self.base_url + api_path_add_constituency, json=data, headers=self.base_headers)
            if response.status_code == 200:
                return response.json()['message']
        except:
            return False

    def edit_constituency(self, constituency_name):
        try:
            states = {
                "constituency_name": constituency_name,
            }
            response = requests.post(self.base_url + api_path_update_constituency, json=states,
                                     headers=self.base_headers)
            if response.status_code == 200:
                return True
        except:
            return False

    def delete_constituency(self, constituency_name):
        try:
            states = {
                "constituency_name": constituency_name,
            }
            response = requests.post(self.base_url + api_path_delete_constituency, json=states,
                                     headers=self.base_headers)
            if response.status_code == 200:
                return True
        except:
            return False

    # Parties 

    def add_party(self,party_details):
        try:
            response=requests.post(self.base_url+api_path_add_party,json=party_details,headers=self.base_headers)
            if response.status_code==200:
                return True
        except:
            return False
        

    def delete_party(self,party_name):
        try:
            party={
                "Party_Name":party_name
            }
            response=requests.post(self.base_url+api_path_delete_party,json=party,headers=self.base_headers)
            if response.status_code==200:
                return True
        except:
            return False
                    

    def get_parties(self):
        try:
            response=requests.get(self.base_url+api_path_list_parties,headers=self.base_headers)
            return response.json()['Political Parties']
        except:
            return None
        
    def login(self, login_details):
        try:
            credentials = {
                "Username": login_details["Username"],
                "Password": login_details["Password"]
            }

            if login_details["IsAdmin"] == True:
                print("Logging in as Admin")
                response = requests.post(self.base_url + api_path_auth_login, json=credentials,
                                         headers=self.base_headers)
            else:
                print("Logging in as Agent")
                response = requests.post(self.base_url + api_path_agent_login, json=credentials,
                                         headers=self.base_headers)
            body = response.json()
            token = body.get("token") if type(body) == dict else None

            return token
        except:
            return None

    def is_logged_in(self):
        response = requests.get(self.base_url + api_path_is_logged_in, headers=self.base_headers)
        print("Admin: logged in:", response.status_code == 200)
        if response:
            body = response.json()
            message = body.get("message") if type(body) == dict else None
            return message and response.status_code == 200

    def is_agent_logged_in(self):
        response = requests.get(self.base_url + api_path_is_agent_logged_in, headers=self.base_headers)
        print("Agent: logged in:", response.status_code == 200)
        if response:
            body = response.json()
            message = body.get("message") if type(body) == dict else None
            return message and response.status_code == 200

    def signup(self, signup_details):
        try:
            if signup_details["IsAdmin"] == 1:
                print("Signing up as Admin")
                response = requests.post(self.base_url + api_path_auth_signup, json=signup_details,
                                         headers=self.base_headers)
                body = response.json()
                message = body.get("message") if type(body) == dict else None
                return message == "Admin Created Successfully" and response.status_code == 200
            else:
                print("Signing up an Agent")
                response = requests.post(self.base_url + api_path_agent_signup, json=signup_details,
                                         headers=self.base_headers)
                body = response.json()
                message = body.get("message") if type(body) == dict else None
                return message == "Agent Id created Successfully" and response.status_code == 200
        except:
            return None

    def change_password(self, psswrd_details):
        try:
            if self.is_logged_in():
                response = requests.post(self.base_url + api_path_auth_changepassword, json=psswrd_details,
                                         headers=self.base_headers)
            else:
                response = requests.post(self.base_url + api_path_agent_changepassword, json=psswrd_details,
                                         headers=self.base_headers)
            body = response.json()
            message = body.get("message") if type(body) == dict else None
            return message == "Password changed successfully" and response.status_code == 200
        except:
            return None

    def admin_logout(self):
        response = requests.post(self.base_url + api_path_auth_logout, headers=self.base_headers)
        return response.status_code == 200

    def agent_logout(self):
        response = requests.post(self.base_url + api_path_agent_logout, headers=self.base_headers)
        return response.status_code == 200

    # Voters
    def get_voters(self):
        try:
            response = requests.get(self.base_url + api_path_list_constituencies, headers=self.base_headers)
            return response.json()['constituencies']
        except:
            return None
