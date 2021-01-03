from attributes.FoodClass import Food

class Profile():
    def __init__(self,user):
        self.user = user
        self.foodList = []
    
    def addFood(self,Food):
        self.foodList.append(Food)
