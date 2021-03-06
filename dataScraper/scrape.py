import requests
import json
from bs4 import BeautifulSoup
import re
import csv
import mysql.connector
import csv
from csv import reader

connection = mysql.connector.connect (
        host="35.224.143.155",
        user="root",
        password='Thursdays5$',
        database="nutrition_app",
)

diningHallList = ["bolton","snelling","the-niche","village-summit","oglethorpe"]
# Bolton
def loadFood(diningHall):
    url = "https://apps.auxiliary.uga.edu/Dining/BuildYourPlate//nutrition/viewMenu/" + diningHall
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    #count = 0
    #fileHandle = open("csvData/" + diningHall + ".csv", "a+")
    #fileHandle.write("Name,Calories,Protein,Carbs,Fat\n")
    #schema is food_name,calories,protein,fat,carbs
    for item in soup.findAll('li'):
        for a in item.findAll('a'):
            print("\n")
            data = a.get('data-nutrition')
            if data is not None:
                cursor = connection.cursor()
                names = json.loads(data)
                food_id = re.sub(",", "",names['serving-name'])
                calories = names['calories']
                protein = re.sub("g","",names['protein'])
                carb = re.sub("g","",names['total-carb'])
                fat = re.sub("g","",names['total-fat'])
                val = [food_id,calories,protein,fat,carb]
                print(val)
                cursor.execute('INSERT IGNORE INTO food_data VALUES (%s,%s,%s,%s,%s)',val)
                cursor.close() #NEED THIS TO CLEAR CURSOR
                connection.commit() #NEED THIS LINE TO SAVE DATABASE
                #fileHandle.write(food_id + "," + names['calories'] + "," + protein + "," + carb + "," + fat + "\n")

for x in diningHallList:
    loadFood(x)
