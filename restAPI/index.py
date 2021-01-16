from flask import Flask, jsonify, request
import requests
app = Flask(__name__)
from models.base import Base, engine, Session, encoder, AlchemyEncoder, object_as_dict
from models.profile import Profile, ProfileFood
from models.food import Food
import json
from datetime import date

session = Session()
"""
@app.route("/intialize")
def initialize():
    Base.metadata.create_all(engine) #creating database schema
    session = Session() #Creating a session
    return("Hello World")
"""
#convert's date json to string json
def dateConvert(o):
    if isinstance(o, date):
        return o.__str__()

@app.route("/rollback")
def rollback():
    session.rollback()
    return "ok"

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
        except Exception as e:
            return "False" + str(e)   
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
    request_json = request.get_json()
    username = request_json['name']
    new_goal = request_json['goal_calorie']
    if request.method=='POST':
        try:
            session.query(Profile).filter(Profile.name == username).update({Profile.goal_calories:new_goal})
            return "Success"
        except Exception as e:
            return str(e)  

@app.route("/edit/goal_weight",methods = ['POST'])
def goalWeightEdit():
    request_json = request.get_json()
    username = request_json['name']
    new_goal = request_json['goal_weight']
    if request.method=='POST':
        try:
            session.query(Profile).filter(Profile.name == username).update({Profile.goal_weight:new_goal})
            return "Success"
        except Exception as e:
            return str(e)  

@app.route("/edit/add",methods = ['POST'])
def addFood():
    request_json = request.get_json()
    username = request_json['name']
    target = ProfileFood(username,request_json['food_name'],request_json['calories'],request_json['protein'],request_json['fat'],request_json['carb'],request_json['insert_date'])
    if request.method=='POST':
        try:
            session.add(target)
            session.commit()
            return "True"
        except Exception as e:
            return str(e)  
    return

@app.route("/diary/delete",methods = ['POST'])
def deleteFood():
    return

@app.route("/diary/cur_weight",methods = ['POST'])
def setCurWeight():
    return

@app.route("/diary/food", methods=['POST'])
def foodList():
    request_json = request.get_json()
    username = request_json['name']
    insert_date = request_json['instance_date']
    if request.method=='POST':
        query = session.query(ProfileFood).filter(ProfileFood.profile_id==username).filter(ProfileFood.insert_date==insert_date)
        if query is None:
            return "False"
        else:
            query = query.all()
            dictlist = []
            for profileFood in query:
                dictlist.append(dict(profileFood.asDict()))
            return json.dumps(dictlist,default = dateConvert)
    return "Not Okay"

