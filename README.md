# Voter-CRM
Voter CRM - Front End(Streamlit)


## To install required dependecies

`pip3 install -r requirements.txt`


## To run project
`streamlit run main.py`

## How to build locally using Docker
git clone https://github.com/SykamRaju/Voter-CRM.git

cd Voter-CRM

docker-compose up -d Note:
This will start three services. backend, frontend and db. frontend connect backend which connects to MySQL DB for data storing and retrieving.


## How to contribute to FrontEnd code and deliver with Docker
Fork the repo https://github.com/SykamRaju/Voter-CRM.git
Note: Forking is different than cloning. Check online tutors for more details.

Clone your repo and change working directory to VoterCRM_Backend.

open docker-compose.yml and enable 'volumes:' under frontend service. Check for the comment.

run 'docker compose up -d' , this will mount your local folder FrontEnd in container.

Make changes in FrontEnd folder and just re run 'docker compose -d'. This will reflect local changes in container.

Commit the changes done in 'FrontEnd' folder and push it to remote main branch.

Commit the changes after testing locally. And contribute back to parent branch.
