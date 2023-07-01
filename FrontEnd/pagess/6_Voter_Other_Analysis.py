import pandas as pd
import streamlit as st
import plotly.express as px
# from numerize.numerize import numerize
import plotly.graph_objects as go
import numpy as np
import streamlit.components.v1 as com
import warnings
warnings.filterwarnings('ignore')
import utils
from API import API
import extra_streamlit_components as stx
import toml
import os
from Views.Login import Login

st.set_page_config(page_title = 'Voter Other Analysis',
                   layout='wide',
                  initial_sidebar_state='collapsed')

cookie_manager = stx.CookieManager()
cookies = cookie_manager.get_all()
authentication_token = cookies.get(
    "token") if type(cookies) == dict else cookies

config = toml.load(".streamlit/config.toml")
api_base_url = "http://{}:8000/".format(
    os.getenv('SERVER_URL', '127.0.0.1')
)
api = API(api_base_url, authentication_token)


def manage_login(login_details):
    token = api.login(login_details)
    cookie_manager.set("token", token)
    return token is not None


def manage_signup(signup_details):
    return api.signup(signup_details)

@st.cache_data
def convert_excel_to_json(excel_file_path):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file_path)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    # Return the JSON data
    return json_data

excel_file_path = 'data/voterCRM.xlsx'
json_data = convert_excel_to_json(excel_file_path)

@st.cache_data
def convert_json_to_dataframe(json_data):
    # Read JSON data into a pandas DataFrame
    df = pd.read_json(json_data)

    # Return the DataFrame
    return df

df = convert_json_to_dataframe(json_data)

# @st.cache
# def get_data():
#     df = utils.convert_excel_to_df(utils.excel_file_name)
#     return df

# df = get_data()

def data(dataframe):
    st.header("Data")
    st.write(dataframe)

def convert_df(df):
    return df.to_csv().encode('utf-8')

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


