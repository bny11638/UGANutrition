import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


#App Class
class NutritionApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.initImage()
        self.resizable(False,False)
        self.frame = None #Frame shown in window
        self.geometry("360x740")
        self.title("UGA Nutrition")
        self.connection = None #MySql Connection
        self.cursor = None #MySql stuff
        self.Profile = None
        self.switch_frame(frameWelcome)
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
    #initializes all images
    def initImage(self):
        imguh = Image.open("resources/login.png")
        imguh = imguh.resize((250, 60), Image.ANTIALIAS) ## The (250, 250) is (height, width
        im_login = ImageTk.PhotoImage(imguh)
        self.loginButtonImg = im_login
        self.logo = ImageTk.PhotoImage(file="resources/logosmall.png")

        register = Image.open("resources/register.png")
        register = register.resize((250, 60), Image.ANTIALIAS)
        im_register = ImageTk.PhotoImage(register)
        self.registerButtonImg = im_register

        use_guest = Image.open("resources/guest.png")
        use_guest = use_guest.resize((250, 60), Image.ANTIALIAS)
        im_guest = ImageTk.PhotoImage(use_guest)
        self.guestButtonImg = im_guest

        back = Image.open("resources/back.png")
        back = back.resize((80, 25), Image.ANTIALIAS)
        im_back = ImageTk.PhotoImage(back)
        self.backButtomImg = im_back

        submit = Image.open("resources/submit.png")
        submit = submit.resize((80, 25), Image.ANTIALIAS)
        im_submit = ImageTk.PhotoImage(submit)
        self.submitButtomImg = im_submit
            
#Welcome Screen DESIGN IS FOR MATTHEW
class frameWelcome(Frame):
    def __init__(self, master):
        Frame.__init__(self,master,bg="#6B081F")
        Label(self,image=master.logo,bg="#6B081F").place(relx=0.5,rely=0.2,anchor=CENTER)
        Message(self, text="Smarter eating starts here.",width = 350, bg="#6B081F", fg="white", font=('century gothic', '18', 'bold')).place(relx=0.5,rely=0.4, anchor=CENTER)
        Button(self, image=master.loginButtonImg, bg="#6B081F", borderwidth=0, activebackground="#6B081F", command=lambda:master.switch_frame(frameLogin)).place(x=55,y=360)
        Button(self, image=master.registerButtonImg, bg="#6B081F", borderwidth=0, activebackground="#6B081F",command=lambda:master.switch_frame(frameRegister)).place(x=55, y=435)
        Button(self, image=master.guestButtonImg, bg="#6B081F", borderwidth=0, activebackground="#6B081F",command=lambda:master.switch_frame(frameHome)).place(x=55, y=510)


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
        Frame.__init__(self,master,bg="#6B081F")

        Label(self,image=master.logo,bg="#6B081F").place(relx=0.5,rely=0.2,anchor=CENTER)
        Message(self, text="Smarter eating starts here.",width = 350, bg="#6B081F", fg="white", font=('century gothic', '18', 'bold')).place(relx=0.5,rely=0.4, anchor=CENTER)
      
        Label(self,text="Username",pady=10,bg="#6B081F", fg="white", font=('century gothic', '12', 'bold')).place(x=90,y=345)
        Label(self,text="Password",pady=10,bg="#6B081F", fg="white", font=('century gothic', '12', 'bold')).place(x=90,y=395)
        userInput = Entry(self,width=30)
        userInput.place(x=90,y=380)
        passInput = Entry(self,width=30)
        passInput.place(x=90,y=430)
        Button(self,text="Submit",image=master.submitButtomImg,bg="#6B081F", borderwidth=0, activebackground="#6B081F",command=lambda:self.submitLogin(userInput,passInput,master)).place(x=190, y=460)
        Button(self,text="Back",image=master.backButtomImg,bg="#6B081F", borderwidth=0, activebackground="#6B081F",command=lambda:master.switch_frame(frameWelcome)).place(x=90,y=460)

