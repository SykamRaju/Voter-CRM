import streamlit as st
from API import API
import extra_streamlit_components as stx
from streamlit_option_menu import option_menu
import toml
import os
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

from Views.AddState import AddState
from Views.DisplayStates import DisplayStates
from Views.EditState import EditState
from Views.DeleteState import DeleteState

from Views.AddDistrict import AddDistrict
from Views.DisplayDistricts import DisplayDistricts
from Views.EditDistrict import EditDistrict
from Views.DeleteDistrict import DeleteDistrict

from Views.AddConstituency import AddConstituency
from Views.DisplayConstituencies import DisplayConstituencies
from Views.EditConstituency import EditConstituency
from Views.DeleteConstituency import DeleteConstituency

from Views.DisplayParties import DisplayParties
from Views.AddParty import AddParty
from Views.DeleteParty import DeleteParty
from Views.UpdateParty import UpdateParty

from Views.ChangePassword import ChangePassword
from Views.RegisterAgent import RegisterAgent
from Views.Login import Login

from Views.VotersList import DisplayVoters

from Views.UploadBooths import UploadBooths
from Views.ListBooths import ListBooths
from Views.DownloadBooths import DownloadBooths

from Views.UploadVoters import UploadVoters
from Views.ListVoters import ListVoters
from Views.DownloadVoters import DownloadVoters

from Views.Analytics import ClusterIdentification
from Views.Analytics import VoterOtherAnalysis
from Views.Analytics import VoterFinancialAnalysis
from Views.Analytics import VoterPersonalDetailAnalysis
from Views.Analytics import PoliticalAffinity1
from Views.Analytics import PoliticalAffinity2

st.set_page_config(page_title = 'Voter CRM',
                   layout='wide',
                  initial_sidebar_state="expanded")

json_file_name = 'voter_data.json'
@st.cache_data
def convert_json_file_to_df(json_file_name):
    return pd.read_json(json_file_name)

df = convert_json_file_to_df(json_file_name)

config = toml.load(".streamlit/config.toml")
api_base_url = "http://{}:8000/".format(
    os.getenv('SERVER_URL', '127.0.0.1')
)

st.markdown("""
        <style>
            .main .block-container {
                margin-top: -4rem;
            }
            footer {visibility: hidden;}
        </style>
        """, unsafe_allow_html=True)
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

cookie_manager = stx.CookieManager()
cookies = cookie_manager.get_all()
authentication_token = cookies.get(
    "token") if type(cookies) == dict else cookies

api = API(api_base_url, authentication_token)


def manage_login(login_details):
    token = api.login(login_details)
    cookie_manager.set("token", token)
    return token is not None


def manage_signup(signup_details):
    return api.signup(signup_details)


def manage_changepassword(password_details):
    return api.change_password(password_details)


def register_agent(agent_details):
    return api.signup(agent_details)