if api.is_logged_in():
    st.sidebar.title("Navigation & Filters")
    # options = st.sidebar.radio('Pages', options=['Political Affinity 1','Political Affinity 2','Voter Personal Detail Analysis','Voter Financial Analysis','Voter Other Analysis','Cluster Identification','Data Dump'])

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

    try:
        # Check if no options are selected
        if len(selected_streets) == 0:
            raise ValueError('Please select at least one option for Voter Street.')
        
        if len(selected_booth_no) == 0:
            raise ValueError('Please select at least one option for Polling Booth No.')
        
        if len(selected_booths) == 0:
            raise ValueError('Please select at least one option for Polling Booth Name.')
        
        if len(selected_bpl_voters) == 0:
            raise ValueError('Please select at least one option for BPL Voters.')
        
        if len(selected_caste) == 0:
            raise ValueError('Please select at least one option for Voter Caste.')
        
        if len(selected_constituencies) == 0:
            raise ValueError('Please select at least one option for Voter Constituency.')
        
        if len(selected_education) == 0:
            raise ValueError('Please select at least one option for Voter Education.')
        
        if len(selected_family_accept_money) == 0:
            raise ValueError('Please select at least one option for Voter Family Accept Money.')
        
        if len(selected_family_govt_benefits) == 0:
            raise ValueError('Please select at least one option for Voter Family Govt Benefits.')
        
        if len(selected_family_visited_foreign) == 0:
            raise ValueError('Please select at least one option for Voter Family Visited Foreign Country.')
        
        if len(selected_genders) == 0:
            raise ValueError('Please select at least one option for Voter Gender.')
        
        if len(selected_marital_status) == 0:
            raise ValueError('Please select at least one option for Voter Marital Status.')
        
        if len(selected_migrated) == 0:
            raise ValueError('Please select at least one option for Migrated Voter.')
        
        if len(selected_mother_tongue) == 0:
            raise ValueError('Please select at least one option for Voter Mother Tongue.')
        
        if len(selected_opn_corp_president) == 0:
            raise ValueError('Please select at least one option for Voter Opinion on Corporator/Village President.')
        
        if len(selected_opn_local_MLA) == 0:
            raise ValueError('Please select at least one option for Voter Opinion on Local MLA.')
        
        if len(selected_opn_opp_MLA) == 0:
            raise ValueError('Please select at least one option for Voter Opinion on Opposition Party MLA.')
        
        if len(selected_opn_present_govt) == 0:
            raise ValueError('Please select at least one option for Voter Opinion on Present Govt.')
        
        if len(selected_parties_to_vote) == 0:
            raise ValueError('Please select at least one option for Voter Political Party Wish to Vote.')
        
        if len(selected_police_cases) == 0:
            raise ValueError('Please select at least one option for Police Cases on Voter.')
        
        if len(selected_police_cases_family) == 0:
            raise ValueError('Please select at least one option for Police Cases on Voter Family.')
        
        if len(selected_political_parties) == 0:
            raise ValueError('Please select at least one option for Voter Political Party.')
        
        if len(selected_politically_neutral) == 0:
            raise ValueError('Please select at least one option for Voter Politically Neutral.')
        
        if len(selected_profession) == 0:
            raise ValueError('Please select at least one option for Voter Profession.')
        
        if len(selected_religion) == 0:
            raise ValueError('Please select at least one option for Voter Religion.')
        
        if len(selected_reservation) == 0:
            raise ValueError('Please select at least one option for Voter Reservation.')
        
        if len(selected_voter_dependents) == 0:
            raise ValueError('Please select at least one option for Dependents of Voter.')
        
        if len(selected_voted_in_last_election) == 0:
            raise ValueError('Please select at least one option for Voter voted in Last Election.')
        
        if len(selected_voter_accept_money) == 0:
            raise ValueError('Please select at least one option for Voter Accepts Money.')
        
        if len(selected_voter_govt_benefits) == 0:
            raise ValueError('Please select at least one option for Voter Govt Benefits.')
        
        if len(selected_voter_handicap) == 0:
            raise ValueError('Please select at least one option for Voter Handicap.')
        
        if len(selected_voter_own_bike) == 0:
            raise ValueError('Please select at least one option for Voter Own Bike.')
        
        if len(selected_voter_own_car) == 0:
            raise ValueError('Please select at least one option for Voter Own Car.')
        
        if len(selected_voter_own_house) == 0:
            raise ValueError('Please select at least one option for Voter Own House.')
        
        if len(selected_voting_first_time) == 0:
            raise ValueError('Please select at least one option for Voter Voting First Time.')
        
        if len(selected_wards) == 0:
            raise ValueError('Please select at least one option for Voter Ward.')
            
        # Continue with your code here, assuming at least one option is selected
        # ...
        # ...

    except ValueError as e:
        # Handle the exception by displaying an error message to the user
        st.error(str(e))

    df_selection = df.query('constituency_name == @selected_constituencies & polling_booth_no == @selected_booth_no & opinion_label_on_local_coporator_or_village_president == @selected_opn_corp_president & opinion_label_on_opposition_party_MLA_candidate == @selected_opn_opp_MLA & opinion_label_on_local_MLA == @selected_opn_local_MLA & opinion_label_on_present_government == @selected_opn_present_govt & which_political_party_you_wish_to_vote == @selected_parties_to_vote & is_voter_handicap == @selected_voter_handicap & number_of_members_visited_foreign_country_in_voters_family == @selected_family_visited_foreign & number_of_dependents_of_the_voter == @selected_voter_dependents & voter_mother_tongue == @selected_mother_tongue & polling_booth_name == @selected_booths & voter_gender == @selected_genders & voter_marital_status == @selected_marital_status & BPL == @selected_bpl_voters & number_of_police_cases_on_voter == @selected_police_cases & number_of_police_cases_on_voters_family_members == @selected_police_cases_family & voter_political_party == @selected_political_parties & whether_voter_is_politically_neutral == @selected_politically_neutral & reservation_category == @selected_reservation & voter_religion == @selected_religion & voter_caste == @selected_caste & whether_voter_is_migrated_from_another_place == @selected_migrated & voter_profession == @selected_profession & voter_educational_qualification == @selected_education & street == @selected_streets & ward == @selected_wards & whether_voter_is_getting_government_benefits == @selected_voter_govt_benefits & whether_voters_family_is_getting_government_benefits == @selected_family_govt_benefits & whether_voter_accepts_money_from_political_party == @selected_voter_accept_money & whether_voters_family_accepts_money_from_political_party == @selected_family_accept_money & voter_has_own_house == @selected_voter_own_house & voter_has_own_car == @selected_voter_own_car & voter_has_own_bike == @selected_voter_own_bike & voting_first_time == @selected_voting_first_time & voted_in_last_election == @selected_voted_in_last_election')

    total_voters = int(df["voterid"].nunique())
    constituency_count = int(df_selection["constituency_name"].nunique())
    polling_booth_count = int(df_selection["polling_booth_name"].nunique())
    new_voters = round(((len(df_selection[df_selection["voter_age"] == 18]) / total_voters)*100),2)
    native_voters = round((len(df_selection[df_selection["whether_voter_is_migrated_from_another_place"]=="No"])/total_voters*100),2)
    police_cases_on_voter = round((len(df_selection[df_selection["number_of_police_cases_on_voter"] >= 1])/ total_voters*100),2)
    literate = round((len(df_selection[df_selection["voter_educational_qualification"] != 'Illiterate'])/total_voters*100),2)
    police_cases_on_voter_family = round((len(df_selection[df_selection["number_of_police_cases_on_voters_family_members"] >= 1])/total_voters*100),2)
    average_age = round(df_selection["voter_age"].mean(), 0)
    average_voter_per_family = round(df_selection["number_of_votes_in_voters_family"].mean(), 0)
    phone_no_count = round(((df_selection.phone_number.notnull().sum())/total_voters*100),2)
    whatsapp_no_count = round(((df_selection.whatsapp_number.notnull().sum())/total_voters*100),2)
    politically_nuetral = round((len(df_selection[df_selection["whether_voter_is_politically_neutral"]=="Yes"])/total_voters*100),2)
    voter_govt_benefits = round((len(df_selection[df_selection["whether_voter_is_getting_government_benefits"]=="Yes"])/total_voters*100),2)
    voter_family_govt_benefits = round((len(df_selection[df_selection["whether_voters_family_is_getting_government_benefits"]=="Yes"])/total_voters*100),2)
    voter_accepts_money = round((len(df_selection[df_selection["whether_voter_accepts_money_from_political_party"]=="Yes"])/total_voters*100),2)
    voter_family_accepts_money = round((len(df_selection[df_selection["whether_voters_family_accepts_money_from_political_party"]=="Yes"])/total_voters*100),2)
    own_house = round((len(df_selection[df_selection["voter_has_own_house"]=="Yes"])/total_voters*100),2)
    own_car = round((len(df_selection[df_selection["voter_has_own_car"]=="Yes"])/total_voters*100),2)
    own_bike = round((len(df_selection[df_selection["voter_has_own_bike"]=="Yes"])/total_voters*100),2)
    handicap = round((len(df_selection[df_selection["is_voter_handicap"]=="Yes"])/total_voters*100),2)
    avg_dependents = round(df_selection["number_of_dependents_of_the_voter"].mean(), 0)
    foreign_visit = round((len(df_selection[df_selection["number_of_members_visited_foreign_country_in_voters_family"] != 0])/total_voters*100),2)
    avg_monthly_income = round(df_selection["voter_income_per_month"].mean(),0)
    avg_family_monthly_income = round(df_selection["voter_family_income_per_month"].mean(),0)
    avg_monthly_spending = round(df_selection["voter_monthly_spending"].mean(),0)
    avg_monthly_family_spending = round(df_selection["voter_family_monthly_spending"].mean(),0)
    voted_last_election = round((len(df_selection[df_selection["voted_in_last_election"]=="Yes"])/total_voters*100),2)
    bpl_voter = round((len(df_selection[df_selection["BPL"]=="Yes"])/total_voters*100),2)
    vote_first_time = round(((len(df_selection[df_selection["voting_first_time"] == "Yes"]) / total_voters)*100),2)

    constituency_names = df_selection["constituency_name"].unique()
    polling_booth_names = df_selection["polling_booth_name"].unique()

    if constituency_count == 1:
        constituency_name = constituency_names[0]
    else:
        constituency_name = "Constituencies..."

    if polling_booth_count == 1:
        polling_booth_name = polling_booth_names[0]
    else:
        polling_booth_name = "Polling Booths.."

    constituency_name_str = f"""
    <h10 style='text-align: center; color: orange;'>{constituency_name}</h10>
    """
    polling_booth_name_str = f"""
    <h10 style='text-align: center; color: orange;'>{polling_booth_name}</h10>
    """

    header_1,header_2,header_3,header_4,header_5,header_6,header_7,header_8= st.columns([2,15,20,30,3,10,10,10],gap='small')

    with header_4:
        st.markdown("<h3 style='text-align: center; color: #5B9BD5;'>Voter Other Analysis</h3>", unsafe_allow_html=True)

    with header_1:
        st.image('images/constituency.png',width = 25,use_column_width="Auto")

        st.image('images/voting.png',width = 25,use_column_width="Auto")

    with header_2:
        st.markdown(constituency_name_str, unsafe_allow_html=True)
        st.markdown(polling_booth_name_str, unsafe_allow_html=True)


    with header_6:
        st.markdown("<h10 style='text-align: left; color: orange;'>Constituency Count</h10>", unsafe_allow_html=True)
        st.subheader(f" :orange[{constituency_count:,}]")

    with header_7:    
        st.markdown("<h10 style='text-align: left; color: orange;'>Polling Booth Count</h10>", unsafe_allow_html=True)
        st.subheader(f" :orange[{polling_booth_count:,}]")

    with header_8:
        st.image('images/user.png',caption = "User Name",width = 50,use_column_width='Auto')

    Q1,Q2,Q3,Q4 = st.columns([1,2,2,2])

    with Q1:
        st.markdown("")
        st.markdown("<h5 style='text-align: left; color: #5B9BD5;'>Native Voters</h5>", unsafe_allow_html=True)
        st.subheader(f" :orange[{native_voters:,}%]")

    with Q2:
        # st.markdown("<h5 style='text-align: center; color: #5B9BD5;'>Reservation Breakup</h5>", unsafe_allow_html=True)
        voter_reservation_df = df_selection.groupby('reservation_category')['voterid'].count().reset_index()
        fig_reservation = px.pie(voter_reservation_df, values='voterid', names='reservation_category',)
        fig_reservation.update_layout(
                            title={
                                'text': 'Reservation Breakup',
                                'x': 0.25,  # Align title to the center of the chart
                                'y': 0.9,  # Adjust the vertical position of the title
                                'font': {
                                    'family': 'sans serif',  # Specify font family
                                    'color': '#5B9BD5',  # Specify font color
                                }
                            }
                        )
        fig_reservation.update_layout(height=225)
        Q2.plotly_chart(fig_reservation, use_container_width=True)

    with Q3:
        # st.markdown("<h5 style='text-align: center; color: #5B9BD5;'>Voter Religion</h5>", unsafe_allow_html=True)
        voter_religion_df = df_selection.groupby('voter_religion')['voterid'].count().reset_index()
        fig_voter_religion = px.bar(voter_religion_df,x="voter_religion",y="voterid")
        fig_voter_religion.update_layout(
                            title={
                                'text': 'Voter Religion',
                                'x': 0.25,  # Align title to the center of the chart
                                'y': 0.9,  # Adjust the vertical position of the title
                                'font': {
                                    'family': 'sans serif',  # Specify font family
                                    'color': '#5B9BD5',  # Specify font color
                                }
                            }
                        )
        fig_voter_religion.update_layout(
                            xaxis_title="Religion",
                            yaxis_title="Voters"
                        )
        fig_voter_religion.update_layout(height=225)
        Q3.plotly_chart(fig_voter_religion, use_container_width=True)

    with Q4:
        # st.markdown("<h5 style='text-align: center; color: #5B9BD5;'>Caste Analysis</h5>", unsafe_allow_html=True)
        voter_caste_df = df_selection.groupby('voter_caste')['voterid'].count().reset_index()
        fig_voter_caste = px.bar(voter_caste_df,x="voter_caste",y="voterid")
        # st.plotly_chart(fig_voter_caste)
        fig_voter_caste.update_layout(
                            title={
                                'text': 'Caste Analysis',
                                'x': 0.25,  # Align title to the center of the chart
                                'y': 0.9,  # Adjust the vertical position of the title
                                'font': {
                                    'family': 'sans serif',  # Specify font family
                                    'color': '#5B9BD5',  # Specify font color
                                }
                            }
                        )
        fig_voter_caste.update_layout(
                            xaxis_title="Caste",
                            yaxis_title="Voters"
                        )
        fig_voter_caste.update_layout(height=225)
        Q4.plotly_chart(fig_voter_caste, use_container_width=True)

    Q1,Q2,Q3 = st.columns(3,gap='small')

    with Q1:
        # st.markdown("<h5 style='text-align: center; color: #5B9BD5;'>Mother Tongue</h5>", unsafe_allow_html=True)
        mother_tongue_df = df_selection.groupby('voter_mother_tongue')['voterid'].count().reset_index()
        fig_mother_tongue = px.bar(mother_tongue_df,x="voter_mother_tongue",y="voterid")
        fig_mother_tongue.update_layout(
                            title={
                                'text': 'Mother Tongue',
                                'x': 0.25,  # Align title to the center of the chart
                                'y': 0.9,  # Adjust the vertical position of the title
                                'font': {
                                    'family': 'sans serif',  # Specify font family
                                    'color': '#5B9BD5',  # Specify font color
                                }
                            }
                        )
        fig_mother_tongue.update_layout(
                            xaxis_title="Mother Tongue",
                            yaxis_title="Voters"
                        )
        fig_mother_tongue.update_layout(height=225)
        Q1.plotly_chart(fig_mother_tongue, use_container_width=True)

    with Q2:
        # st.markdown("<h5 style='text-align: center; color: #5B9BD5;'>Street Breakup</h5>", unsafe_allow_html=True)
        street_df = df_selection.groupby('street')['voterid'].count().reset_index()
        fig_street = px.bar(street_df,x="street",y="voterid")
        fig_street.update_layout(
                            title={
                                'text': 'Street Breakup',
                                'x': 0.25,  # Align title to the center of the chart
                                'y': 0.9,  # Adjust the vertical position of the title
                                'font': {
                                    'family': 'sans serif',  # Specify font family
                                    'color': '#5B9BD5',  # Specify font color
                                }
                            }
                        )
        fig_street.update_layout(
                            xaxis_title="Street",
                            yaxis_title="Voters"
                        )
        fig_street.update_layout(height=225)
        Q2.plotly_chart(fig_street, use_container_width=True)

    with Q3:
        # st.markdown("<h5 style='text-align: center; color: #5B9BD5;'>Ward Wise Breakup</h5>", unsafe_allow_html=True)
        ward_df = df_selection.groupby('ward')['voterid'].count().reset_index()
        fig_ward = px.bar(ward_df,x="ward",y="voterid")
        fig_ward.update_layout(
                            title={
                                'text': 'Ward Wise Breakup',
                                'x': 0.25,  # Align title to the center of the chart
                                'y': 0.9,  # Adjust the vertical position of the title
                                'font': {
                                    'family': 'sans serif',  # Specify font family
                                    'color': '#5B9BD5',  # Specify font color
                                }
                            }
                        )
        fig_ward.update_layout(
                            xaxis_title="Ward",
                            yaxis_title="Voters"
                        )
        fig_ward.update_layout(height=225)
        Q3.plotly_chart(fig_ward, use_container_width=True)

    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)
else:
    Login(manage_login, manage_signup)