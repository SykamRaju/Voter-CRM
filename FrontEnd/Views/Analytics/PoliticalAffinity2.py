import streamlit as st
import plotly.express as px

class PoliticalAffinity2:
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
            st.markdown("<h3 style='text-align: center; color: #5B9BD5;'>Political Affinity 2</h3>", unsafe_allow_html=True)

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

        # Q1,Q2 = st.columns([4,5],gap='small')

        # with Q1:
        opn_lbl_loc_MLA_df = df_selection.groupby(by = ['opinion_label_on_local_MLA']).count()[['voterid']].reset_index() 
        opn_lbl_opp_MLA_df = df_selection.groupby(by = ['opinion_label_on_opposition_party_MLA_candidate']).count()[['voterid']].reset_index() 
        opn_lbl_loc_corp_df = df_selection.groupby(by = ['opinion_label_on_local_coporator_or_village_president']).count()[['voterid']].reset_index() 
        opn_lbl_psnt_govt_df = df_selection.groupby(by = ['opinion_label_on_present_government']).count()[['voterid']].reset_index()    
        opn_lbl_loc_MLA_df['x'] = 0
        opn_lbl_opp_MLA_df['x'] = 0
        opn_lbl_loc_corp_df['x'] = 0
        opn_lbl_psnt_govt_df['x'] = 0

        c1,c2,c3,c4 = st.columns(4,gap='small')

        with c1:
            fig = px.bar(opn_lbl_loc_MLA_df, x='x', y=['voterid'], color="opinion_label_on_local_MLA", barmode="stack")
            fig.update_layout(title = {'x':0.05}, plot_bgcolor = "rgba(0,0,0,0)",height=550)
            fig.update_yaxes(visible=False, showticklabels=False)
            fig.update_xaxes(visible=False, showticklabels=False)
            fig.update_layout(
                                legend_title_text=''
                            )
            fig.update_layout(
                                title={
                                    'text': 'Opinion on Local MLA',
                                    'x': 0,  # Align title to the center of the chart
                                    'y': 0.9,  # Adjust the vertical position of the title
                                    'font': {
                                        'family': 'sans serif',  # Specify font family
                                        'color': '#5B9BD5',  # Specify font color
                                    }
                                }
                            )
            fig.update_layout(height=240)
            st.plotly_chart(fig,use_container_width=True)
                
        with c2:
            fig = px.bar(opn_lbl_opp_MLA_df, x='x', y=['voterid'], color="opinion_label_on_opposition_party_MLA_candidate", barmode="stack")
            fig.update_layout(title = {'x':0.05}, plot_bgcolor = "rgba(0,0,0,0)")
            fig.update_yaxes(visible=False, showticklabels=False)
            fig.update_xaxes(visible=False, showticklabels=False)
            fig.update_layout(
                                legend_title_text=''
                            )
            fig.update_layout(
                                title={
                                    'text': 'Opinion on Opp Party MLA',
                                    'x': 0,  # Align title to the center of the chart
                                    'y': 0.9,  # Adjust the vertical position of the title
                                    'font': {
                                        'family': 'sans serif',  # Specify font family
                                        'color': '#5B9BD5',  # Specify font color
                                    }
                                }
                            )
            fig.update_layout(height=240)
            st.plotly_chart(fig,use_container_width=True)  
        with c3:
            fig = px.bar(opn_lbl_loc_corp_df, x='x', y=['voterid'], color="opinion_label_on_local_coporator_or_village_president", barmode="stack")
            fig.update_layout(title = {'x':0.05}, plot_bgcolor = "rgba(0,0,0,0)")
            fig.update_yaxes(visible=False, showticklabels=False)
            fig.update_xaxes(visible=False, showticklabels=False)
            fig.update_layout(
                                legend_title_text=''
                            )
            fig.update_layout(
                                title={
                                    'text': 'Opinion on Local<br>Corporator/Village President',
                                    'x': 0,  # Align title to the center of the chart
                                    'y': 0.9,  # Adjust the vertical position of the title
                                    'font': {
                                        'family': 'sans serif',  # Specify font family
                                        'color': '#5B9BD5',  # Specify font color
                                    }
                                }
                            )
            fig.update_layout(height=240)
            st.plotly_chart(fig,use_container_width=True)  
        with c4:
            fig = px.bar(opn_lbl_psnt_govt_df, x='x', y=['voterid'], color="opinion_label_on_present_government", barmode="stack")
            fig.update_layout(title = {'x':0.05}, plot_bgcolor = "rgba(0,0,0,0)")
            fig.update_yaxes(visible=False, showticklabels=False)
            fig.update_xaxes(visible=False, showticklabels=False)
            fig.update_layout(
                                legend_title_text=''
                            )
            fig.update_layout(
                                title={
                                    'text': 'Opinion on Present Govt.',
                                    'x': 0,  # Align title to the center of the chart
                                    'y': 0.9,  # Adjust the vertical position of the title
                                    'font': {
                                        'family': 'sans serif',  # Specify font family
                                        'color': '#5B9BD5',  # Specify font color
                                    }
                                }
                            )
            fig.update_layout(height=240)
            st.plotly_chart(fig,use_container_width=True)

        # with Q2:
        pol_neut_df = df_selection.groupby(by = ['whether_voter_is_politically_neutral']).count()[['voterid']].reset_index() 
        vot_gov_bnft_df = df_selection.groupby(by = ['whether_voter_is_getting_government_benefits']).count()[['voterid']].reset_index() 
        family_govt_bnft_df = df_selection.groupby(by = ['whether_voters_family_is_getting_government_benefits']).count()[['voterid']].reset_index() 
        voter_accepts_df = df_selection.groupby(by = ['whether_voter_accepts_money_from_political_party']).count()[['voterid']].reset_index() 
        family_accepts_df = df_selection.groupby(by = ['whether_voters_family_accepts_money_from_political_party']).count()[['voterid']].reset_index() 
        pol_neut_df['x'] = 0
        vot_gov_bnft_df['x'] = 0
        family_govt_bnft_df['x'] = 0
        voter_accepts_df['x'] = 0
        family_accepts_df['x'] = 0

        c1,c2,c3,c4,c5 = st.columns([20,20,20,20,20],gap='small')

        with c1:
                fig = px.bar(pol_neut_df, x='x', y=['voterid'], color="whether_voter_is_politically_neutral", barmode="stack")
                fig.update_layout(title = {'x':0.05}, plot_bgcolor = "rgba(0,0,0,0)")
                fig.update_yaxes(visible=False, showticklabels=False)
                fig.update_xaxes(visible=False, showticklabels=False)
                fig.update_layout(
                                legend_title_text=''
                            )
                fig.update_layout(
                                title={
                                    'text': 'Politically Neutral Voters',
                                    'x': 0,  # Align title to the center of the chart
                                    'y': 0.9,  # Adjust the vertical position of the title
                                    'font': {
                                        'family': 'sans serif',  # Specify font family
                                        'color': '#5B9BD5',  # Specify font color
                                    }
                                }
                            )
                fig.update_layout(height=240)
                st.plotly_chart(fig,use_container_width=True)
                
        with c2:
                fig = px.bar(vot_gov_bnft_df, x='x', y=['voterid'], color="whether_voter_is_getting_government_benefits", barmode="stack")
                fig.update_layout(title = {'x':0.05}, plot_bgcolor = "rgba(0,0,0,0)")
                fig.update_yaxes(visible=False, showticklabels=False)
                fig.update_xaxes(visible=False, showticklabels=False)
                fig.update_layout(
                                legend_title_text=''
                            )
                fig.update_layout(
                                title={
                                    'text': 'Voters getting<br>Government Benefits',
                                    'x': 0,  # Align title to the center of the chart
                                    'y': 0.9,  # Adjust the vertical position of the title
                                    'font': {
                                        'family': 'sans serif',  # Specify font family
                                        'color': '#5B9BD5',  # Specify font color
                                    }
                                }
                            )
                fig.update_layout(height=240)
                st.plotly_chart(fig,use_container_width=True)  
        with c3:
                fig = px.bar(family_govt_bnft_df, x='x', y=['voterid'], color="whether_voters_family_is_getting_government_benefits", barmode="stack")
                fig.update_layout(title = {'x':0.05}, plot_bgcolor = "rgba(0,0,0,0)")
                fig.update_yaxes(visible=False, showticklabels=False)
                fig.update_xaxes(visible=False, showticklabels=False)
                fig.update_layout(
                                legend_title_text=''
                            )
                fig.update_layout(
                                title={
                                    'text': 'Voters Family getting<br>Government Benefits',
                                    'x': 0,  # Align title to the center of the chart
                                    'y': 0.9,  # Adjust the vertical position of the title
                                    'font': {
                                        'family': 'sans serif',  # Specify font family
                                        'color': '#5B9BD5',  # Specify font color
                                    }
                                }
                            )
                fig.update_layout(height=240)
                st.plotly_chart(fig,use_container_width=True)  
        with c4:
                fig = px.bar(voter_accepts_df, x='x', y=['voterid'], color="whether_voter_accepts_money_from_political_party", barmode="stack")
                fig.update_layout(title = {'x':0.05}, plot_bgcolor = "rgba(0,0,0,0)")
                fig.update_yaxes(visible=False, showticklabels=False)
                fig.update_xaxes(visible=False, showticklabels=False)
                fig.update_layout(
                                legend_title_text=''
                            )
                fig.update_layout(
                                title={
                                    'text': 'Voters Accept Money<br>from Political Party',
                                    'x': 0,  # Align title to the center of the chart
                                    'y': 0.9,  # Adjust the vertical position of the title
                                    'font': {
                                        'family': 'sans serif',  # Specify font family
                                        'color': '#5B9BD5',  # Specify font color
                                    }
                                }
                            )
                fig.update_layout(height=240)
                st.plotly_chart(fig,use_container_width=True)

        with c5:
                fig = px.bar(family_accepts_df, x='x', y=['voterid'], color="whether_voters_family_accepts_money_from_political_party", barmode="stack")
                fig.update_layout(title = {'x':0.05}, plot_bgcolor = "rgba(0,0,0,0)")
                fig.update_yaxes(visible=False, showticklabels=False)
                fig.update_xaxes(visible=False, showticklabels=False)
                fig.update_layout(
                                legend_title_text=''
                            )
                fig.update_layout(
                                title={
                                    'text': 'Voters Family Accept Money<br>from Political Party',
                                    'x': 0,  # Align title to the center of the chart
                                    'y': 0.9,  # Adjust the vertical position of the title
                                    'font': {
                                        'family': 'sans serif',  # Specify font family
                                        'color': '#5B9BD5',  # Specify font color
                                    }
                                }
                            )
                fig.update_layout(height=240)
                st.plotly_chart(fig,use_container_width=True)