if api.is_logged_in():

    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["States", "Districts", "Constituencies",
                     "Political Parties", "Polling Booths","Display Voters List", "Register Agent", "Analytics", "Change Password", "Log Out"],
            icons=['patch-check', 'patch-check', 'patch-check', 'patch-check', 'patch-check', 'patch-check',
                   'patch-check', 'person-plus', 'shuffle', 'box-arrow-left'],
            menu_icon="app-indicator",
            styles={
                "container": {"padding": "5px !important"},
                "icon": {"font-size": "24px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                             "--hover-color": "rgba(128,128,128,0.25)"}
            }
        )

        if selected == "Analytics":
            with st.sidebar:
                with st.expander("Select Street"):
                    street = df['street'].unique()
                    selected_streets = st.multiselect("Choose Street", street, default=street, key = "1")

            with st.expander("Select Ward"):
                ward = df['ward'].unique()
                selected_wards = st.multiselect("Choose Ward", ward, default=ward, key = "2")

            with st.expander("Select Constituency"):
                constituency = df['constituency_name'].unique()
                selected_constituencies = st.multiselect("Choose Constituency", constituency, default=constituency, key = "3")

            with st.expander("Select Polling Booth"):
                polling_booth = df['polling_booth_name'].unique()
                selected_booths = st.multiselect("Choose Polling Booth", polling_booth, default=polling_booth, key = "4")

            with st.expander("Select Polling Booth No."):
                polling_booth_no = df['polling_booth_no'].unique()
                selected_booth_no = st.multiselect("Choose Polling Booth No.", polling_booth_no, default=polling_booth_no, key = "5")

            with st.expander("Select Gender"):
                gender = df['voter_gender'].unique()
                selected_genders = st.multiselect("Choose Gender", gender, default=gender, key = "6")

            with st.expander("Select Marital Status"):
                marital_status = df['voter_marital_status'].unique()
                selected_marital_status = st.multiselect("Choose Marital Status", marital_status, default=marital_status, key = "7")

            with st.expander("Select Dependents of Voter"):
                voter_dependents = df['number_of_dependents_of_the_voter'].unique()
                selected_voter_dependents = st.multiselect("Choose Dependents of Voter", voter_dependents, default=voter_dependents, key = "8")

            with st.expander("BPL Voter?"):
                bpl = df['BPL'].unique()
                selected_bpl_voters = st.multiselect("Choose BPL Voter?", bpl, default=bpl, key = "9")

            with st.expander("Select Police Cases on Voter"):
                police_case = df['number_of_police_cases_on_voter'].unique()
                selected_police_cases = st.multiselect("Choose Police Cases on Voter", police_case, default=police_case, key = "10")

            with st.expander("Select Police Cases on Family"):
                police_case_family = df['number_of_police_cases_on_voters_family_members'].unique()
                selected_police_cases_family = st.multiselect("Choose Police Cases on Family", police_case_family, default=police_case_family, key = "11")

            with st.expander("Select Voter Political Party"):
                political_party = df['voter_political_party'].unique()
                selected_political_parties = st.multiselect("Choose Voter Political Party", political_party, default=political_party, key = "12")

            with st.expander("Select Political Party Voter Wish to Vote"):
                political_party_to_vote = df['which_political_party_you_wish_to_vote'].unique()
                selected_parties_to_vote = st.multiselect("Choose Political Party Voter Wish to Vote", political_party_to_vote, default=political_party_to_vote, key = "13")

            with st.expander("Select Voter Opinion on Present Govt."):
                opn_present_govt = df['opinion_label_on_present_government'].unique()
                selected_opn_present_govt = st.multiselect("Choose Voter Opinion on Present Govt.", opn_present_govt, default=opn_present_govt, key = "14")

            with st.expander("Select Voter Opinion on Local MLA"):
                opn_local_MLA = df['opinion_label_on_local_MLA'].unique()
                selected_opn_local_MLA = st.multiselect("Choose Voter Opinion on Local MLA", opn_local_MLA, default=opn_local_MLA, key = "15")

            with st.expander("Select Voter Opinion on Opp Party MLA"):
                opn_opp_MLA = df['opinion_label_on_opposition_party_MLA_candidate'].unique()
                selected_opn_opp_MLA = st.multiselect("Choose Voter Opinion on Opp Party MLA", opn_opp_MLA, default=opn_opp_MLA, key = "36")

            with st.expander("Select Voter Opinion Corporator/Village President"):
                opn_corp_president = df['opinion_label_on_local_coporator_or_village_president'].unique()
                selected_opn_corp_president = st.multiselect("Choose Voter Opinion Corporator/Village President", opn_corp_president, default=opn_corp_president, key = "16")

            with st.expander("Voter Politically Neutral?"):
                politically_neutral = df['whether_voter_is_politically_neutral'].unique()
                selected_politically_neutral = st.multiselect("Choose Politically Neutral?", politically_neutral, default=politically_neutral, key = "17")

            with st.expander("Select Voter Reservation Category"):
                reservation = df['reservation_category'].unique()
                selected_reservation = st.multiselect("Choose Voter Reservation Category", reservation, default=reservation, key = "18")

            with st.expander("Select Voter Religion"):
                religion = df['voter_religion'].unique()
                selected_religion = st.multiselect("Choose Voter Religion", religion, default=religion, key = "19")

            with st.expander("Select Voter Caste"):
                caste = df['voter_caste'].unique()
                selected_caste = st.multiselect("Choose Voter Caste", caste, default=caste, key = "20")

            with st.expander("Select Voter Mother Tongue"):
                mother_tongue = df['voter_mother_tongue'].unique()
                selected_mother_tongue = st.multiselect("Choose Voter Mother Tongue", mother_tongue, default=mother_tongue, key = "21")

            with st.expander("Voter Migrated?"):
                migrated = df['whether_voter_is_migrated_from_another_place'].unique()
                selected_migrated = st.multiselect("Choose Voter Migrated?", migrated, default=migrated, key = "22")

            with st.expander("Select Voter Education"):
                education = df['voter_educational_qualification'].unique()
                selected_education = st.multiselect("Choose Voter Education", education, default=education, key = "23")

            with st.expander("Select Voter Profession"):
                profession = df['voter_profession'].unique()
                selected_profession = st.multiselect("Choose Voter Profession", profession, default=profession, key = "24")

            with st.expander("Voter Getting Govt. Benefits?"):
                voter_govt_benefits = df['whether_voter_is_getting_government_benefits'].unique()
                selected_voter_govt_benefits = st.multiselect("Choose Voter Getting Govt. Benefits?", voter_govt_benefits, default=voter_govt_benefits, key = "25")

            with st.expander("Family Getting Govt. Benefits?"):
                family_govt_benefits = df['whether_voters_family_is_getting_government_benefits'].unique()
                selected_family_govt_benefits = st.multiselect("Choose Family Getting Govt. Benefits?", family_govt_benefits, default=family_govt_benefits, key = "26")

            with st.expander("Select Family Members Visited Foreign Country"):
                family_visited_foreign = df['number_of_members_visited_foreign_country_in_voters_family'].unique()
                selected_family_visited_foreign = st.multiselect("Choose Family Members Visited Foreign Country", family_visited_foreign, default=family_visited_foreign, key = "27")

            with st.expander("Voter Accepts Money?"):
                voter_accept_money = df['whether_voter_accepts_money_from_political_party'].unique()
                selected_voter_accept_money = st.multiselect("Choose Voter Accepts Money?", voter_accept_money, default=voter_accept_money, key = "28")

            with st.expander("Family Accepts Money?"):
                family_accept_money = df['whether_voters_family_accepts_money_from_political_party'].unique()
                selected_family_accept_money = st.multiselect("Choose Family Accepts Money?", family_accept_money, default=family_accept_money, key = "29")

            with st.expander("Voter Own House?"):
                voter_own_house = df['voter_has_own_house'].unique()
                selected_voter_own_house = st.multiselect("Choose Voter Own House?", voter_own_house, default=voter_own_house, key = "30")

            with st.expander("Voter Own Car?"):
                voter_own_car = df['voter_has_own_car'].unique()
                selected_voter_own_car = st.multiselect("Choose Voter Own Car?", voter_own_car, default=voter_own_car, key = "31")

            with st.expander("Voter Own Bike?"):
                voter_own_bike = df['voter_has_own_bike'].unique()
                selected_voter_own_bike = st.multiselect("Choose Voter Own Bike?", voter_own_bike, default=voter_own_bike, key = "32")

            with st.expander("Voting First Time?"):
                voting_first_time = df['voting_first_time'].unique()
                selected_voting_first_time = st.multiselect("Choose Voting First Time?", voting_first_time, default=voting_first_time, key = "33")

            with st.expander("Voted in Last Election?"):
                voted_in_last_election = df['voted_in_last_election'].unique()
                selected_voted_in_last_election = st.multiselect("Choose Voted in Last Election?", voted_in_last_election, default=voted_in_last_election, key = "34")

            with st.expander("Voter Handicap?"):
                voter_handicap = df['is_voter_handicap'].unique()
                selected_voter_handicap = st.multiselect("Choose Voter Handicap?", voter_handicap, default=voter_handicap, key = "35")
            filter={"selected_streets":selected_streets,"selected_booth_no":selected_booth_no,"selected_booths":selected_booths,"selected_bpl_voters":selected_bpl_voters,"selected_caste":selected_caste,"selected_constituencies":selected_constituencies,"selected_education":selected_education,"selected_family_accept_money":selected_family_accept_money,"selected_family_govt_benefits":selected_family_govt_benefits,"selected_family_visited_foreign":selected_family_visited_foreign,"selected_genders":selected_genders,"selected_marital_status":selected_marital_status,"selected_migrated":selected_migrated,"selected_mother_tongue":selected_mother_tongue,"selected_opn_corp_president":selected_opn_corp_president,"selected_opn_local_MLA":selected_opn_local_MLA,"selected_opn_opp_MLA":selected_opn_opp_MLA,"selected_opn_present_govt":selected_opn_present_govt,"selected_parties_to_vote":selected_parties_to_vote,"selected_police_cases":selected_police_cases,"selected_police_cases_family":selected_police_cases_family,"selected_political_parties":selected_political_parties,"selected_politically_neutral":selected_politically_neutral,"selected_profession":selected_profession,"selected_religion":selected_religion,"selected_reservation":selected_reservation,"selected_voter_dependents":selected_voter_dependents,"selected_voted_in_last_election":selected_voted_in_last_election,"selected_voter_accept_money":selected_voter_accept_money,"selected_voter_govt_benefits":selected_voter_govt_benefits,"selected_voter_handicap":selected_voter_handicap,"selected_voter_own_bike":selected_voter_own_bike,"selected_voter_own_car":selected_voter_own_car,"selected_voter_own_house":selected_voter_own_house,"selected_voting_first_time":selected_voting_first_time,"selected_wards":selected_wards}

    ###############################################################
    #
    #   L O G O U T
    #
    ###############################################################
    if selected == "Log Out":
        if api.admin_logout():
            st.success("Logging out!")
            st.session_state.runpage = Login(manage_login, manage_signup)
            st.experimental_rerun()
        else:
            st.error("An error occurred during logout!")

    ###############################################################
    #
    #   C H A N G E  P A S S W O R D
    #
    ###############################################################

    if selected == "Change Password":
        ChangePassword(manage_changepassword)

    ###############################################################
    #
    #   S T A T E S
    #
    ###############################################################
    if selected == "States":
        tab1, tab2, tab3, tab4 = st.tabs(
            ["View States", "Add State", "Edit State", "Delete State"])

        with tab1:
            # List States
            DisplayStates(api.get_states)

        with tab2:
            # Add a State
            AddState(api.add_state)

        with tab3:
            # Edit State
            EditState(api.get_states, api.edit_state)

        with tab4:
            # Delete State
            DeleteState(api.get_states, api.delete_state)

    ###############################################################
    #
    #   D I S T R I C T S
    #
    ###############################################################
    if selected == "Districts":
        tab1, tab2, tab3, tab4 = st.tabs(
            ["View Districts", "Add District", "Edit District", "Delete District"])

        with tab1:
            # List Districts
            DisplayDistricts(api.get_states,api.get_districts_for_given_state)

        with tab2:
            # Add a District
            AddDistrict(api.get_states, api.add_district)

        with tab3:
            # Edit District
            EditDistrict(api.get_states,api.get_districts_for_given_state, api.edit_district)

        with tab4:
            # Delete District
            DeleteDistrict(api.get_states,api.get_districts_for_given_state, api.delete_district)

    ###############################################################
    #
    #   C O N S T I T U E N C I E S
    #
    ###############################################################
    if selected == "Constituencies":
        tab1, tab2, tab3, tab4 = st.tabs(
            ["View Constituencies", "Add Constituency", "Edit Constituency", "Delete Constituency"])

        with tab1:
            # List Constituencies
            # DisplayConstituencies(api.get_constituencies)
            DisplayConstituencies(api.get_states,api.get_districts_for_given_state,api.get_constituencies_for_given_district)
            


        with tab2:
            # Add a Constituency
            AddConstituency(api.get_states,api.get_districts_for_given_state,api.add_constituency)

        with tab3:
            # Edit Constituency
            EditConstituency(api.get_states,api.get_districts_for_given_state,api.get_constituencies_for_given_district, api.edit_constituency)

        with tab4:
            # Delete Constituency
            # DeleteConstituency(api.get_constituencies_for_given_district, api.delete_constituency)
            DeleteConstituency(api.get_states,api.get_districts_for_given_state,api.get_constituencies_for_given_district, api.delete_constituency)

    



     ###############################################################
    #
    #   P O L L I N G   B O O T H S
    #
    ###############################################################
    if selected == "Polling Booths":
        tab1, tab2, tab3 = st.tabs(
            ["Upload Polling Booths", "View Polling Booths", "Download Polling Booths"])

        with tab1:
            # Upload Polling Booths
            UploadBooths(api.upload_polling_booths)
            
        with tab2:
            # View Polling Booths
            ListBooths(api.get_states,api.get_districts_for_given_state,api.get_constituencies_for_given_district, api.list_polling_booths)

        with tab3:
            # Download Polling Booths
            DownloadBooths(api.get_states,api.get_districts_for_given_state,api.get_constituencies_for_given_district, api.download_polling_booths)


    


    
    
    
    ###############################################################
    #
    #   D I S P L A Y   V O T E R S   L I S T
    #
    ###############################################################
    if selected == "Display Voters List":
        # DisplayVoters(api.get_voters)
        tab1, tab2, tab3 = st.tabs(
            ["Upload Voters", "View Voters", "Download Voters"])

        with tab1:
            # Upload Voters
            UploadVoters(api.upload_voters)
            
        with tab2:
            # View Voters
            ListVoters(api.get_states,api.get_districts_for_given_state,api.get_constituencies_for_given_district, api.list_voters)

        with tab3:
            # Download Voters
            DownloadVoters(api.get_states,api.get_districts_for_given_state,api.get_constituencies_for_given_district, api.download_voters)


    ###############################################################
    #
    #   R E G I S T E R   A N   A G E N T
    #
    ###############################################################
    if selected == "Register Agent":
        RegisterAgent(register_agent)

    ###############################################################
    #
    #   P O L I T I C A L  P A R T I E S
    #
    ###############################################################
    if selected == "Political Parties":
        tab1, tab2, tab3, tab4 = st.tabs(
            ["View Political Parties", "Add Political Party","Update Political Party", "Delete Political Party"])

        with tab1:
            # List Political Parties
            DisplayParties(api.get_parties)

        with tab2:
            # Add a Political Party
            AddParty(api.add_party,api.get_states)

        with tab3:
            # Update a Political Party
            UpdateParty(api.get_states,api.get_parties,api.edit_party)    

        with tab4:
            # Delete a Political Party
            DeleteParty(api.get_parties, api.delete_party)

    ###############################################################
    #
    #   A N A L Y T I C S
    #
    ###############################################################
    if selected == "Analytics":
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
            ["Political Affinity 1","Political Affinity 2","Voter Personal Detail Analysis", "Voter Financial Analysis", "Voter Other Analysis", "Cluster Identification"])

        with tab1:
            PoliticalAffinity1(df,filter)

        with tab2:
            PoliticalAffinity2(df,filter)

        with tab3:
            VoterPersonalDetailAnalysis(df,filter)

        with tab4:
            VoterFinancialAnalysis(df,filter)

        with tab5:
            VoterOtherAnalysis(df,filter)

        with tab6:
            # Delete State
            ClusterIdentification(df,filter)

