import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import threading
import mysql.connector
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import time


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

        self.addButtonPhoto = PhotoImage(file='resources/redPlusButton.png')
        
            
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
        if master.Profile is None:
            master.Profile = Profile("Guest")
            guestAcc = True
        Frame.__init__(self,master,bg="#6B081F")
        Label(self,text=master.Profile.user + "'s Profile:",font=("Calibri",18),padx=5,pady=5,anchor='w').pack(side="top",expand=False,fill=tk.X)
        #matthews frame to design and develop
        userFrame = Frame(self,bg="gray")
        userFrame.pack(side="top",expand=1,fill=BOTH)
        #Put your code in this blank spot




        ####
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
        axe.bar(["Protein","Carbs","Fats"],[master.Profile.getTotCarb(),master.Profile.getTotFat(),master.Profile.getTotProtein()],color=['#FF6666','#FFA152','#FFE666'],width=.6,bottom=0)
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
        axe.axvline(x=master.Profile.calGoal)
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
        searchFrame = Frame(self,bg="gray")
        Button(searchFrame,text="Submit",bg="#6B081F",fg="white",command=lambda:self.addFoodSQL(master,self.search.get())).pack(side="left")
        self.search = Entry(searchFrame,width=100)
        self.search.pack(pady=25,fill=tk.Y,expand=1,side="left")
        searchFrame.pack(fill=tk.X)
        #bottom part -- bottom bar
        bar = ButtonBar(self,master)
        bar.pack(side="bottom",fill=tk.X)
        bar.addButton['state']='disable'
        #left hand result search barh
        self.resultFrame = Frame(self,bg="gray")
        Label(self.resultFrame,text="Results",width=5).pack(fill=tk.X)
        self.resultFrame.pack(side='left',fill=BOTH,expand=1,padx=(0,5))
        #right hand display plots
        self.displayFrame = Frame(self,bg="gray")
        self.displayFrame.pack(side='left',fill=BOTH,expand=1)
        self.topFrame = Frame(self.displayFrame,bg="gray")
        self.topFrame.pack(fill=BOTH,expand=1)
        Label(self.topFrame,text="Nutrition:").pack(fill=BOTH)
        ###DESIGN SPOT FOR MATTHEW###



        ###
        self.bottomFrame = Frame(self.displayFrame,bg="gray")
        self.bottomFrame.pack(fill=BOTH,expand=1)
        self.initCalPlot(None,master,self.bottomFrame)
        self.initMacroBar(None,master,self.bottomFrame)
        self.initPieGraph(None,master,self.bottomFrame)
        

    def addFoodSQL(self,master,food):
        master.establishCursor()
        master.cursor.execute("SELECT * FROM nutrition.Food WHERE name LIKE \'%" + food + "%\'")
        results = master.cursor.fetchall()
        self.initSearchFrame(master,results)
    def initSearchFrame(self,master,results):
        for line in results:
            self.buttonList.append(Button(self.resultFrame,text=line[0].title(),anchor='w',width=4,command=lambda food=line:self.clickFood(Food(food),master)))
        for button in self.buttonList:
            button.pack(fill=tk.X)
    def clickFood(self,food,master):
        self.refreshGraphs(food,master)
        try:
            self.topFrame.winfo_children()[1].destroy()
        except:
            Button(self.topFrame,text="Add Food",command=lambda:self.addFood(food,master)).pack()
        else:
            Button(self.topFrame,text="Add Food",command=lambda:self.addFood(food,master)).pack()
        self.topFrame.winfo_children()[1].destroy()
        Button(self.topFrame,text="Add Food",command=lambda:self.addFood(food,master)).pack()
    def addFood(self,food,master):
        master.Profile.addFood(food)
        self.topFrame.winfo_children()[1].destroy()
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
            axe.bar(["Protein","Carbs","Fats"],[master.Profile.getTotCarb(),master.Profile.getTotFat(),master.Profile.getTotProtein()],color=['#FF6666','#FFA152','#FFE666'],width=.6,bottom=0,label="Today's Macros")
            axe.bar(["Protein","Carbs","Fats"],[food.getProtein(),food.getCarb(),food.getFat()],bottom=[master.Profile.getTotCarb(),master.Profile.getTotFat(),master.Profile.getTotProtein()],width=.6,label="Food's Macros")
            axe.set_title("Macronutrients",fontsize=12,loc='left')
            axe.set_ylabel('Nutrients Consumed (g)',fontsize=8)
            axe.set_ylim(bottom=0)
            axe.legend()
        else:
            axe.bar(["Protein","Carbs","Fats"],[master.Profile.getTotCarb(),master.Profile.getTotFat(),master.Profile.getTotProtein()],color=['#FF6666','#FFA152','#FFE666'],width=.6,bottom=0,label="Today's Macros")
            axe.bar(["Protein","Carbs","Fats"],[0,0,0],bottom=[master.Profile.getTotCarb(),master.Profile.getTotFat(),master.Profile.getTotProtein()],width=.6,label="Food's Macros")
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
            axe.pie([food.getProtein(),food.getCarb(),food.getFat()],labels=["Proteins","Carbs","Fats"],radius=.75)
            axe.set_title("Macronutrients of " + food.getFoodID())
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
        axe.barh([""],[master.Profile.getTotCal()] ,height = .005, color = '#52BE80')
        if food is not None:
            axe.barh([""],[food.getCal()],left=master.Profile.getTotCal() ,height = .005, color = 'yellow')
        else:
            axe.barh([""],[0],left=master.Profile.getTotCal(),height = .0005, color = 'yellow')
        axe.set_ylabel("Calories (kj)")
        axe.axvline(x=master.Profile.calGoal)
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
    def __init__(self,user):
        self.user = user
        self.foodList = []
        self.calGoal = 1750
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

class ButtonBar(Frame):
    def __init__(self,frame,master):
        Frame.__init__(self,frame,bg="#6B081F")
        self.addButton = Button(self,text="Add Food",fg="white",bg="gray",height=3,command=lambda:master.switch_frame(frameFoodAdd))
        self.addButton.pack(side="right",expand=True,fill=tk.X)
        self.homeButton= Button(self,text="Home",height=3,bg="gray",fg="white",command=lambda:master.switch_frame(frameHome))
        self.homeButton.pack(side="left",expand=True,fill=tk.X)
        self.goals = Button(self,text="Edit Goals",height=3,bg="gray",fg="white")
        self.goals.pack(side="left",expand=True,fill=tk.X)
        self.diaryButton = Button(self,text="Food Diary",height=3,bg="gray",fg="white")
        self.diaryButton.pack(side="left",expand=True,fill=tk.X)
        #buttonBar.pack(side="bottom",fill=tk.X)
    
    
 #:) starting the app
if __name__ == "__main__":
    app = NutritionApp()
    app.mainloop(0)
       