#Register Screen
class frameRegister(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,bg="#6B081F")

        Label(self,image=master.logo,bg="#6B081F").place(relx=0.5,rely=0.2,anchor=CENTER)
        Message(self, text="Smarter eating starts here.",width = 350, bg="#6B081F", fg="white", font=('century gothic', '18', 'bold')).place(relx=0.5,rely=0.4, anchor=CENTER)
        Label(self,text="Create Username",pady=10,bg="#6B081F", fg="white", font=('century gothic', '12', 'bold')).place(x=90,y=345)
        Label(self,text="Create Password",pady=10,bg="#6B081F", fg="white", font=('century gothic', '12', 'bold')).place(x=90,y=395)
        userInput = Entry(self,width=30)
        userInput.place(x=90,y=380)
        passInput = Entry(self,width=30)
        passInput.place(x=90,y=430)
        Button(self,text="Submit",image=master.submitButtomImg,bg="#6B081F", borderwidth=0, activebackground="#6B081F",command=lambda:self.submitRegister(userInput,passInput,master)).place(x=190, y=460)
        Button(self,text="Back",image=master.backButtomImg,bg="#6B081F", borderwidth=0, activebackground="#6B081F",command=lambda:master.switch_frame(frameWelcome)).place(x=90,y=460)

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
        addButtonPhoto = PhotoImage(file='resources/redPlusButton.png')
        Frame.__init__(self,master,bg="white")
        if master.Profile is None:
            master.Profile = Profile("Guest")
            guestAcc = True
        self.getMacroPlot(master)
        Label(self,text=master.Profile.user + "'s Profile:",font=("Calibri",18),padx=5,pady=5).place(x=0,y=0)
        addButton = Button(self,image=addButtonPhoto,command=lambda:master.switch_frame(frameFoodAdd),borderwidth=0)
        addButton.pack()
        buttonBar = Frame(self)
        Button(buttonBar,text="Home",height=2).pack(side="left",expand=True,fill=tk.X)
        goals = Button(buttonBar,text="Goals",height=2)
        goals.pack(side="left",expand=True,fill=tk.X)
        Button(buttonBar,text="Food Log",height=2).pack(side="left",expand=True,fill=tk.X)
        buttonBar.pack(fill=tk.X,side="bottom")
        if guestAcc:
            goals["state"] = DISABLED
    #Creates macro plot
    def getMacroPlot(self,master):
        #Figure containing plot
        fig = Figure(figsize=(2.5,3))
        axe = fig.add_subplot()
        axe.bar(["Protein","Carbs","Fats"],[master.Profile.getTotCarb(),master.Profile.getTotFat(),master.Profile.getTotProtein()],width=.6,bottom=0)
        axe.set_title("Macronutrients",fontsize=12,loc='left')
        axe.set_ylabel('Nutrients Consumed (g)',fontsize=8)
        axe.set_ylim(bottom=0)
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().place(x=0,y=280)
        


class frameFoodAdd(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        Button(self,text="add chicken",command=lambda:self.addFoodSQL(master)).pack()
        Button(self,text="Back",command=lambda:master.switch_frame(frameHome)).pack()

    def addFoodSQL(self,master):
        chicken = Food(("Chicken",85,10,5,7))
        master.Profile.addFood(chicken)

class Profile():
    def __init__(self,user):
        self.user = user
        self.foodList = []
    def addFood(self,Food):
        self.foodList.append(Food)
    def getTotProtein(self):
        count = 0
        for x in self.foodList:
            count = count + x.getProtein()
        print(count)
        return count
    def getTotCarb(self):
        count = 0
        for x in self.foodList:
            count = count + x.getCarb()
        return count
    def getTotFat(self):
        count = 0
        for x in self.foodList:
            count = count + x.getFat()
        return count
    def getTotCal(self):
        count = 0
        for x in self.foodList:
            count = count + x.getCal()
        return count

class Food():
    def __init__(self,list):
        self.name = list[0]
        self.cal = int(list[1])
        self.fat = int(list[2])
        self.carb = int(list[3])
        self.protein = int(list[4])
    def getProtein(self):
        return self.protein
    def getCarb(self):
        return self.carb
    def getFat(self):
        return self.fat
    def getFoodID(self):
        return self.name
    def getCal(self):
        return self.cal
    
    
 #:) starting the app
if __name__ == "__main__":
    app = NutritionApp()
    app.mainloop(0)
       