elif api.is_agent_logged_in():
    with st.sidebar:
        agent_selected = option_menu(
            menu_title="Main Menu",
            options=["Display Voters List", "Change Password", "Log Out"],
            icons=['patch-check', 'shuffle', 'box-arrow-left'],
            menu_icon="app-indicator",
            styles={
                "container": {"padding": "5px !important"},
                "icon": {"font-size": "24px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                             "--hover-color": "rgba(128,128,128,0.25)"}
            }
        )

###############################################################
    #
    #   D I S P L A Y   V O T E R S   L I S T
    #
    ###############################################################
    if agent_selected == "Display Voters List":
        # DisplayVoters(api.get_voters)
        tab1, tab2, tab3 = st.tabs(
            ["Upload Voters", "View Voters", "Download Voters"])

        with tab1:
            # Upload Voters
            UploadVoters(api.upload_voters)
            
        with tab2:
            # View Voters
            ListVoters(api.get_states,api.get_districts_for_given_state,api.get_constituencies_for_given_district, api.list_voters)

        with tab3:
            # Download Voters
            DownloadVoters(api.get_states,api.get_districts_for_given_state,api.get_constituencies_for_given_district, api.download_voters)        

    ###############################################################
    #
    #   L O G O U T
    #
    ###############################################################
    if agent_selected == "Log Out":
        if api.agent_logout():
            st.success("Logging out!")
            st.session_state.runpage = Login(manage_login, manage_signup)
            st.experimental_rerun()
        else:
            st.error("An error occurred during logout!")

    ###############################################################
    #
    #   C H A N G E  P A S S W O R D
    #
    ###############################################################

    if agent_selected == "Change Password":
        ChangePassword(manage_changepassword)



else:
    Login(manage_login, manage_signup)
