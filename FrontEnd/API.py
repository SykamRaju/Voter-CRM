import requests
import extra_streamlit_components as stx
import toml

config = toml.load(".streamlit/config.toml")
api_path_auth_login = config['api_url']['auth_login']
api_path_is_logged_in = config['api_url']['is_logged_in']

api_path_auth_logout = config['api_url']['auth_logout']

api_path_auth_signup = config['api_url']['auth_signup']

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

class API:
    def __init__(self, base_url:str,token:str):
        self.base_url=base_url
        self.base_headers={
            "Content-Type":"application/json",
            "token":token,
            "signupkey":"signupkey",
        }

    def add_state(self,state_name,state_number):
        try:
            states={
                "State_Name":state_name,
                "State_No":state_number
            }
            response=requests.post(self.base_url+api_path_add_state,json=states,headers=self.base_headers)
            if response.status_code==200:
                return True
        except:
            return False

    def edit_state(self,state_name):
        try:
            states={
                "State_Name":state_name
            }
            response=requests.post(self.base_url+api_path_update_state,json=states,headers=self.base_headers)
            if response.status_code==200:
                return True
        except:
            return False

    def delete_state(self,state_name):
        try:
            states={
                "State_Name":state_name
            }
            response=requests.post(self.base_url+api_path_delete_state,json=states,headers=self.base_headers)
            if response.status_code==200:
                return True
        except:
            return False
                    

    def get_states(self):
        try:
            response=requests.get(self.base_url+api_path_list_states,headers=self.base_headers)
            return response.json()['states']
        except:
            return None
    
    
    # Districts 

    def get_districts(self):
        try:
            response=requests.get(self.base_url+api_path_list_districts,headers=self.base_headers)
            return response.json()['districts']
        except:
            return None
        
    def add_district(self,state_name,district_name):
        try:
            states={
                "State_Name":state_name,
                "district_name":district_name,                
            }
            response=requests.post(self.base_url+api_path_add_district,json=states,headers=self.base_headers)
            if response.status_code==200:
                return True
        except:
            return False

    def edit_district(self,district_name):
        try:
            states={
                "district_name":district_name,                
            }
            response=requests.post(self.base_url+api_path_update_district,json=states,headers=self.base_headers)
            if response.status_code==200:
                return True
        except:
            return False

    def delete_district(self,district_name):
        try:
            states={
                "district_name":district_name,                
            }
            response=requests.post(self.base_url+api_path_delete_district,json=states,headers=self.base_headers)
            if response.status_code==200:
                return True
        except:
            return False

    # Constituencies 

    def get_constituencies(self):
        try:
            response=requests.get(self.base_url+api_path_list_constituencies,headers=self.base_headers)
            return response.json()['constituencies']
        except:
            return None
        
    def add_constituency(self,district_name,constituency_name):
        try:
            states={
                "district_name":district_name,
                "districtconstituency_name_name":constituency_name,                
            }
            response=requests.post(self.base_url+api_path_add_constituency,json=states,headers=self.base_headers)
            if response.status_code==200:
                return True
        except:
            return False

    def edit_constituency(self,constituency_name):
        try:
            states={
                "constituency_name":constituency_name,                
            }
            response=requests.post(self.base_url+api_path_update_constituency,json=states,headers=self.base_headers)
            if response.status_code==200:
                return True
        except:
            return False

    def delete_constituency(self,constituency_name):
        try:
            states={
                "constituency_name":constituency_name,                
            }
            response=requests.post(self.base_url+api_path_delete_constituency,json=states,headers=self.base_headers)
            if response.status_code==200:
                return True
        except:
            return False

    def login(self,username,password):
        try:
            credentials={
                "Username":username,
                "Password":password
            }

            response=requests.put(self.base_url+api_path_auth_login,json=credentials,headers=self.base_headers)
            body=response.json()
            token=body.get("token") if type(body)==dict else None

            return token
        except:
            return None

    def is_logged_in(self):
        response=requests.get(self.base_url+api_path_is_logged_in,headers=self.base_headers)
        return response.status_code==200
    
    def signup(self, signup_details):
        try:
            response=requests.post(self.base_url+api_path_auth_signup,json=signup_details,headers=self.base_headers)
            body=response.json()
            token=body.get("token") if type(body)==dict else None

            return token
        except:
            return None

    def logout(self, token):
        response = requests.post(self.base_url+api_path_auth_logout, headers=token) 
        return response.status_code==200
