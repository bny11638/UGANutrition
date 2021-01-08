import requests
import json
from bs4 import BeautifulSoup
import re
import csv

url = "https://apps.auxiliary.uga.edu/Dining/BuildYourPlate//nutrition/viewMenu/bolton"
source_code = requests.get(url)
plain_text = source_code.text
#plain_text = plain_text.replace("&quot;", '"')
soup = BeautifulSoup(plain_text, 'html.parser')
count = 0
bolton_csv = open("boltonFoods.csv", "w")
bolton_csv.write("Name,Calories,Protein,Carbs,Fat\n")
with open('employee_file.csv', mode='w') as employee_file:
    food_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
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

            