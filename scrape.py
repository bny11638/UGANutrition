import requests
import json
from bs4 import BeautifulSoup
import re
import csv

diningHallList = ["bolton","snelling","the-niche","village-summit","oglethorpe"]
# Bolton
def loadFood(diningHall):
    url = "https://apps.auxiliary.uga.edu/Dining/BuildYourPlate//nutrition/viewMenu/" + diningHall
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    count = 0
    fileHandle = open("csvData/" + diningHall + ".csv", "a+")
    fileHandle.write("Name,Calories,Protein,Carbs,Fat\n")
    for item in soup.findAll('li'):
        for a in item.findAll('a'):
            print("\n")
            data = a.get('data-nutrition')
            if data is not None:
                names = json.loads(data)
                food_id = re.sub(",", "",names['serving-name'])
                protein = re.sub("g","",names['protein'])
                carb = re.sub("g","",names['total-carb'])
                fat = re.sub("g","",names['total-fat'])
                print("Name:\t\t" + names['serving-name'])
                print("Calories:\t" + names['calories'])
                print("Protein:\t" + protein)
                print("Carbs:\t\t" + carb)
                print("Fat:\t\t" + fat)
                fileHandle.write(food_id + "," + names['calories'] + "," + protein + "," + carb + "," + fat + "\n")

#For Loop
for x in diningHallList:
    loadFood(x)

