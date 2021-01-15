from flask import Flask, jsonify, request
import requests


app = Flask(__name__)
from models.base import Base, engine, Session, encoder, AlchemyEncoder, object_as_dict
from models.profile import Profile, ProfileFood
from models.food import Food
import json


@app.route("/intialize")
def initialize():
    Base.metadata.create_all(engine) #creating database schema
    session = Session() #Creating a session
    return("Hello World")

@app.route("/", methods=['GET','POST'])
def hello_world():
    session.add(test)
    session.commit()
    return "Hello, World!"

@app.route("/register",methods=['POST'])
def register():
    request_json = request.get_json()
    if request.method=='POST':
        user = Profile(request_json['name'],request_json['password'],None,2000)
        tmp = session.query(Profile).filter(Profile.name==user.name).first()
        if tmp is None:
            session.add(user)
            session.commit()
            return "True"
        else:
            return "False"
    else:
        return "not post"

@app.route("/login",methods=['POST'])
def login():
    request_json = request.get_json()
    if request.method=='POST':
        tmp = Profile(request_json['name'],request_json['password'],None,2000)
        loginLook = session.query(Profile).filter(Profile.name==tmp.name).filter(Profile.password==tmp.password)
        try:
            loginLook = loginLook.one()
        except:
            return "False"    
        return jsonify(object_as_dict(loginLook))

@app.route("/calorie_goal",methods=['POST'])
def calorie_goal():
    request_json = request.get_json()
    if request.method=='POST':
        tmp = Profile(request_json['name'],None,None,None)
        loginLook = session.query(Profile).filter(Profile.name==tmp.name)
        try:
            loginLook = loginLook.one()
        except:
            return "False"    
        return jsonify(object_as_dict(loginLook))  

