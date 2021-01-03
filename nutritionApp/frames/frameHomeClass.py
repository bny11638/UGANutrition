from attributes.ProfileClass import Profile
import tkinter as tk
from tkinter import *
from frames import *

class frameHome(Frame):
    def __init__(self,master):
        guestAcc = False
        Frame.__init__(self,master)
        if master.Profile is None:
            master.Profile = Profile("Guest")
            guestAcc = True
        Label(self,text="Hello " + master.Profile.user + "!").grid(row=0,column=0)
        Button(self,text="Track Meals",command=lambda:master.switch_frame(frameTrackMeals)).grid(row=1,column=0)
        goals = Button(self,text="Goals")
        goals.grid(row=1,column=1)
        Button(self,text="Favorite Meals").grid(row=2,column=0)
        if guestAcc:
            goals["state"] = DISABLED