from models.base import Base, object_as_dict
from sqlalchemy import Column, String, Integer, Date
from dataclasses import dataclass


class Food(Base):
    __tablename__="food_data"
    id = Column(Integer, primary_key=True)
    food_name = Column(String(255))
    calories = Column(Integer)
    protein = Column(Integer)
    fat = Column(Integer)
    carb = Column(Integer)

    def __init__(self, food_name, calories, protein, fat, carb):
        self.food_name = food_name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carb = carb
        self.insert_date = insert_date
    


