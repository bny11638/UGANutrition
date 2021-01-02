import tkinter as tk
from tkinter import *

#App Class
class NutritionApp(tk.Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(frameWelcome)
        self.geometry("450x300")
        self.title("UGA Nutrition")
    
    def switch_frame(self, frameClass):
        new_frame = frameClass(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

#Welcome Screen
class frameWelcome(tk.Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        Message(self, text="Welcome to UGANutrition!",width = 100).pack()
        Button(self, text= "Log In", command=lambda:master.switch_frame(frameLogin)).pack()
        Button(self, text="Register").pack()

#Login Screen
class frameLogin(tk.Frame):

    def submitClick(user,password,master):
        username = user.get()
        password = password.get()
        print(username + " " + password)
        #Replace with sql stuff once DB is created
        if username == "Brandon" and password == "Yau":
            master.switch_frame(frameWelcome)
        
    def __init__(self,master):
        Frame.__init__(self,master)
        Label(self,text="Username").pack()
        userInput = Entry(self,width=30)
        Label(self,text="Password").pack()
        passInput = Entry(self,width=30)
        userInput.pack()
        passInput.pack()
        Button(self,text="Submit",command=lambda:frameLogin.submitClick(userInput,passInput,master)).pack()
    
if __name__ == "__main__":
    app = NutritionApp()
    app.mainloop(0)
       