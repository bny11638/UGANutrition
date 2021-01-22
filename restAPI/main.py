from flask import Flask, jsonify, request
import requests
app = Flask(__name__)
from models.base import Base, engine, Session, encoder, AlchemyEncoder, object_as_dict
from models.profile import Profile, ProfileFood, Profile_Weight
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

@app.route("/", methods=['GET'])
def hello_world():
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
        loginLook = session.query(Profile).filter(Profile.name==request_json['name']).filter(Profile.password==request_json['password'])
        try:
            loginLook = loginLook.one()
        except Exception as e:
            return "False" + str(e)   
        return jsonify(loginLook.asDict())

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
            dictlist = []
            for food in query:
                dictlist.append(dict(food.asDict()))
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
    request_json = request.get_json()
    username = request_json['name']
    food_name = request_json['food_name']
    insert_date = request_json['insert_date']
    if request.method=='POST':
        try:
            record_obj = session.query(ProfileFood).filter(ProfileFood.profile_id==username).filter(ProfileFood.food_name==food_name).filter(ProfileFood.insert_date==insert_date).first()
            session.delete(record_obj)
            session.commit()
            return "ok"
        except Exception as e:
            return str(e)  
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

@app.route("/diary/get_weight", methods=['POST'])
def getWeight():
    request_json = request.get_json()
    username = request_json['name']
    insert_date = request_json['instance_date']
    if request.method=='POST':
        query = session.query(Profile_Weight).filter(Profile_Weight.profile_id==username).filter(Profile_Weight.insert_date==insert_date)
        if query.first() is None:
            return "False"
        else:
            query = query.first()
            return json.dumps(query.asDict(), default = dateConvert)
    return "Oof"

#Two step query
@app.route("/diary/insert_weight",methods=['POST'])
def insertWeight():
    request_json = request.get_json()
    username = request_json['name']
    weight = request_json['weight']
    insert_date = request_json['instance_date']
    if request.method=='POST':
        query = session.query(Profile_Weight).filter(Profile_Weight.profile_id==username).filter(Profile_Weight.insert_date==insert_date)
        if query.first() is None:
            session.add(Profile_Weight(username,weight,insert_date))
            session.commit()
            return "True"
        else:
            ## update block
            query.delete(synchronize_session=False)
            session.commit()
            session.add(Profile_Weight(username,weight,insert_date))
            session.commit()
            return "True"
    return "Oof"
