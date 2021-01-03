
import tkinter as tk
from tkinter import *
from attributes.ProfileClass import Profile
import mysql.connector
from frames.frameWelcomeClass import frameWelcome
from frames.frameLoginClass import frameLogin
from frames.frameRegisterClass import frameRegister

class NutritionApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.currentFrame = None #Frame shown in window
        self.switch_frame(frameWelcome)
        self.geometry("450x300")
        self.title("UGA Nutrition")
        self.connection = None #MySql Connection
        self.cursor = None #MySql stuff
        self.Profile = None
    #defining frames
        self.welcomeFrame = frameWelcome(self)
        self.loginFrame = frameLogin(self)
        self.registerFrame = frameRegister(self)
    #Switches frame on window
    def switch_frame(self, frame):
        if self.currentFrame is not None:
            self.currentFrame.destroy()
        self.currentFrame = frame
        self.currentFrame.pack()
    
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

