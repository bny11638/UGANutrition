from models.base import Base, object_as_dict
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from dataclasses import dataclass

class Profile(Base):
    __tablename__="profile_data"
    pid = Column(Integer, primary_key=True)
    name = Column(String(255))
    password = Column(String(255))
    goal_weight = Column(Integer)
    goal_calories = Column(Integer)
    food = relationship("ProfileFood")
    cur_weight = relationship("Profile_Weight")

    def __init__(self, name, password, goal_weight, goal_calories):
        self.name = name
        self.password = password
        self.goal_weight = goal_weight
        self.goal_calories = goal_calories

    def __repr__(self):
        return "<Profile(%s,%s,%s,%s,%s)>" % (self.pid, self.name, self.password, self.goal_weight, self.goal_calories)
    def asDict(self):
        return {"pid": self.pid, "name":self.name,"goal_calories":self.goal_calories,"goal_weight":self.goal_weight}

class ProfileFood(Base):
    __tablename__="profile_food"
    id = Column(Integer, primary_key=True)
    pid = Column(Integer, ForeignKey('profile_data.pid'))
    food_name = Column(String(255))
    calories = Column(Integer)
    protein = Column(Integer)
    fat = Column(Integer)
    carb = Column(Integer)
    insert_date = Column(Date)

    def __init__(self, profile_id, food_name, calories, protein, fat, carb, insert_date):
        self.pid= profile_id
        self.food_name = food_name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carb = carb
        self.insert_date = insert_date
    
    def asDict(self):
        return {"profile_id":self.pid,"food_name":self.food_name,"calories":self.calories,"protein":self.protein,"fat":self.fat,"carb":self.carb,"insert_date":self.insert_date}

class Profile_Weight(Base):
    __tablename__="weight_data"
    id = Column(Integer, primary_key=True)
    pid = Column(Integer, ForeignKey('profile_data.pid'))
    weight = Column(Integer)
    insert_date = Column(Date)

    def __init__(self, profile_id, weight, insert_date):
        self.pid = profile_id
        self.weight = weight
        self.insert_date = insert_date

    def asDict(self):
        return {"profile_id":self.pid,"weight":self.weight,"insert_date":self.insert_date}