import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import threading
import mysql.connector
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import time
from datetime import date
import calendar
import requests
import json
import sys
import os
import resources


HEADERS = {
                'Content-Type': 'application/json'
            }
CLOUDURL = "https://precise-truck-301217.ue.r.appspot.com" 
#CLOUDURL = "http://localhost:5000"

def find_data_file(filename):
    if getattr(sys, "frozen", False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)
    return os.path.join(datadir, 'lib', 'resources', filename)

#App Class
class NutritionApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.initImage()
        #self.resizable(False,False)
        self.frame = None #Frame shown in window
        self.geometry("1024x768")
        self.title("UGA Nutrition")
        self.connection = None #MySql Connection
        self.cursor = None #MySql stuff
        self.Profile = None
        self.switch_frame(frameWelcome)
    #Switches frame on window
    def switch_frame(self, frameClass):
        newFrame = frameClass(self)
        if self.frame is not None:
            self.frame.pack_forget()
            x = threading.Thread(target=self.frame.destroy, args=())
        self.frame = newFrame
        self.frame.pack(fill=BOTH, expand=True)
        
    #Sets up DB Stuff
    def establishCursor(self):
        self.connection = mysql.connector.connect (
        host="35.224.143.155",
        user="guest",
        password="password",
        database="nutrition_app",
        )
        self.cursor = self.connection.cursor(buffered=True)
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
    #selected date of session
        self.today = date.today()
        self.dt_string = self.today.strftime('%B %d')
        #self.instance_date = self.today.strftime("%Y/%m/%d %H:%M:%S")
        self.instance_date = self.today.isoformat()
        self.weekday = calendar.day_name[self.today.weekday()]
            
#Welcome Screen DESIGN IS FOR MATTHEW
class frameWelcome(Frame):
    def __init__(self, master):
        Frame.__init__(self,master,bg="#6B081F")
        Label(self,image=master.logo,bg="#6B081F").pack(pady=40)
        Message(self, text="Smarter eating starts here.",width = 350, bg="#6B081F", fg="white", font=('century gothic', '18', 'bold')).pack()
        Button(self, image=master.loginButtonImg, bg="#6B081F", borderwidth=0, activebackground="#6B081F", command=lambda:master.switch_frame(frameLogin)).pack(pady=10)
        Button(self, image=master.registerButtonImg, bg="#6B081F", borderwidth=0, activebackground="#6B081F",command=lambda:master.switch_frame(frameRegister)).pack(pady=10)
        Button(self, image=master.guestButtonImg, bg="#6B081F", borderwidth=0, activebackground="#6B081F",command=lambda:master.switch_frame(frameHome)).pack(pady=10)

#Login Screen
class frameLogin(Frame):
    def submitLogin(self,user,password,master):
        username = user.get()
        password = password.get()
        data = {'name':username.lower(),'password':password}
        y = json.dumps(data)
        url = CLOUDURL + "/login"
        loginRequest = requests.post(url,data=y,headers=HEADERS)
        tmp = loginRequest.text
        if tmp.find("False") > -1:
            print("Invalid Login Information")
        else:
            x = json.dumps(loginRequest.json())
            y = json.loads(x)
            y = dict(y)
            master.Profile = Profile(y['name'],master,y['goal_calories'])
            master.switch_frame(frameHome)

    def __init__(self,master):
        Frame.__init__(self,master,bg="#6B081F")
        Label(self,image=master.logo,bg="#6B081F").pack(pady=40)
        Message(self, text="Smarter eating starts here.",width = 350, bg="#6B081F", fg="white", font=('century gothic', '18', 'bold')).pack()
        Label(self,text="Username",pady=10,bg="#6B081F", fg="white", font=('century gothic', '12', 'bold')).pack(pady=2)
        userInput = Entry(self,width=30)
        userInput.pack()
        Label(self,text="Password",pady=10,bg="#6B081F", fg="white", font=('century gothic', '12', 'bold')).pack(pady=2)
        passInput = Entry(self,width=30)
        passInput.pack()
        Button(self,text="Submit",image=master.submitButtomImg,bg="#6B081F", borderwidth=0, activebackground="#6B081F",command=lambda:self.submitLogin(userInput,passInput,master)).pack(pady=(20,10))
        Button(self,text="Back",image=master.backButtomImg,bg="#6B081F", borderwidth=0, activebackground="#6B081F",command=lambda:master.switch_frame(frameWelcome)).pack()

