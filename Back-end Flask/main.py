from firstFunctions import application,db
from models import Admins,States
from jwtservice import JWTService
from middleware import Middleware
from hashingservice import HashingService
from flask import request
from werkzeug import exceptions
import uuid

sign_up_key="sign_up_key_comes_here"
jwt_secret="secret"

jwt_service=JWTService(jwt_secret)
middleware=Middleware(jwt_service)
hashing_service=HashingService()

application.before_request(lambda :middleware.auth(request))

@application.route('/api/states')
def get_all_states():
    states = States.query.all()
    if states:
        state_list=[]
        for state in states:
            print(f'state name: {state.state_name}')
            state_dict={}
            state_dict['state_code']=state.state_code
            state_dict['state_name']=state.state_name
            state_dict['country']=state.country
            state_list.append(state_dict)
        return {"states": state_list}
    else:
        return {"message": "No states Available"}

@application.route('/api/state', methods=['POST'])
def add_state():
    body = request.json
    state = States(
        uuid.uuid4(),
        body['state_name'],
        body['country']
    )
    db.session.add(state)
    db.session.commit()
    return {"message": "New state added successfully"}

@application.route('/api/auth/login', methods=['POST'])
def log_in():
    username,password=request.json['username'],request.json['password']
    admin=Admins.query.filter_by(user_name=username).first()
    if admin is None:
        return exceptions.Unauthorized(description="Incorrect username/password combination")
    is_password_correct=hashing_service.check_bcrypt(password.encode("utf-8"),admin.password.encode("utf-8"))

    if not is_password_correct:
        return exceptions.Unauthorized(description="Incorrect username/password combination")
    token_payload={"username":username}
    token=jwt_service.generate(token_payload)

    if token is None:
        return exceptions.InternalServerError(description="Login Failed")
    return {"token":token}

@application.route("/api/auth/signup",methods=["POST"])
def sign_up():
    username, password = request.json['username'], request.json['password']
    print(f'request.headers.get("sign_up_key"): {request.headers.get("sign_up_key")}')
    print(f'sign_up_key: {sign_up_key}')
    trace = request.headers.get("sign_up_key")
    # if request.headers.get("sign_up_key")!=sign_up_key:
    #     return exceptions.Unauthorized(description="Incorrect Key")
    password_hash=hashing_service.hash_bcrypt(password.encode("utf-8")).decode("utf-8")

    admin=Admins(
        uuid.uuid4(),
        username,
        password_hash
    )
    db.session.add(admin)
    db.session.commit()
    return {"message":"Admin Created Successfully"}

@application.route("/api/auth/is_logged_in",methods=["POST"])
def is_logged_in():
    return {"status_code":200,"message":"token is valid"}

if __name__ == "__main__":
    application.run(debug=True, port=8000)