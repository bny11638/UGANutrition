import tkinter
from tkinter import *

root = Tk()
root.title("UGA Nutrition")
root.geometry("450x300")

def loginClick():
    frameLogo.destroy()
    frameLogin.pack()

def submitClick(user, passWord):
    username = user.get()
    password = passWord.get()
    print(username + " " + password)
    if username == "Brandon" and password == "Yau":
        frameLogin.destroy()
        frameProfile.pack(side=("left"))


#Welcome Frame
frameLogo = Frame(root)
welcomeMess = Message(frameLogo, text="Welcome to UGANutrition!",width = 100)
logIn = Button(frameLogo, text= "Log In", command=loginClick)
register = Button(frameLogo, text="Register")
welcomeMess.pack()
frameLogo.pack()
logIn.pack()
register.pack()

#Login Frame
frameLogin = Frame(root)
usernameInput = Label(frameLogin,text="Username")
user = Entry(frameLogin, width = 30)
usernameInput.pack()
user.pack()
passwordInput = Label(frameLogin,text="Password")
password = Entry(frameLogin, width = 30)
passwordInput.pack()
password.pack()
submit = Button(frameLogin, text="Submit",command=lambda:submitClick(user,password))
submit.pack()

#Profile Frame
frameProfile = Frame(root)
txt = Label(frameProfile, text="My Profile")
txt.pack(side="left")


frameRegister = Frame(root)


root.mainloop(0)