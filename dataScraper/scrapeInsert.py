import mysql.connector
import csv
from csv import reader

connection = mysql.connector.connect (
        host="localHost",
        user="root",
        password="insert_password",
        database="nutrition",
        auth_plugin='mysql_native_password'
)

fileList =['bolton.csv','snelling.csv','the-niche.csv','village-summit.csv']
def openIt(x):
    """
    with open("csvData/" + x,"r") as data:
        csvReader = reader(data)
        for line in csvReader:
            cursor = connection.cursor()
            (name,calories,protein,carbs,fat) = line
            if name == 'Name':
                continue
            else:
                val = [name,calories,protein,carbs,fat]
                print(val)
                cursor.execute('INSERT INTO nutrition.Food VALUES (%s,%s,%s,%s,%s)',val)
                cursor.close() #NEED THIS TO CLEAR CURSOR
                connection.commit() #NEED THIS LINE TO SAVE DATABASE
    """
for x in fileList:
    openIt(x)