#Register Screen
class frameRegister(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,bg="#6B081F")
        Label(self,image=master.logo,bg="#6B081F").pack(pady=40)
        Message(self, text="Smarter eating starts here.",width = 350, bg="#6B081F", fg="white", font=('century gothic', '18', 'bold')).pack()
        Label(self,text="Create Username",pady=10,bg="#6B081F", fg="white", font=('century gothic', '12', 'bold')).pack(pady=2)
        userInput = Entry(self,width=30)
        userInput.pack()
        Label(self,text="Create Password",pady=10,bg="#6B081F", fg="white", font=('century gothic', '12', 'bold')).pack(pady=2)
        passInput = Entry(self,width=30)
        passInput.pack()
        Button(self,text="Submit",image=master.submitButtomImg,bg="#6B081F", borderwidth=0, activebackground="#6B081F",command=lambda:self.submitRegister(userInput,passInput,master)).pack(pady=(20,10))
        Button(self,text="Back",image=master.backButtomImg,bg="#6B081F", borderwidth=0, activebackground="#6B081F",command=lambda:master.switch_frame(frameWelcome)).pack()

    def submitRegister(self,user,password,master):
        username = user.get().lower()
        password = password.get()
        if username != "" and password != "":
            data = {"name":username,"password":password}
            y = json.dumps(data)
            check = requests.post(CLOUDURL +"/register",data=y,headers=HEADERS)

            if check.text == 'True':
                master.switch_frame(frameWelcome)
            else:
                print("Username is already taken")

