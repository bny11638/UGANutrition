import requests
import json
from bs4 import BeautifulSoup
import re
url = "https://apps.auxiliary.uga.edu/Dining/BuildYourPlate//nutrition/viewMenu/bolton"
source_code = requests.get(url)
plain_text = source_code.text
#plain_text = plain_text.replace("&quot;", '"')
soup = BeautifulSoup(plain_text, 'html.parser')
count = 0
for item in soup.findAll('li'):
    for a in item.findAll('a'):
        print("\n")
        if count == 0:
            data = a.get('data-nutrition')
            if data is not None:
                #print(str(data))
                #data = data.replace(":", ": ")
                #data = data.replace(",", ", ")
                #ingredients_index = data.find(', "ingredients"')
                #data_json_string = data[:ingredients_index] + "}"
                #print(data_json_string)
                #data_json = json.dumps(data)
                names = json.loads(data)
                protein = re.sub("g","",names['protein'])
                carb = re.sub("g","",names['total-carb'])
                fat = re.sub("g","",names['total-fat'])
                print("Name:\t\t" + names['serving-name'])
                print("Calories:\t" + names['calories'])
                print("Protein:\t" + protein)
                print("Carbs:\t\t" + carb)
                print("Fat:\t\t" + fat)

            