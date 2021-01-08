import requests
import json
from bs4 import BeautifulSoup
import re
import csv

# Bolton
url = "https://apps.auxiliary.uga.edu/Dining/BuildYourPlate//nutrition/viewMenu/bolton"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'html.parser')
count = 0
bolton_csv = open("boltonFoods.csv", "w")
bolton_csv.write("Name,Calories,Protein,Carbs,Fat\n")
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
            bolton_csv.write(food_id + "," + names['calories'] + "," + protein + "," + carb + "," + fat + "\n")

# Snelling
url = "https://apps.auxiliary.uga.edu/Dining/BuildYourPlate//nutrition/viewMenu/snelling"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'html.parser')
count = 0
snelling_csv = open("snellingFoods.csv", "w")
snelling_csv.write("Name,Calories,Protein,Carbs,Fat\n")
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
            snelling_csv.write(food_id + "," + names['calories'] + "," + protein + "," + carb + "," + fat + "\n")

# The Niche
url = "https://apps.auxiliary.uga.edu/Dining/BuildYourPlate//nutrition/viewMenu/the-niche"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'html.parser')
count = 0
the_niche_csv = open("theNicheFoods.csv", "w")
the_niche_csv.write("Name,Calories,Protein,Carbs,Fat\n")
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
            the_niche_csv.write(food_id + "," + names['calories'] + "," + protein + "," + carb + "," + fat + "\n")

# Village Summit
url = "https://apps.auxiliary.uga.edu/Dining/BuildYourPlate//nutrition/viewMenu/village-summit"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'html.parser')
count = 0
village_summit_csv = open("villageSummitFoods.csv", "w")
village_summit_csv.write("Name,Calories,Protein,Carbs,Fat\n")
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
            village_summit_csv.write(food_id + "," + names['calories'] + "," + protein + "," + carb + "," + fat + "\n")

# Oglethorpe
url = "https://apps.auxiliary.uga.edu/Dining/BuildYourPlate//nutrition/viewMenu/oglethorpe"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'html.parser')
count = 0
oglethorpe_csv = open("villageSummitFoods.csv", "w")
oglethorpe_csv.write("Name,Calories,Protein,Carbs,Fat\n")
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
            oglethorpe_csv.write(food_id + "," + names['calories'] + "," + protein + "," + carb + "," + fat + "\n")