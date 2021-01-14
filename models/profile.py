from models.base import Base, object_as_dict
from sqlalchemy import Column, String, Integer, Date
from dataclasses import dataclass

class Profile(Base):
    __tablename__="profile_data"
    name = Column(String(255), primary_key=True)
    password = Column(String(255))
    goal_weight = Column(Integer)
    goal_calories = Column(Integer)

    def __init__(self, name, password, goal_weight, goal_calories):
        self.name = name
        self.password = password
        self.goal_weight = goal_weight
        self.goal_calories = goal_calories

    def __repr__(self):
        return "<Profile(%s,%s,%s,%s)>" % (self.name, self.password, self.goal_weight, self.goal_calories)

    