class frameHome(Frame):
    def __init__(self,master):
        if master.Profile is None:
            master.Profile = Profile("Guest",master,None)
            guestAcc = True
        Frame.__init__(self,master,bg="white")
        Label(self,text=master.Profile.user.title() + "'s Profile:",font=("Calibri",18),padx=5,pady=5,anchor='w',bg="#6B081F",fg='white').pack(side="top",expand=False,fill=tk.X)
        #matthews frame to design and develop
        date_frame = Frame(self)
        date_frame.pack()
        userFrame = Frame(self,bg="white")
        userFrame.pack(side="top",expand=1,fill=BOTH)
        rows, columns = userFrame.grid_size()
        #Put your code in this blank spot
        userFrame.columnconfigure(1, weight=1)
        Label(date_frame,text=master.weekday + ", " + master.dt_string,font=("century gothic",18),bg='white').grid(column=1)
        Label(userFrame,text="Calories Consumed:",font=("century gothic",18),anchor='w',bg='white').grid(row=1,sticky='w')
        # Calories consumed will be red if exceeding requirement needed by goal; green otherwise
        Label(userFrame,text=master.Profile.getTotCal(),font=("century gothic",18),anchor='e',bg='white').grid(row=1,column=1,sticky='e')
        # Calories remaining will be red if exceeding requirement needed by goal; green otherwise
        Label(userFrame,text="Calories Remaining:",font=("century gothic",18),anchor='w',bg='white').grid(row=2,sticky='w')
        calories_remaining = Label(userFrame,text=abs(master.Profile.getTotCal() - master.Profile.calGoal),font=("century gothic",18),anchor='e',bg='white')
        calories_remaining.grid(row=2,column=1,sticky='e')
        Label(userFrame,text="Today's Protein:",font=("century gothic",18),anchor='w',bg='white').grid(row=3,sticky='w')
        Label(userFrame,text=master.Profile.getTotProtein(),font=("century gothic",18),anchor='e',bg='white').grid(row=3,column=1,sticky='e')
        Label(userFrame,text="Today's Carbs:",font=("century gothic",18),anchor='w',bg='white').grid(row=4,sticky='w')
        Label(userFrame,text=master.Profile.getTotCarb(),font=("century gothic",18),anchor='e',bg='white').grid(row=4,column=1,sticky='e')
        Label(userFrame,text="Today's Fats:",font=("century gothic",18),anchor='w',bg='white').grid(row=5,sticky='w')
        Label(userFrame,text=master.Profile.getTotFat(),font=("century gothic",18),anchor='e',bg='white').grid(row=5,column=1,sticky='e')

        # Following if-else statement does NOT account for user's goal of gaining or losing weight;
        if master.Profile.getTotCal() - master.Profile.calGoal < 0:
            calories_remaining.config(fg="red")
        else:
            calories_remaining.config(fg="green")
            
        bar = ButtonBar(self,master)
        bar.pack(side="bottom",fill=tk.X)
        bar.homeButton['state']='disable'
        calorieFrame = Frame(self,bg="white")
        self.initMacroPlot(calorieFrame,master)
        self.initCalPlot(calorieFrame,master)
        self.initLinePlot(calorieFrame,master)
        calorieFrame.pack(side='bottom',expand=0,fill=tk.X,padx=5)
    #Creates macro plot
    def initMacroPlot(self,frame,master):
        #Figure containing plot
        FF6666=(255,102,102,)
        FFA152=(.255,.160,.82,)
        FFE666=(.255,.230,.102)
        figMacroPlot = Figure(figsize=(3,4))
        axe = figMacroPlot.add_subplot()
        axe.bar(["Protein","Carbs","Fats"],[master.Profile.getTotProtein(),master.Profile.getTotCarb(),master.Profile.getTotFat()],color=['#FF6666','#FFA152','#FFE666'],width=.6,bottom=0)
        axe.set_title("Macronutrients",fontsize=12,loc='left')
        axe.set_ylabel('Nutrients Consumed (g)',fontsize=8)
        axe.set_ylim(bottom=0)
        figMacroPlot.set_tight_layout(True)
        canvasMacro = FigureCanvasTkAgg(figMacroPlot, master=frame)
        canvasMacro.draw()
        canvasMacro.get_tk_widget().pack(side='right')
    #Create Calorie Bar
    def initCalPlot(self,frame,master):
        #Figure containing cal
        figCalPlot = Figure(figsize=(6,1.5))
        axe = figCalPlot.add_subplot()
        axe.barh([""],[master.Profile.getTotCal()] ,height = .005, color = '#52BE80')
        axe.set_ylabel("Calories (kj)")
        if master.Profile.calGoal is not None:
            axe.axvline(x=master.Profile.calGoal)
        else:
            axe.axvline(x=2000)
        axe.set_title("Calories Consumed")
        axe.set_xlim(0)
        figCalPlot.set_tight_layout(True)
        canvasCal = FigureCanvasTkAgg(figCalPlot, master=frame)
        canvasCal.draw()
        canvasCal.get_tk_widget().pack(fill=tk.X)
    def initLinePlot(self,frame,master):
        fig = Figure(figsize=(6,2.5))
        axe = fig.add_subplot()
        axe.plot(["Jan","Feb","Mar","April","May","June","July","Aug","Sept","Oct","Nov","Dec"],[150,155,160,155,150,145,140,135,130,133,128,130])
        axe.set_title("Progress")
        axe.set_ylabel("Weight in Pounds (lbs)")
        fig.set_tight_layout(True)
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.X)


