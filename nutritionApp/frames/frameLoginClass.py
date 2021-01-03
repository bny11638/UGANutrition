from attributes.ProfileClass import Profile
import tkinter as tk
from tkinter import *

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
        Button(self,text="Back",command=lambda:master.switch_frame(master.welcomeFrame)).pack()