from flask import Flask, jsonify, request
import requests
app = Flask(__name__)
from models.base import Base, engine, Session, encoder, AlchemyEncoder, object_as_dict
from models.profile import Profile, ProfileFood
from models.food import Food
import json

session = Session()
"""
@app.route("/intialize")
def initialize():
    Base.metadata.create_all(engine) #creating database schema
    session = Session() #Creating a session
    return("Hello World")
"""

@app.route("/", methods=['GET','POST'])
def hello_world():
    session.add(test)
    session.commit()
    return "Hello, World!"

@app.route("/register",methods=['POST'])
def register():
    request_json = request.get_json()
    if request.method=='POST':
        user = Profile(request_json['name'],request_json['password'],None,2000,None)
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
        tmp = Profile(request_json['name'],request_json['password'],None,None,None)
        loginLook = session.query(Profile).filter(Profile.name==tmp.name).filter(Profile.password==tmp.password)
        try:
            loginLook = loginLook.one()
        except:
            return "False"    
        return jsonify(object_as_dict(loginLook))

@app.route("/fill_food",methods=['POST'])
def queryFood():
    request_json = request.get_json()
    name = request_json['food']
    if request.method=='POST':
        tmp = Food(name,None,None,None,None)
        search = "%{}%".format(name)
        query = session.query(Food).filter(Food.food_name.like(search))
        if query is None:
            return "False"
        else:
            query = query.all()
            dictlist = [dict(object_as_dict(row)) for row in query]
            return json.dumps(dictlist)
    return "Not Okay"

@app.route("/edit/goal_calorie",methods = ['POST'])
def calorieEdit():
    return

@app.route("/edit/goal_weight",methods = ['POST'])
def goalWeightEdit():
    return

@app.route("/edit/add",methods = ['POST'])
def addFood():
    return

@app.route("/diary/delete",methods = ['POST'])
def deleteFood():
    return

@app.route("/diary/cur_weight",methods = ['POST'])
def setCurWeight():
    return

