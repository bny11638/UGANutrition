import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
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
        Button(self,text="Back",pady=5,command=lambda:master.switch_frame(frameWelcome)).pack()

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
        addButtonPhoto = PhotoImage(file='redPlusButton.png')
        Frame.__init__(self,master)
        if master.Profile is None:
            master.Profile = Profile("Guest")
            guestAcc = True
        Label(self,text=master.Profile.user + "'s Profile:",font=("Calibri",18),padx=5,pady=5).place(x=0,y=0)
        home = Button(self,text="Home",font=("Calibri",13),width=9,height=2)
        goals = Button(self,text="Goals",font=("Calibri",13),width=9,height=2)
        foodLog = Button(self,text="Food Log",font=("Calibri",13),width=9,height=2)
        addButton = Button(self,image=addButtonPhoto,command=lambda:master.switch_frame("NOT SURE WHAT I'M DOING YET"))
        addButton.image = addButtonPhoto
        addButton.pack()
        home.place(x=0,y=685)
        goals.place(x=120,y=685)
        foodLog.place(x=240,y=685)
        addButton.place(x=280,y=600)
        if guestAcc:
            goals["state"] = DISABLED

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
       