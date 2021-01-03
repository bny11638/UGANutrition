from attributes.ProfileClass import Profile
from attributes.FoodClass import Food
import tkinter as tk
from tkinter import *
from frames import *

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