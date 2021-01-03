import tkinter as tk
from tkinter import *
import mysql.connector

#App Class
class NutritionApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.resizable(False,False)
        self.frame = None #Frame shown in window
        self.switch_frame(frameWelcome)
        self.geometry("360x740")
        self.title("UGA Nutrition")
        self.connection = None #MySql Connection
        self.cursor = None #MySql stuff
        self.Profile = None

    #Switches frame on window
    def switch_frame(self, frameClass):
        newFrame = frameClass(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = newFrame
        self.frame.pack(fill=BOTH, expand=True)
    
    #Sets up DB Stuff
    def establishCursor(self):
        self.connection = mysql.connector.connect (
        host="localHost",
        user="root",
        password="insert_password",
        database="nutrition",
        auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()
    def closeCursor(self):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

#Welcome Screen DESIGN IS FOR MATTHEW
class frameWelcome(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        Message(self, text="Welcome to UGANutrition!",width = 100).pack()
        Button(self, text= "Log In", command=lambda:master.switch_frame(frameLogin)).pack()
        Button(self, text="Register",command=lambda:master.switch_frame(frameRegister)).pack()
        Button(self, text="Continue as Guest",command=lambda:master.switch_frame(frameHome)).pack()

#Login Screen
class frameLogin(Frame):
    def submitLogin(self,user,password,master):
        username = user.get()
        password = password.get()
        #Establishing a cursor to execute query
        master.establishCursor()
        master.cursor.execute('SELECT * from nutrition.profiles where user = %s',(username,))
        profile = master.cursor.fetchone()
        if profile is None:
            print("Invalid Username")
            master.closeCursor()
        elif not profile[1] == password:
            print("Invalid Password")
            master.closeCursor()
        else:
            #need to replace with my profile frame
            master.Profile = Profile(username)
            master.switch_frame(frameHome)
            master.closeCursor()

    def __init__(self,master):
        Frame.__init__(self,master)
        Label(self,text="Username",pady=10).pack()
        userInput = Entry(self,width=30)
        userInput.pack()
        passInput = Entry(self,width=30)
        Label(self,text="Password",pady=10).pack()
        passInput.pack()
        Button(self,text="Submit",command=lambda:self.submitLogin(userInput,passInput,master)).pack()
        Button(self,text="Back",command=lambda:master.switch_frame(frameWelcome)).pack()

#Register Screen
class frameRegister(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        Label(self,text="Enter Username",pady=10).pack()
        userInput = Entry(self,width=30)
        userInput.pack()
        passInput = Entry(self,width=30)
        Label(self,text="Enter Password",pady=10).pack()
        passInput.pack()
        Button(self,text="Submit",pady=5,command=lambda:self.submitRegister(userInput,passInput,master)).pack()
        Button(self,text="Back",pady=5,command=lambda:master.switch_frame(frameLogin)).pack()

    def submitRegister(self,user,password,master):
        username = user.get()
        password = password.get()
        if username != "" and password != "":
            #Establishing a cursor to execute query
            master.establishCursor()
            master.cursor.execute('SELECT * from nutrition.profiles where user = %s',(username,))
            profile = master.cursor.fetchone()
            if profile is None:
                master.closeCursor()
                master.establishCursor()
                master.cursor.execute('INSERT INTO profiles VALUES (%s,%s)',(username,password))
                master.closeCursor()
                master.switch_frame(frameWelcome)
            else:
                print("Username is already taken")
                master.closeCursor()

class frameHome(Frame):
    def __init__(self,master):
        guestAcc = False
        Frame.__init__(self,master)
        if master.Profile is None:
            master.Profile = Profile("Guest")
            guestAcc = True
        Label(self,text="Hello " + master.Profile.user + "!",font=("Calibri",18),padx=5,pady=5).place(x=0,y=0)
        Button(self,text="Track Meals",command=lambda:master.switch_frame(frameTrackMeals)).grid(row=1,column=0)
        goals = Button(self,text="Goals")
        goals.grid(row=1,column=1)
        Button(self,text="Favorite Meals").grid(row=2,column=0)
        if guestAcc:
            goals["state"] = DISABLED

class frameTrackMeals(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        Label(self,text="Track your meals!").pack(side="left")
        self.add = Button(self,text="Add Meal",command=lambda:self.showSearchbar())
        self.searchBar = Entry(self)
        self.search = Button(self,text="Search",command=lambda:self.execute(self.searchBar.get(),master))
        self.add.pack()
    
    def showSearchbar(self):
        self.add.pack_forget()
        self.searchBar.pack()
        self.search.pack()
    
    def execute(self,query,master):
        self.searchBar.forget()
        self.search.forget()
        master.establishCursor()
        master.cursor.execute('SELECT * FROM Food where Name = %s',(query,))
        tmp = master.cursor.fetchone()
        master.Profile.addFood(Food(tmp))


class Profile():
    def __init__(self,user):
        self.user = user
        self.foodList = []
    
    def addFood(self,Food):
        self.foodList.append(Food)

class Food():
    def __init__(self,list):
        self.name = list[0]
        self.cal = list[1]
        self.fat = list[2]
        self.carb = list[3]
        self.protein = list[4]
    
    
 #:) starting the app
if __name__ == "__main__":
    app = NutritionApp()
    app.mainloop(0)
       