class frameFoodAdd(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.buttonList = []
        self.figMacroCanvas = None
        self.figPieCanvas = None
        self.figCalCanvas = None
        #top part -- search bar
        searchFrame = Frame(self,bg="#6B081F")
        Label(searchFrame,text="Search Foods:",bg="#6B081F",fg="white",font=('century gothic', '14')).pack(side="left",expand=False,fill=X)
        self.submitButton = Button(searchFrame,text="Submit",image=master.submitButtomImg,borderwidth=0,bg="#6B081F",activebackground="#6B081F",fg="white",command=lambda:self.addFoodSQL(master,self.search.get()))
        self.submitButton.pack(side="right")
        self.search = Entry(searchFrame,width=100)
        self.search.pack(pady=10,fill=tk.X,expand=1,side="left") #testattu
        searchFrame.pack(fill=tk.X)
        #bottom part -- bottom bar
        bar = ButtonBar(self,master)
        bar.pack(side="bottom",fill=tk.X)
        bar.addButton['state']='disable'
        #left hand result search barh
        self.resultFrame = Frame(self,bg="gray",width=3)
        Label(self.resultFrame,text="Results",font=('century gothic', '10')).pack(fill=tk.X)
        self.resultFrame.pack(side='left',fill=BOTH,padx=(0,5),expand=1)
        #right hand display plots
        self.displayFrame = Frame(self,bg="gray")
        self.displayFrame.pack(side='left',fill=BOTH,expand=1)
        self.topFrame = Frame(self.displayFrame,bg="white")
        self.topFrame.pack(fill=BOTH,expand=1,pady=(0,0.5))
        Label(self.topFrame,text="Nutrition:",font=('century gothic', '10')).pack(fill=BOTH)
        #Bottom Frame
        self.bottomFrame = Frame(self.displayFrame,bg="gray")
        self.bottomFrame.pack(fill=BOTH,expand=1)
        self.initCalPlot(None,master,self.bottomFrame)
        self.initMacroBar(None,master,self.bottomFrame)
        self.initPieGraph(None,master,self.bottomFrame)
        

    def addFoodSQL(self,master,food):
        data = {'food':food}
        y = json.dumps(data)
        url = CLOUDURL + "/fill_food"
        foodRequest = requests.post(url,data=y,headers=HEADERS)
        resultQuery = foodRequest.text
        self.clearSearchFrame(master)
        self.initSearchFrame(master,json.loads(resultQuery))
    def clearSearchFrame(self,master):
        buttonCount = 0
        for button in self.buttonList:
            button.destroy()
        self.buttonList.clear()
    def initSearchFrame(self,master,results):
        for dictionary in results:
            x = Button(self.resultFrame,text=dictionary['food_name'].title(),anchor='w',width=4,command=lambda food=dictionary:self.clickFood(food,master),font=('century gothic',8))
            self.buttonList.append(x)
        for button in self.buttonList:
            button.pack(fill=tk.X)
    def clickFood(self,food,master):
        tmpFood = Food(food) # need to convert dict into Food object
        self.refreshGraphs(tmpFood,master)
        #Tries to clear top frame before initializing food stats
        try:
            for x in self.topFrame.winfo_children():
                x.destroy()
        except: 
            Button(self.topFrame,text="Add Food",command=lambda x=food:self.addFood(x,master)).pack(side=BOTTOM)
            Label(self.topFrame,text=food['food_name'],font=('century gothic', '18'),bg='white').pack(side=TOP,fill=tk.BOTH,expand=1)
            Label(self.topFrame,text="Calories: " + str(food['calories']) + "\tProtein: " + str(food['protein']) + "\tCarbs: " + str(food['carb']) + "\tFat: " + str(food['fat']),font=('century gothic', '18'),bg='white').pack(fill=X,side=TOP)
        else:
            Button(self.topFrame,text="Add Food",command=lambda x=food:self.addFood(x,master)).pack(side=BOTTOM)
            Label(self.topFrame,text=food['food_name'],font=('century gothic', '18'),bg='white').pack(side=TOP,fill=tk.BOTH,expand=1)
            Label(self.topFrame,text="Calories: " + str(food['calories']) + "\tProtein: " + str(food['protein']) + "\tCarbs: " + str(food['carb']) + "\tFat: " + str(food['fat']),font=('century gothic', '18'),bg='white').pack(fill=X,side=TOP)

    def addFood(self,food,master):
        tmpFood = Food(food) #Convert food dict into Food Object
        if master.Profile.user != 'guest':
            data = {'name':master.Profile.user, 'food_name':food['food_name'], 'calories':food['calories'],'protein':food['protein'],'fat':food['fat'],'carb':food['carb'],'insert_date':master.instance_date} 
            y = json.dumps(data)
            url = CLOUDURL + "/edit/add"
            addRequest = requests.post(url,data=y,headers=HEADERS)
        master.Profile.addFood(tmpFood)
        for x in self.topFrame.winfo_children():
                x.destroy()
        self.clearGraph(master)
    def clearGraph(self,master):
        self.clear(self.figMacroCanvas)
        self.clear(self.figPieCanvas)
        self.clear(self.figCalCanvas)
        self.initCalPlot(None,master,self.bottomFrame)
        self.initMacroBar(None,master,self.bottomFrame)
        self.initPieGraph(None,master,self.bottomFrame)
        
    def initMacroBar(self,food,master,frame):
        #Figure containing plot
        FF6666=(255,102,102,)
        FFA152=(.255,.160,.82,)
        FFE666=(.255,.230,.102)
        figMacroPlot = Figure(figsize=(3,3.5))
        axe = figMacroPlot.add_subplot()
        if food is not None:
            axe.bar(["Protein","Carbs","Fats"],[master.Profile.getTotProtein(),master.Profile.getTotCarb(),master.Profile.getTotFat()],color=['#FF6666','#FF6666','#FF6666'],width=.6,bottom=0,label="Today's Macros")
            axe.bar(["Protein","Carbs","Fats"],[food.getProtein(),food.getCarb(),food.getFat()],bottom=[master.Profile.getTotProtein(),master.Profile.getTotCarb(),master.Profile.getTotFat()],width=.6,label="Food's Macros")
            axe.set_title("Macronutrients",fontsize=12,loc='left')
            axe.set_ylabel('Nutrients Consumed (g)',fontsize=8)
            axe.set_ylim(bottom=0)
            axe.legend()
        else:
            axe.bar(["Protein","Carbs","Fats"],[master.Profile.getTotProtein(),master.Profile.getTotCarb(),master.Profile.getTotFat()],color=['#FF6666','#FF6666','#FF6666'],width=.6,bottom=0,label="Today's Macros")
            axe.bar(["Protein","Carbs","Fats"],[0,0,0],bottom=[master.Profile.getTotProtein(),master.Profile.getTotCarb(),master.Profile.getTotFat()],width=.6,label="Food's Macros")
            axe.set_title("User's Macronutrients",fontsize=12,loc='left')
            axe.set_ylabel('Nutrients Consumed (g)',fontsize=8)
            axe.set_ylim(bottom=0)
            axe.legend()
        figMacroPlot.set_tight_layout(True)
        self.figMacroCanvas = FigureCanvasTkAgg(figMacroPlot, master=frame)
        self.figMacroCanvas.draw()
        self.figMacroCanvas.get_tk_widget().pack(side="right",fill=BOTH,expand=1)
    def initPieGraph(self,food,master,frame):
        figPieGraph = Figure(figsize=(3,3.5))
        axe = figPieGraph.add_subplot()
        if food is not None:
            if food.getCal() == 0:
                axe.pie([100],labels=["No Info Available"])
                axe.set_title("Macronutrients Pie Graph")
                axe.legend(loc="upper left")
            else:
                axe.pie([food.getProtein(),food.getCarb(),food.getFat()],labels=["Proteins","Carbs","Fats"],radius=.75)
                axe.set_title("Macronutrients of \n" + food.getFoodID())
                axe.legend()
        else:
            axe.pie([100],labels=["No Food Selected"])
            axe.set_title("Macronutrients Pie Graph")
        figPieGraph.set_tight_layout(True)
        self.figPieCanvas = FigureCanvasTkAgg(figPieGraph, master=frame)
        self.figPieCanvas.draw()
        self.figPieCanvas.get_tk_widget().pack(side="right",fill=BOTH,expand=1)
    def initCalPlot(self,food,master,frame):
        #Figure containing cal
        figCalPlot = Figure(figsize=(6,1.5))
        axe = figCalPlot.add_subplot()
        axe.barh([""],[master.Profile.getTotCal()],label="Calorie's Consumed" ,height = .005, color = '#52BE80')
        if food is not None:
            axe.barh([""],[food.getCal()],left=master.Profile.getTotCal(),label="Calories in " + food.getFoodID(),height = .005, color = 'yellow')
        else:
            axe.barh([""],[0],left=master.Profile.getTotCal(),height = .0005, color = 'yellow')
        axe.legend(loc='upper left')
        axe.set_ylabel("Calories (kj)")
        if master.Profile.calGoal is not None:
            axe.axvline(x=master.Profile.calGoal)
        else:
            axe.axvline(x=2000)
        axe.set_title("Calories Consumed")
        axe.set_xlim(0)
        figCalPlot.set_tight_layout(True)
        self.figCalCanvas = FigureCanvasTkAgg(figCalPlot, master=frame)
        self.figCalCanvas.draw()
        self.figCalCanvas.get_tk_widget().pack(fill=BOTH)
    def refreshGraphs(self,food,master):
        self.clear(self.figMacroCanvas)
        self.clear(self.figPieCanvas)
        self.clear(self.figCalCanvas)
        self.initCalPlot(food,master,self.bottomFrame)
        self.initMacroBar(food,master,self.bottomFrame)
        self.initPieGraph(food,master,self.bottomFrame)
    def clear(self,canvas):
        for item in canvas.get_tk_widget().find_all():
            canvas.get_tk_widget().pack_forget()
            canvas.get_tk_widget().delete(item)

class Profile():
    def __init__(self,user,master,calGoal):
        self.user = user.lower() #Username
        self.foodList = [] #Food List containing food from the sessions insert_date
        self.calGoal = None 
        self.weightGoal = None
        if user == 'Guest':
            self.calGoal = 2000
        elif calGoal is not None:
            self.calGoal = calGoal
        else:
            self.calGoal = 2000
        self.loadFood(master) 

    #Loads in food if user has already put in food
    def loadFood(self,master):
        self.clearFood()
        data = {"name":self.user,"instance_date":master.instance_date}
        y = json.dumps(data)
        url = CLOUDURL + "/diary/food"
        request = requests.post(url,data=y,headers=HEADERS)
        request = request.json()
        for dictionary in request:
            self.foodList.append(Food(dictionary))
    def clearFood(self):
        self.foodList.clear()
    def addFood(self,Food):
        self.foodList.append(Food)
    def getTotProtein(self):
        count = 0
        for x in self.foodList:
            count = count + x.getProtein()
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
    def __init__(self,dictionary):
        self.name = dictionary['food_name']
        self.cal = int(dictionary['calories'])
        self.fat = int(dictionary['fat'])
        self.carb = int(dictionary['carb'])
        self.protein = int(dictionary['protein'])
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

class ButtonBar(Frame):
    def __init__(self,frame,master):
        Frame.__init__(self,frame,bg="#6B081F")
        self.addButton = Button(self,text="Add Food",fg="white",bg="gray",height=3,command=lambda:master.switch_frame(frameFoodAdd))
        self.addButton.pack(side="right",expand=True,fill=tk.X)
        self.homeButton= Button(self,text="Home",height=3,bg="gray",fg="white",command=lambda:master.switch_frame(frameHome))
        self.homeButton.pack(side="left",expand=True,fill=tk.X)
        self.goals = Button(self,text="Edit Goals",height=3,bg="gray",fg="white",command=lambda:master.switch_frame(frameEditGoals))
        self.goals.pack(side="left",expand=True,fill=tk.X)
        self.diaryButton = Button(self,text="Food Diary",height=3,bg="gray",fg="white",command=lambda:master.switch_frame(frameDiary))
        self.diaryButton.pack(side="left",expand=True,fill=tk.X)
        if master.Profile.user == 'Guest':
            self.goals['state'] = 'disabled'
        #buttonBar.pack(side="bottom",fill=tk.X)
    
class frameEditGoals(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        Message(self,text="Edit Calorie Goal").pack()
        calorieGoal = Entry(self,width=30)
        calorieGoal.pack()
        calorieButton = Button(self,text="Save",command=lambda:self.setCalorieGoal(calorieGoal.get(),master)).pack()
        bar = ButtonBar(self,master)
        bar.pack(side='bottom',fill=tk.X)
        bar.goals['state'] = 'disabled'
        Message(self,text="Edit Weight Goal").pack()
        weightGoal = Entry(self,width=30)
        weightGoal.pack()
        weightSaveButton = Button(self,text="Save",command=lambda:self.setWeightGoal(weightGoal.get(),master)).pack()
        
    def setCalorieGoal(self,calorie,master):
        if master.Profile.user != 'guest':
            data = {'name':master.Profile.user,'goal_calorie':calorie}
            y = json.dumps(data)
            url = CLOUDURL + "/edit/goal_calorie"
            foodRequest = requests.post(url,data=y,headers=HEADERS)
        master.Profile.calGoal = int(calorie)

    ##implement guest weight goal LATER
    def setWeightGoal(self,calorie,master):
        if master.Profile.user != 'guest':
            data = {'name':master.Profile.user,'goal_weight':calorie}
            y = json.dumps(data)
            url = CLOUDURL + "/edit/goal_weight"
            foodRequest = requests.post(url,data=y,headers=HEADERS)
        master.Profile.weightGoal = int(calorie)

class frameDiary(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.buttonList = [] #contains the buttons for the food
        self.FoodList = [] #contains the food user has eaten for day
        self.LabelList = [] #Contains the labels for food consumed
        ###TOP ENTER CURRENT WEIGHT EDIT FRAME#
        Label(self,text="Your Diary:",bg="#6B081F",font=("Calibri",26),fg='white',anchor='w').pack(side='top',fill=tk.X)
        self.currentWeightFrame = Frame(self,bg="#6B081F")
        self.currentWeightFrame.pack(fill=tk.X,side='top')
        Label(self.currentWeightFrame,text="Enter Today's Weight:",bg="#6B081F",font=("Calibri",18),fg='white').pack(side='left',fill=tk.X,pady=(10,30))
        Entry(self.currentWeightFrame,width=10,justify='center',bg="white",font=("Calibri",15)).pack(side='left',pady=(10,30),padx=20)
        ###FOODLISTED FRAME BELOW
        self.foodListFrame = Frame(self,bg='white')
        self.foodListFrame.pack(fill=BOTH,expand=1,side='top')
        self.initSearchFrame(master,master.Profile.foodList)
        ###BOTTOM BAR 
        bar = ButtonBar(self,master)
        bar.pack(side="bottom",fill=tk.X)
        bar.diaryButton['state']='disable'
    def clearSearchFrame(self,master,frame):
        buttonCount = 0
        for button in self.buttonList:
            button.destroy()
        for label in self.LabelList:
            label.destroy()
        self.buttonList.clear()
        self.LabelList.clear()
        for widget in frame.winfo_children():
            widget.destroy()
    ##fills the foodListFrame with tmpFrames holding labels and buttons for food
    def initSearchFrame(self,master,foodList):
        Label(self.foodListFrame,text="Food Log:",fg="#6B081F",font=("Calibri",24,'bold','underline'),bg='white').pack(fill=tk.X,pady=(5,15))
        for food in foodList:
            tmpFrame = Frame(self.foodListFrame,bg='white')
            #buttonString = dictionary['food_name'].title() + "\tCalories: " + str(dictionary['calories']) + "\tProtein: " +  str(dictionary['protein']) + "g\t Fat: " + str(dictionary['fat']) + "g\t\tCarbohydrates: " + str(dictionary['carb']) + "g"
            buttonString = food.name.title() + "\t\tCalories: " + str(food.cal) + "\t\tProtein: " +  str(food.protein) + "g\t\t Fat: " + str(food.fat) + "g\t\tCarbohydrates: " + str(food.carb) + "g"         
            foodLabel = Label(tmpFrame,text=buttonString,anchor='w',font=('century gothic',10,'bold'),bg="white",fg="#6B081F")
            removeButton = Button(tmpFrame,text="Remove",bg="#6B081F",fg="white",command=lambda food=food.name:self.remove(food,master))
            self.buttonList.append(removeButton)
            self.LabelList.append(foodLabel)
            foodLabel.pack(side='left',fill=tk.X)
            removeButton.pack(side='right',fill=tk.X)
            tmpFrame.pack(fill=tk.X)
    def remove(self,food,master):
        if master.Profile.user != 'guest':
            data = {"name":master.Profile.user,"food_name":food,"insert_date":master.instance_date}
            y = json.dumps(data)
            url = CLOUDURL + "/diary/delete"
            request = requests.post(url,data=y,headers=HEADERS)
        self.removeFromList(food,master.Profile.foodList)
        self.reload(master,self.master.Profile.foodList)
    def removeFromList(self,food_name,food_list):
        for i in range(len(food_list)): 
            if food_list[i].name == food_name: 
                del food_list[i] 
                break
    def reload(self,master,foodList):
        self.clearSearchFrame(master,self.foodListFrame)
        self.initSearchFrame(master,foodList)
        
 #:) starting the app
if __name__ == "__main__":
    app = NutritionApp()
    app.mainloop(0)