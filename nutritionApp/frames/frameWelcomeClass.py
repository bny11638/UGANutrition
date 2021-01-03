from attributes.ProfileClass import Profile
import tkinter as tk
from tkinter import *

#Welcome Screen DESIGN IS FOR MATTHEW
class frameWelcome(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        Message(self, text="Welcome to UGANutrition!",width = 100).pack()
        Button(self, text= "Log In", command=lambda:master.switch_frame(master.loginFrame)).pack()
        Button(self, text="Register",command=lambda:master.switch_frame(master.registerFrame)).pack()
        Button(self, text="Continue as Guest",command=lambda:master.switch_frame(master.frameHome)).pack()
