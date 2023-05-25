import requests
import extra_streamlit_components as stx
import toml

config = toml.load(".streamlit/config.toml")
api_path_auth_login = config['api_url']['auth_login']
api_path_is_logged_in = config['api_url']['is_logged_in']

api_path_state = config['api_url']['state']
api_path_states = config['api_url']['states']

class API:
    def __init__(self, base_url:str,token:str):
        self.base_url=base_url
        self.base_headers={"token":token}

    def add_state(self,state_name,country):
        try:
            states={
                "state_name":state_name,
                "country":country
            }
            response=requests.post(self.base_url+api_path_state,json=states,headers=self.base_headers)
            if response.status_code==200:
                return True
        except:
            return False

    def get_states(self):
        try:
            response=requests.get(self.base_url+api_path_states,headers=self.base_headers)
            return response.json()['states']
        except:
            return None

    def login(self,username,password):
        try:
            credentials={
                "username":username,
                "password":password
            }
            response=requests.post(self.base_url+api_path_auth_login,json=credentials)
            body=response.json()
            token=body.get("token") if type(body)==dict else None

            return token
        except:
            return None

    def is_logged_in(self):
        response=requests.post(self.base_url+api_path_is_logged_in,headers=self.base_headers)
        return response.status_code==200
    
