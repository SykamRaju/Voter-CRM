import streamlit as st
from typing import Callable
import plotly.express as px

class ClusterIdentification:
    def __init__(self,df,filter):
        # Check if no options are selected
        try:
            if len(filter["selected_streets"]) == 0:
                raise ValueError('Please select at least one option for Voter Street.')
            
            if len(filter["selected_booth_no"]) == 0:
                raise ValueError('Please select at least one option for Polling Booth No.')
            
            if len(filter["selected_booths"]) == 0:
                raise ValueError('Please select at least one option for Polling Booth Name.')
            
            if len(filter["selected_bpl_voters"]) == 0:
                raise ValueError('Please select at least one option for BPL Voters.')
            
            if len(filter["selected_caste"]) == 0:
                raise ValueError('Please select at least one option for Voter Caste.')
            
            if len(filter["selected_constituencies"]) == 0:
                raise ValueError('Please select at least one option for Voter Constituency.')
            
            if len(filter["selected_education"]) == 0:
                raise ValueError('Please select at least one option for Voter Education.')
            
            if len(filter["selected_family_accept_money"]) == 0:
                raise ValueError('Please select at least one option for Voter Family Accept Money.')
            
            if len(filter["selected_family_govt_benefits"]) == 0:
                raise ValueError('Please select at least one option for Voter Family Govt Benefits.')
            
            if len(filter["selected_family_visited_foreign"]) == 0:
                raise ValueError('Please select at least one option for Voter Family Visited Foreign Country.')
            
            if len(filter["selected_genders"]) == 0:
                raise ValueError('Please select at least one option for Voter Gender.')
            
            if len(filter["selected_marital_status"]) == 0:
                raise ValueError('Please select at least one option for Voter Marital Status.')
            
            if len(filter["selected_migrated"]) == 0:
                raise ValueError('Please select at least one option for Migrated Voter.')
            
            if len(filter["selected_mother_tongue"]) == 0:
                raise ValueError('Please select at least one option for Voter Mother Tongue.')
            
            if len(filter["selected_opn_corp_president"]) == 0:
                raise ValueError('Please select at least one option for Voter Opinion on Corporator/Village President.')
            
            if len(filter["selected_opn_local_MLA"]) == 0:
                raise ValueError('Please select at least one option for Voter Opinion on Local MLA.')
            
            if len(filter["selected_opn_opp_MLA"]) == 0:
                raise ValueError('Please select at least one option for Voter Opinion on Opposition Party MLA.')
            
            if len(filter["selected_opn_present_govt"]) == 0:
                raise ValueError('Please select at least one option for Voter Opinion on Present Govt.')
            
            if len(filter["selected_parties_to_vote"]) == 0:
                raise ValueError('Please select at least one option for Voter Political Party Wish to Vote.')
            
            if len(filter["selected_police_cases"]) == 0:
                raise ValueError('Please select at least one option for Police Cases on Voter.')
            
            if len(filter["selected_police_cases_family"]) == 0:
                raise ValueError('Please select at least one option for Police Cases on Voter Family.')
            
            if len(filter["selected_political_parties"]) == 0:
                raise ValueError('Please select at least one option for Voter Political Party.')
            
            if len(filter["selected_politically_neutral"]) == 0:
                raise ValueError('Please select at least one option for Voter Politically Neutral.')
            
            if len(filter["selected_profession"]) == 0:
                raise ValueError('Please select at least one option for Voter Profession.')
            
            if len(filter["selected_religion"]) == 0:
                raise ValueError('Please select at least one option for Voter Religion.')
            
            if len(filter["selected_reservation"]) == 0:
                raise ValueError('Please select at least one option for Voter Reservation.')
            
            if len(filter["selected_voter_dependents"]) == 0:
                raise ValueError('Please select at least one option for Dependents of Voter.')
            
            if len(filter["selected_voted_in_last_election"]) == 0:
                raise ValueError('Please select at least one option for Voter voted in Last Election.')
            
            if len(filter["selected_voter_accept_money"]) == 0:
                raise ValueError('Please select at least one option for Voter Accepts Money.')
            
            if len(filter["selected_voter_govt_benefits"]) == 0:
                raise ValueError('Please select at least one option for Voter Govt Benefits.')
            
            if len(filter["selected_voter_handicap"]) == 0:
                raise ValueError('Please select at least one option for Voter Handicap.')
            
            if len(filter["selected_voter_own_bike"]) == 0:
                raise ValueError('Please select at least one option for Voter Own Bike.')
            
            if len(filter["selected_voter_own_car"]) == 0:
                raise ValueError('Please select at least one option for Voter Own Car.')
            
            if len(filter["selected_voter_own_house"]) == 0:
                raise ValueError('Please select at least one option for Voter Own House.')
            
            if len(filter["selected_voting_first_time"]) == 0:
                raise ValueError('Please select at least one option for Voter Voting First Time.')
            
            if len(filter["selected_wards"]) == 0:
                raise ValueError('Please select at least one option for Voter Ward.')
                
            # Continue with your code here, assuming at least one option is selected
            # ...
            # ...

        except ValueError as e:
            # Handle the exception by displaying an error message to the user
            st.error(str(e))

        df_selection = df.query('constituency_name == @filter["selected_constituencies"] & polling_booth_no == @filter["selected_booth_no"] & opinion_label_on_local_coporator_or_village_president == @filter["selected_opn_corp_president"] & opinion_label_on_opposition_party_MLA_candidate == @filter["selected_opn_opp_MLA"] & opinion_label_on_local_MLA == @filter["selected_opn_local_MLA"] & opinion_label_on_present_government == @filter["selected_opn_present_govt"] & which_political_party_you_wish_to_vote == @filter["selected_parties_to_vote"] & is_voter_handicap == @filter["selected_voter_handicap"] & number_of_members_visited_foreign_country_in_voters_family == @filter["selected_family_visited_foreign"] & number_of_dependents_of_the_voter == @filter["selected_voter_dependents"] & voter_mother_tongue == @filter["selected_mother_tongue"] & polling_booth_name == @filter["selected_booths"] & voter_gender == @filter["selected_genders"] & voter_marital_status == @filter["selected_marital_status"] & BPL == @filter["selected_bpl_voters"] & number_of_police_cases_on_voter == @filter["selected_police_cases"] & number_of_police_cases_on_voters_family_members == @filter["selected_police_cases_family"] & voter_political_party == @filter["selected_political_parties"] & whether_voter_is_politically_neutral == @filter["selected_politically_neutral"] & reservation_category == @filter["selected_reservation"] & voter_religion == @filter["selected_religion"] & voter_caste == @filter["selected_caste"] & whether_voter_is_migrated_from_another_place == @filter["selected_migrated"] & voter_profession == @filter["selected_profession"] & voter_educational_qualification == @filter["selected_education"] & street == @filter["selected_streets"] & ward == @filter["selected_wards"] & whether_voter_is_getting_government_benefits == @filter["selected_voter_govt_benefits"] & whether_voters_family_is_getting_government_benefits == @filter["selected_family_govt_benefits"] & whether_voter_accepts_money_from_political_party == @filter["selected_voter_accept_money"] & whether_voters_family_accepts_money_from_political_party == @filter["selected_family_accept_money"] & voter_has_own_house == @filter["selected_voter_own_house"] & voter_has_own_car == @filter["selected_voter_own_car"] & voter_has_own_bike == @filter["selected_voter_own_bike"] & voting_first_time == @filter["selected_voting_first_time"] & voted_in_last_election == @filter["selected_voted_in_last_election"]')

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
            st.markdown("<h3 style='text-align: center; color: #5B9BD5;'>Cluster Identification</h3>", unsafe_allow_html=True)

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

        Q1,Q2 = st.columns((1,1))

        with Q1:
            X = df_selection[['voter_age','voter_income_per_month']]
            from sklearn.cluster import KMeans
            wcss = []
            for i in range(1, 11):
                kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
                kmeans.fit(X)
                wcss.append(kmeans.inertia_)
            kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
            y_kmeans = kmeans.fit_predict(X)
            X['cluster'] = y_kmeans
            # st.markdown("<h5 style='text-align: center; color: #5B9BD5;'>Age Vs. Voter Income per Month</h5>", unsafe_allow_html=True)
            fig = px.scatter(X, x="voter_age", y="voter_income_per_month", color="cluster")
            fig.update_layout(
                                title={
                                    'text': 'Age Vs. Voter Income per Month',
                                    'x': 0.2,  # Align title to the center of the chart
                                    'y': 0.9,  # Adjust the vertical position of the title
                                    'font': {
                                        'family': 'sans serif',  # Specify font family
                                        'color': '#5B9BD5',  # Specify font color
                                    }
                                }
                            )
            fig.update_layout(
                                xaxis_title="Age",
                                yaxis_title="Income"
                            )
            fig.update_layout(height=225)
            st.plotly_chart(fig,use_container_width=True)

        with Q2:
            X2 = df_selection[['voter_age','voter_family_income_per_month']]
            from sklearn.cluster import KMeans
            wcss = []
            for i in range(1, 11):
                kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
                kmeans.fit(X2)
                wcss.append(kmeans.inertia_)
            kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
            y_kmeans = kmeans.fit_predict(X2)
            X2['cluster'] = y_kmeans
            # st.markdown("<h5 style='text-align: center; color: #5B9BD5;'>Age Vs. Voters Family Income per Month</h5>", unsafe_allow_html=True)
            fig = px.scatter(X2, x="voter_age", y="voter_family_income_per_month", color="cluster")
            fig.update_layout(
                                title={
                                    'text': 'Age Vs. Voters Family Income per Month',
                                    'x': 0.2,  # Align title to the center of the chart
                                    'y': 0.9,  # Adjust the vertical position of the title
                                    'font': {
                                        'family': 'sans serif',  # Specify font family
                                        'color': '#5B9BD5',  # Specify font color
                                    }
                                }
                            )
            fig.update_layout(
                                xaxis_title="Age",
                                yaxis_title="Family Income"
                            )
            fig.update_layout(height=225)
            st.plotly_chart(fig,use_container_width=True)

        Q1,Q2 = st.columns([100,1])
        with Q1:
            X3 = df_selection[['voter_monthly_spending','voter_income_per_month']]
            from sklearn.cluster import KMeans
            wcss = []
            for i in range(1, 11):
                kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
                kmeans.fit(X3)
                wcss.append(kmeans.inertia_)
            kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
            y_kmeans = kmeans.fit_predict(X3)
            X3['cluster'] = y_kmeans
            # st.markdown("<h5 style='text-align: center; color: #5B9BD5;'>Voter Income Vs. Spending</h5>", unsafe_allow_html=True)
            fig = px.scatter(X3, x="voter_monthly_spending", y="voter_income_per_month", color="cluster")
            fig.update_layout(
                                title={
                                    'text': 'Voter Income Vs. Spending',
                                    'x': 0.4,  # Align title to the center of the chart
                                    'y': 0.9,  # Adjust the vertical position of the title
                                    'font': {
                                        'family': 'sans serif',  # Specify font family
                                        'color': '#5B9BD5',  # Specify font color
                                    }
                                }
                            )
            fig.update_layout(
                                xaxis_title="Spending",
                                yaxis_title="Income"
                            )
            fig.update_layout(height=230)
            st.plotly_chart(fig,use_container_width=True)

        hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
        st.markdown(hide_st_style, unsafe_allow_html=True)