import tkinter as tk
from tkinter import *
import mysql.connector

#App Class
class NutritionApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame = None
        self.switch_frame(frameWelcome)
        self.geometry("450x300")
        self.title("UGA Nutrition")
        self.connection = None
        self.cursor = None
        self.Profile = None

    def switch_frame(self, frameClass):
        newFrame = frameClass(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = newFrame
        self.frame.pack()
    
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

#Welcome Screen
class frameWelcome(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        Message(self, text="Welcome to UGANutrition!",width = 100).pack()
        Button(self, text= "Log In", command=lambda:master.switch_frame(frameLogin)).pack()
        Button(self, text="Register",command=lambda:master.switch_frame(frameRegister)).pack()
        Button(self, text="Continue as Guest",command=lambda:master.switch_frame(frameHome)).pack()

#Login Screen
class frameLogin(Frame):
    def submitLogin(user,password,master):
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
        Button(self,text="Submit",command=lambda:frameLogin.submitLogin(userInput,passInput,master)).pack()
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
        Button(self,text="Submit",pady=5,command=lambda:frameRegister.submitRegister(userInput,passInput,master)).pack()
        Button(self,text="Back",pady=5,command=lambda:master.switch_frame(frameLogin)).pack()

    def submitRegister(user,password,master):
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
        Label(self,text="Hello " + master.Profile.user + "!").grid(row=0,column=0)
        Button(self,text="Add Food").grid(row=1,column=0)
        goals = Button(self,text="Change Goals")
        goals.grid(row=1,column=1)
        if guestAcc:
            goals["state"] = DISABLED

class frameAddFood(Frame):
    def __init__(self,master):
        return


class Profile():
    def __init__(self,user):
        self.user = user

    

 #:) starting the app
if __name__ == "__main__":
    app = NutritionApp()
    app.mainloop(0)
       