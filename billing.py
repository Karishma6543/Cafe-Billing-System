from tkinter import *

import tkinter.ttk as ttk

import tkinter.messagebox as tkMessageBox

import PIL

from PIL import ImageTk

from PIL import Image 

from datetime import *

import sqlite3

import csv

import os

import tempfile

#================Front Page of Program=============

class Front:

    def __init__(self,window):

        #===================Font===================
        jls_extract_var = self
        jls_extract_var.font1=("cinzel",50,"bold")

        self.font2=("arial",24,"underline")

        self.font3=("bell mt",105,"bold")

        self.font4=("arial",18,"bold")

        #================Top Frame=========

        self.top=Frame(window,width=1366,height=120,bd=5,bg="#EEF5DB",relief=RAISED)

        self.top.propagate(0)

        self.top.place(x=0,y=0)

        #===================Main label=============

        self.l1=Label(self.top,text="CENTRAL PERK",font=self.font1,bg="#EEF5DB",bd=8,fg="#4B8BBE",justify=CENTER)

        self.l1.place(x=235,y=0)

        #=============Right Canvas==============

        self.right=Canvas(window,width=1366,height=520,bd=5,bg="#4F6367",relief=RAISED)

        self.image=ImageTk.PhotoImage(Image.open("2.jpg"))

        id=self.right.create_image(680,250,image=self.image)

        text=self.right.create_text(400,540,fill="#EEF5DB",font=("cinzel",27,"bold"),text="WELCOME TO CENTRAL PERK")

        self.right.place(x=0,y=220)

        #==================left  Frame============

        self.left=Frame(window,width=1366,height=100,bd=5,bg="#4F6367",relief=RAISED)

        self.left.propagate(0)

        self.left.place(x=0,y=120)

        #=====================button=============

        self.button1=Button(self.left,text="BILL COUNTER",width=15,height=3,bd=8,bg="#4F6367",

                            fg="#EEF5DB",command=self.call)

        self.button1.place(x=450,y=10)

        self.button2=Button(self.left,text="CALCULATOR",width=15,height=3,bd=8,bg="#4F6367",

                            fg="#EEF5DB",command=self.cal)

        self.button2.place(x=900,y=10)

        self.button3=Button(self.left,text="EXIT",width=15,height=3,bd=8,bg="#4F6367",

                            fg="#EEF5DB",command=self.exit)

        self.button3.place(x=1200,y=10)

        self.button4=Button(self.left,text="ABOUT US",width=15,height=3,bd=8,

                            bg="#4F6367",fg="#EEF5DB",command=self.aboutus)

        self.button4.place(x=1050,y=10)

        self.button5=Button(self.left,text="MENU",width=15,height=3,bd=8,bg="#4F6367",

                            fg="#EEF5DB",command=self.rate)

        self.button5.place(x=600,y=10)

        self.button6=Button(self.left,text="SEARCH BILL",width=15,height=3,bd=8,bg="#4F6367",

                            fg="#EEF5DB",command=self.sum)

        self.button6.place(x=750,y=10)

    #======================Calculator==============

    def cal(self):

        root=Tk()

        obj=Calc(root)

        root.title("calculator")

        root.mainloop()

    #===============================Exit Button===============

    def exit(self):

        window.destroy()

    #=====================Restra class calliing==============

    def call(self):

        window.destroy()

        root=Tk()

        obj1=Restra(root)

        root.title("CENTRAL PERK")

        root.geometry("1366x768")

        root.configure(background="#EEF5DB")

        root.mainloop()

    def sum(self):

        root=Tk()

        obj1=Bill(root)

        root.configure(background="#EEF5DB")

        root.mainloop

    def rate(self):

        var=Tk()

        obj=Menu(var)

        var.title("MENU")

        var.mainloop()

    def aboutus(self):

        window=Tk()

        obj5=About(window)

        window.title("ABOUT US")

        window.geometry("1366x768")

        window.mainloop


#==================new class========================

class Restra(Front):

    def __init__(self,root):

        #===================Font===================

        self.font1=("cinzel",50,"bold")

        self.font2=("arial",24,"bold")

        self.font3=("bell mt",105,"bold")

        self.font4=("arial",18,"bold")

        #============================Frame=========================

        self.top=Frame(root,width=1366,height=120,bd=5,bg="#EEF5DB",relief=RAISED)

        self.top.propagate(0)

        self.top.place(x=0,y=0)

        #===================Main label=============

        self.l1=Label(self.top,text="CENTRAL PERK",font=self.font1,

                        bg="#EEF5DB",bd=8,fg="#FE5F55",justify=CENTER)

        self.l1.place(x=235,y=0)

        #====================Menu=================

        self.menu=Frame(root,width=760,height=350,bd=5,bg="#4F6367",relief=RAISED,

                        cursor="arrow")

        self.menu.place(x=0,y=120)

        #================Billing Menu=============

        self.l11=Label(self.menu,text="DISH",font=("bell",18,"bold"),

                       bg="#4F6367",fg="#EEF5DB")

        self.l11.place(x=40,y=0)


        self.l9=Label(self.menu,text="SELECT DISH",font=("bell MT",18,"bold"),

                      bg="#4F6367",fg="#EEF5DB")

        self.l9.place(x=260,y=0)

        self.l10=Label(self.menu,text="QTN",font=("bell MT",18,"bold"),

                      bg="#4F6367",fg="#EEF5DB")

        self.l10.place(x=520,y=0)

        self.l5=Label(self.menu,text="SNACKS=",font=("bell MT",18,"bold"),

                      bg="#4F6367",fg="#EEF5DB")

        self.l5.place(x=40,y=50)

        self.l6=Label(self.menu,text="SOUPS & SALADS=",font=("bell MT",18,"bold"),

                      bg="#4F6367",fg="#EEF5DB")

        self.l6.place(x=40,y=100)

        self.l7=Label(self.menu,text="BAKERY SWEETS=",font=("bell MT",18,"bold"),

                      bg="#4F6367",fg="#EEF5DB")

        self.l7.place(x=40,y=150)

        self.l8=Label(self.menu,text="DESERTS=",font=("bell MT",18,"bold"),

                      bg="#4F6367",fg="#EEF5DB")

        self.l8.place(x=40,y=200)

        self.l9=Label(self.menu,text="BEVERAGES=",font=("bell MT",18,"bold"),

                      bg="#4F6367",fg="#EEF5DB")

        self.l9.place(x=40,y=250)

        #=================ENTRY=============

        self.q1=Entry(self.menu,bd=5,width=15)

        self.q1.place(x=500,y=50)

        self.q2=Entry(self.menu,bd=5,width=15)

        self.q2.place(x=500,y=100)

        self.q3=Entry(self.menu,bd=5,width=15)

        self.q3.place(x=500,y=150)

        self.q4=Entry(self.menu,bd=5,width=15)

        self.q4.place(x=500,y=200)

        self.q5=Entry(self.menu,bd=5,width=15)

        self.q5.place(x=500,y=250)

        #==============Dish Name============

        self.ddvar1=StringVar()

        self.method1={"CHEESE GRILLED SANDWICH","CHILLI CHEESE MOMOS","NOODLE FRANKIE","CHEESE BURST PIZZA",

                      "FRENCH FRIES","CHEESE BURGER","RED SAUCE PASTA","NACHOS"}

        self.ddvar1.set("CHEESE GRILLED SANDWICH")

        self.dropdowm1=OptionMenu(self.menu,self.ddvar1,*self.method1)

        self.dropdowm1.place(x=260,y=50)

        self.ddvar2=StringVar()

        self.method2={"GREEN SALAD","CLASSIC GREEK SALAD","BROCOLLI SPROUT SALAD","GLAZED CARROT SALAD",

                      "MANCHURIAN SOUP","WHEAT CORN SOUP","MANCHOW SOUP"}

        self.ddvar2.set("GREEN SALAD")

        self.dropdowm2=OptionMenu(self.menu,self.ddvar2,*self.method2)

        self.dropdowm2.place(x=260,y=100)

        self.ddvar3=StringVar()

        self.method3={"PASTERY","CREAM ROLL","COOKIE","DOUGHNUT",

                        "MUFFIN","PANCAKE"}

        self.ddvar3.set("PASTERY")

        self.dropdowm3=OptionMenu(self.menu,self.ddvar3,*self.method3)

        self.dropdowm3.place(x=260,y=150)

        self.ddvar4=StringVar()

        self.method4={"CHOCOLATE ICE CREAM","FRUIT SALAD","HOT CHOCOLATE BROWNIE","STRAWBERRY SUNDAE","NUTELLA BELLA",

                        "WAFFLE"}

        self.ddvar4.set("CHOCOLATE ICE CREAM")

        self.dropdowm4=OptionMenu(self.menu,self.ddvar4,*self.method4)

        self.dropdowm4.place(x=260,y=200)

        self.ddvar5=StringVar()

        self.method5={"COLD COFFEE","CAPPUCCINO","MOJITO","SMOOTIE"}

        self.ddvar5.set("COLD COFFEE")

        self.dropdowm5=OptionMenu(self.menu,self.ddvar5,*self.method5)

        self.dropdowm5.place(x=260,y=250)

        #=============================================

        #======================Button=================

        #=============================================

        self.add1=Button(self.menu,text="ADD",width=5,height=1,bd=6,bg="#4F6367",

                            fg="#EEF5DB",command=self.vgadd)

        self.add1.place(x=650,y=50)

        self.add2=Button(self.menu,text="ADD",width=5,height=1,bd=6,bg="#4F6367",

                            fg="#EEF5DB",command=self.nvgadd)

        self.add2.place(x=650,y=95)

        self.add3=Button(self.menu,text="ADD",width=5,height=1,bd=6,bg="#4F6367",

                            fg="#EEF5DB",command=self.sweadd)

        self.add3.place(x=650,y=145)

        self.add4=Button(self.menu,text="ADD",width=5,height=1,bd=6,bg="#4F6367",

                            fg="#EEF5DB",command=self.dadd)

        self.add4.place(x=650,y=195)

        self.add5=Button(self.menu,text="ADD",width=5,height=1,bd=6,bg="#4F6367",

                         fg="#EEF5DB",command=self.roadd)

        self.add5.place(x=650,y=245)

        #======================================================

        #==============================button==================

        #======================================================

        self.button=Frame(root,width=120,height=240,bd=5,bg="#4F6367",relief=RAISED)

        self.button.propagate(0)

        self.button.place(x=760,y=120)

        #====================button==================

        self.menu=Button(self.button,text="MENU",width=13,height=4,bd=5,bg="#4F6367",

                            fg="#EEF5DB",command=self.rate)

        self.menu.place(x=0,y=-2)

        self.cal=Button(self.button,text="CALCULATOR",width=13,height=4,bd=5,bg="#4F6367",

                            fg="#EEF5DB",command=self.cal)

        self.cal.place(x=0,y=73)

        self.search=Button(self.button,text="RESET",width=13,height=4,bd=5,bg="#4F6367",

                           fg="#EEF5DB",command=self.reset)

        self.search.place(x=0,y=150)

        #==============================================

        #===================customer detials===========

        #=====================left Frame===============

        self.left=Frame(root,width=490,height=220,bd=5,bg="#4F6367",relief=RAISED)

        self.left.place(x=870,y=120)

        #=====================label====================

        self.labelcd=Label(self.left,text="CUSTOMER INFORMATION",bg="#4F6367",

                           font=self.font2,fg="#EEF5DB")

        self.labelcd.place(x=0,y=20)

        self.labelcn=Label(self.left,text="CUSTOMER NAME:-",bg="#4F6367",

                           font=self.font4,fg="#EEF5DB")

        self.labelcn.place(x=0,y=80)

        self.labelcm=Label(self.left,text="BILL NUMBER:-",bg="#4F6367",

                           font=self.font4,fg="#EEF5DB")

        self.labelcm.place(x=0,y=120)

        self.labelpm=Label(self.left,text="PAYMENT METHOD:-",bg="#4F6367",

                           font=self.font4,fg="#EEF5DB")

        self.labelpm.place(x=0,y=160)

        #==================Entry Box==================

        self.entry1=Entry(self.left,width=25,bd=3)

        self.entry1.place(x=260,y=85)

        self.entry2=Entry(self.left,width=25,bd=3)

        self.entry2.place(x=260,y=125)

        #===============dropdown menu===============

        self.ddvar=StringVar()

        self.method={"By Cash","By Card","By UPI"}

        self.ddvar.set("By cash")

        self.dropdowm=OptionMenu(self.left,self.ddvar,*self.method)

        self.dropdowm.place(x=260,y=165)


        #======================================================

        #=============================Bill=====================

        #======================================================

        self.bill=Frame(root,width=760,height=270,bd=5,bg="#4f6367",relief=RAISED)

        self.bill.propagate(0)

        self.bill.place(x=0,y=470)

        #================Recipt=============

        self.label1=Label(self.bill,text="SUB TOTAL=",font=self.font2,bg="#4F6367",fg="#EEF5DB")

        self.label1.place(x=20,y=10)

        self.sb=Entry(self.bill,bd=5,width=8)

        self.sb.place(x=230,y=18)

        self.sb.insert(END,int(0))

        self.label2=Label(self.bill,text="TAX=",font=self.font2,bg="#4F6367",fg="#EEF5DB")

        self.label2.place(x=330,y=10)

        self.tax=Entry(self.bill,bd=5,width=8)

        self.tax.place(x=420,y=18)

        self.label3=Label(self.bill,text="TOTAL=",font=self.font2,bg="#4F6367",fg="#EEF5DB")

        self.label3.place(x=520,y=10)

        self.total=Entry(self.bill,bd=5,width=8)

        self.total.place(x=660,y=18)

        self.L1=Label(self.bill,text=" ",

                      font=("cooper",17,"italic"),bg="#4F6367",fg="#EEF5DB")

        self.L1.place(x=10,y=140)

        #==================button=========

        self.button1=Button(self.bill,text="TOTAL",width=20,height=3,bd=6,bg="#4F6367",

                            fg="#EEF5DB",command=self.tot)

        self.button1.place(x=20,y=70)

        self.button2=Button(self.bill,text="SEARCH BILL",width=20,height=3,bd=6,bg="#4F6367",

                            fg="#EEF5DB",command=self.sum)

        self.button2.place(x=200,y=70)

        self.button3=Button(self.bill,text="SHOW RECIPT",width=20,height=3,bd=6,bg="#4F6367",

                            fg="#EEF5DB",command=self.insert)

        self.button3.place(x=390,y=70)

        self.button4=Button(self.bill,text="PRINT",width=20,height=3,bd=6,bg="#4F6367",

                            fg="#EEF5DB",command=self.prt)

        self.button4.place(x=580,y=70)


        #======================================================

        #==========================recipt======================

        #======================================================

        self.recipt=Frame(root,width=600,height=400,bd=20,bg="#4F6367",relief=RAISED)

        self.recipt.propagate()

        self.recipt.place(x=760,y=340)

        self.ric=Text(self.recipt,width=42,height=12,font=("arial",18,"bold"),relief=RAISED)

        self.ric.place(x=2,y=5)

        self.ric.insert(END,str("DESCRIPTION              QTY   RATE    AMOUNT"))

        self.scrollbar=Scrollbar(self.recipt)

        self.scrollbar.place(x=532,y=270)

        self.scrollbar.configure(command=self.ric.yview)

        self.ric.configure(yscrollcommand=self.scrollbar.set)
        

    #========================Function===================

    def reset(self):

        self.ric.delete("1.0",END)

        self.ric.insert(END,str("DESCRIPTION              QTY   RATE    AMOUNT"))

        self.q1.delete("0",END)

        self.q2.delete("0",END)

        self.q3.delete("0",END)

        self.q4.delete("0",END)

        self.q5.delete("0",END)

        self.sb.delete("0",END)

        self.sb.insert(END,int("0"))

        self.entry1.delete("0",END)

        self.entry2.delete("0",END)

        self.total.delete("0",END)

        self.tax.delete("0",END)
        
        

    def vgadd(self):

        str1=str(self.ddvar1.get())

        str2=str(self.q1.get())

        str3=int(self.sb.get())

        if str2=="":

            result=tkMessageBox.showwarning('WARNING', 'Please Enter The Dish Qut.', icon="warning")

        else:

            str2=int(self.q1.get())

            val1=str(self.q1.get())

            if str1=="CHEESE GRILLED SANDWICH":

                self.sb.delete('0',END)

                result=str2*250+str3

                self.sb.insert(END,int(result))

                num1=str2*250

                num1=str(num1)

                self.ric.insert(END,str("\nCHEESE GRILLED SANDWICH"+val1+"       100          "+num1))
                

            elif str1=="CHEESE BURST PIZZA":

                self.sb.delete('0',END)

                result=str2*220+str3

                self.sb.insert(END,int(result))

                num2=str2*220

                num2=str(num2)

                self.ric.insert(END,str("\nCHEESE BURST PIZZA "+val1+"        160         "+num2))

            elif str1=="CHEESE BURGER":

                self.sb.delete('0',END)

                result=str2*120+str3

                self.sb.insert(END,int(result))

                num3=str2*120

                num3=str(num3)

                self.ric.insert(END,str("\nCHEESE BURGER         "+val1+"       120         "+num3))

            elif str1=="FRENCH FRIES":

                self.sb.delete('0',END)

                result=str2*250+str3

                self.sb.insert(END,int(result))

                num4=str2*250

                num4=str(num4)

                self.ric.insert(END,str("\nFRENCH FRIES             "+val1+"       110         "+num4))

            elif str1=="NOODLE FRANKIE":

                self.sb.delete('0',END)

                result=str2*320+str3

                self.sb.insert(END,int(result))

                num5=str2*320

                num5=str(num5)

                self.ric.insert(END,str("\nNOODLE FRANKIE        "+val1+"       100          "+num5))

            elif str1=="RED SAUCE PASTA":

                self.sb.delete('0',END)

                result=str2*160+str3

                self.sb.insert(END,int(result))

                num6=str2*160

                num6=str(num6)

                self.ric.insert(END,str("\nRED SAUCE PASTA      "+val1+"       200          "+num6))

            elif str1=="CHILLI CHEESE MOMOS":

                self.sb.delete('0',END)

                result=str2*320+str3

                self.sb.insert(END,int(result))

                num7=str2*320

                num7=str(num7)

                self.ric.insert(END,str("\nCHILLI CHEESE MOMOS"+val1+"        190         "+num7))

            elif str1=="NACHOS":

                self.sb.delete('0',END)

                result=str2*180+str3

                self.sb.insert(END,int(result))

                num8=str2*180

                num8=str(num8)

                self.ric.insert(END,str("\nNACHOS                        "+val1+"       180          "+num8))

    def nvgadd(self):

        str1=str(self.ddvar2.get())

        str2=str(self.q2.get())

        str3=int(self.sb.get())
        

        if str2=="":

            result=tkMessageBox.showwarning('WARNING','Please Enter the Quantity',icon="warning")

        else:

            str2=int(self.q2.get())

            val2=str(self.q2.get())

            if str1=="GREEN SALAD":

                self.sb.delete('0',END)

                result=str2*250+str3

                self.sb.insert(END,int(result))

                num1=str2*200

                num1=str(num1)

                self.ric.insert(END,str("\nGREEN SALAD              "+val2+"       200          "+num1))

            elif str1=="CLASSIC GREEK SALAD":

                self.sb.delete('0',END)

                result=str2*220+str3

                self.sb.insert(END,int(result))

                num2=str2*220

                num2=str(num2)

                self.ric.insert(END,str("\nCLASSIC GREEK SALAD "+val2+"    220          "+num2))

            elif str1=="BROCOLLI SPROUT SALAD":

                self.sb.delete('0',END)

                result=str2*120+str3

                self.sb.insert(END,int(result))

                num3=str2*120

                num3=str(num3)

                self.ric.insert(END,str("\nBROCOLLI SPROUT SALAD  "+val2+"       250          "+num3))

            elif str1=="GLAZED CARROT SALAD":

                self.sb.delete('0',END)

                result=str2*250+str3

                self.sb.insert(END,int(result))

                num4=str2*250

                num4=str(num4)

                self.ric.insert(END,str("\nGLAZED CARROT SALAD"+val2+"    210          "+num4))

            elif str1=="MANCHURIAN SOUP":

                self.sb.delete('0',END)

                result=str2*320+str3

                self.sb.insert(END,int(result))

                num5=str2*320

                num5=str(num5)

                self.ric.insert(END,str("\nMANCHURIAN SOUP     "+val2+"       130          "+num5))

            elif str1=="WHEAT CORN SOUP":

                self.sb.delete('0',END)

                result=str2*160+str3

                self.sb.insert(END,int(result))

                num6=str2*160

                num6=str(num6)

                self.ric.insert(END,str("\nWHEAT CORN SOUP     "+val2+"      100          "+num6))

            elif str1=="MANCHOW SOUP":

                self.sb.delete('0',END)

                result=str2*320+str3

                self.sb.insert(END,int(result))

                num7=str2*320

                num7=str(num7)

                self.ric.insert(END,str("\nMANCHOW SOUP        "+val2+"        160         "+num7))

    def dadd(self):

        str1=str(self.ddvar4.get())

        str2=str(self.q4.get())

        str3=int(self.sb.get())

        if str2=="":

            result=tkMessageBox.showwarning('WARNING','Please Enter the Quantity',icon="warning")

        else:

            str2=int(self.q4.get())

            val4=str(self.q4.get())

            if str1=="CHOCOLATE ICE CREAM":

                self.sb.delete('0',END)

                result=str2*25+str3

                self.sb.insert(END,int(result))

                num1=str2*25

                num1=str(num1)

                self.ric.insert(END,str("\nCHOCOLATE ICE CREAM"+val4+"      90             "+num1))

            elif str1=="FRUIT SALAD":

                self.sb.delete('0',END)

                result=str2*40+str3

                self.sb.insert(END,int(result))

                num2=str2*40

                num2=str(num2)

                self.ric.insert(END,str("\nFRUIT SALAD                 "+val4+"         99            "+num2))

            elif str1=="HOT CHOCOLATE BROWNIE":

                self.sb.delete('0',END)

                result=str2*10+str3

                self.sb.insert(END,int(result))

                num3=str2*10

                num3=str(num3)

                self.ric.insert(END,str("\nHOT CHOCOLATE BROWNIE"+val4+" 95             "+num3))

            elif str1=="STRAWBERRY SUNDAE":

                self.sb.delete('0',END)

                result=str2*25+str3

                self.sb.insert(END,int(result))

                num4=str2*25

                num4=str(num4)

                self.ric.insert(END,str("\nSTRAWBERRY SUNDAE"+val4+"        80             "+num4))

            elif str1=="NUTELLA BELLA":

                self.sb.delete('0',END)

                result=str2*15+str3

                self.sb.insert(END,int(result)) 

                num5=str2*15

                num5=str(num5)

                self.ric.insert(END,str("\nNUTELLA BELLA           "+val4+"        60             "+num5))

            elif str1== "WAFFLE":

                self.sb.delete('0',END)

                result=str2*40+str3

                self.sb.insert(END,int(result))

                num6=str2*40

                num6=str(num6)

                self.ric.insert(END,str("\nWAFFLE                         "+val4+"         50             "+num6))

    def sweadd(self):

            str1=str(self.ddvar3.get())

            str2=str(self.q3.get())

            str3=int(self.sb.get())

            if str2=="":

                result=tkMessageBox.showwarning('WARNING','Please Enter the Quantity',icon="warning")

            else:

                str2=int(self.q3.get())

                val3=str(self.q3.get())

                if str1=="PASTERY":

                    self.sb.delete('0',END)

                    result=str2*10+str3

                    self.sb.insert(END,int(result))

                    num1=str2*10

                    num1=str(num1)

                    self.ric.insert(END,str("\nPASTERY                       "+val3+"        60             "+num1))    

                elif str1=="CREAM ROLL":

                    self.sb.delete('0',END)

                    result=str2*20+str3

                    self.sb.insert(END,int(result))

                    num2=str2*20

                    num2=str(num2)

                    self.ric.insert(END,str("\nCREAM ROLL                "+val3+"        40             "+num2))

                elif str1=="COOKIE":

                    self.sb.delete('0',END)

                    result=str2*25+str3

                    self.sb.insert(END,int(result))

                    num3=str2*25

                    num3=str(num3)

                    self.ric.insert(END,str("\nCOOKIE                          "+val3+"         75             "+num3))

                elif str1=="DOUGHNUT":

                    self.sb.delete('0',END)

                    result=str2*40+str3

                    self.sb.insert(END,int(result))

                    num4=str2*40

                    num4=str(num4)

                    self.ric.insert(END,str("\nDOUGHNUT                    "+val3+"        80             "+num4))

                elif str1=="MUFFIN":

                    self.sb.delete('0',END)

                    result=str2*15+str3

                    self.sb.insert(END,int(result))

                    num5=str2*15

                    num5=str(num5)

                    self.ric.insert(END,str("\nMUFFIN                          "+val3+"        75             "+num5))

                elif str1=="PANCAKE":

                    self.sb.delete('0',END)

                    result=str2*20+str3

                    self.sb.insert(END,int(result))

                    num6=str2*20

                    num6=str(num6)

                    self.ric.insert(END,str("\nPANCAKE                      "+val3+"        85             "+num6))

    def roadd(self):

        str1=str(self.ddvar5.get())

        str2=str(self.q5.get())

        str3=int(self.sb.get())

        val5=str(self.q5.get())

        if str2=="":

            result=tkMessageBox.showwarning('WARNING', 'Please Enter The Dish Qut.', icon="warning")

        else:

            str2=int(self.q5.get())

            if str1=="COLD COFFEE":

                self.sb.delete('0',END)

                result=str2*8+str3

                self.sb.insert(END,int(result))

                num1=str2*8

                num1=str(num1)

                self.ric.insert(END,str("\nCOLD COFFEE               "+val5+"           80               "+num1))

            elif str1=="CAPPUCCINO":

                self.sb.delete('0',END)

                result=str2*12+str3

                self.sb.insert(END,int(result))

                num2=str2*12

                num2=str(num2)

                self.ric.insert(END,str("\nCAPPUCCINO                 "+val5+"        120             "+num2))

            elif str1=="MOJITO":

                self.sb.delete('0',END)

                result=str2*25+str3

                self.sb.insert(END,int(result))

                num3=str2*25

                num3=str(num3)

                self.ric.insert(END,str("\nMOJITO                           "+val5+"         80             "+num3))
                

            elif str1=="SMOOTIE":

                self.sb.delete('0',END)

                result=str2*40+str3

                self.sb.insert(END,int(result))

                num4=str2*25

                num4=str(num4)

                self.ric.insert(END,str("\nSMOOTIE                        "+val5+"         95             "+num4))

    def tot(self):

        str1=int(self.sb.get())

        result=(str1*3)/100

        fin=result+result+str1

        self.tax.delete('0',END)

        self.total.delete('0',END)

        self.tax.insert(END,int(result))

        self.total.insert(END,int(fin))





    def insert(self):

        myconn=sqlite3.connect("restra.db")

        with myconn:

                cursor=myconn.cursor()

                cursor.execute("""SELECT COUNT(ID) FROM COMPANY;""")

                fetch = cursor.fetchone()

        myconn.commit()

        str8=str(self.ric.get('1.0', END))

        self.ric.delete('1.0',END)

        str1=str(self.entry1.get())

        str3=str(self.total.get())

        str4=str(self.ddvar.get())

        str5=str(date.today())

        now=datetime.now()

        current=now.strftime("%H:%M")

        str6=str(current)

        str7=str(self.tax.get())

        self.entry2.delete('0',END)

        self.entry2.insert(END,(fetch))

        str10=int(self.entry2.get())

        str10=str10+1

        if str1=="":

            result=tkMessageBox.showwarning('WARNING', 'Please Enter the Customer Name', icon="warning")

        elif set('1234567890').intersection(str1):

            result=tkMessageBox.showwarning('WARNING', 'Customer Name Cannot be in Number', icon="warning")

        elif set('!@#$%^&*)(_+=-}{][|/;,.><:').intersection(str1):

            result=tkMessageBox.showwarning('WARNING', 'Customer Name Cannot be in charater', icon="warning")
            

        elif str3=="":

            result=tkMessageBox.showwarning('WARNING', 'Please Calculate the bill', icon="warning")

        else:

            str10=str(str10)

            self.entry2.delete('0',END)

            self.entry2.insert(END,str(str10))

            self.ric.insert(END,str("\t     CENTRAL PERK"))

            self.ric.insert(END,str("\n\tGSTIN/UIN:05AAACS8577K1ZV "))

            self.ric.insert(END,str("\n\tState Name: Maharashtra Code:5"))

            self.ric.insert(END,str("\n\tE-Mail:centralperk@gmail.com"))

            self.ric.insert(END,str("\n\t\tPOS INVOICE"))

            self.ric.insert(END,str("\n\tBill No.:"+str10+"\t\t Time :"+str6))

            self.ric.insert(END,str("\n\tDate    :"+str5+"\t  Name : "+str1))

            self.ric.insert(END,str("\n"+str8))

            self.ric.insert(END,str("\n\t\t\tCGST\t"+str7))

            self.ric.insert(END,str("\n\t\t\tSGST\t"+str7))

            self.ric.insert(END,str("\n\t\t\tTotal\t"+str3))

            self.ric.insert(END,str("\n_________________________________________"))

            self.ric.insert(END,str("\n\tTOTAL Paid:"+str3))

            self.ric.insert(END,str("\n________________________________________"))

            self.ric.insert(END,str("\n\t7684209211\t\tE&OE"))

            self.ric.insert(END,str("\n\tYour Satisfaction is Ours"))

            text=self.ric.get("1.0",END)

            myconn1=sqlite3.connect("restra.db")

            with myconn1:

                cursor1=myconn1.cursor()

                cursor1.execute("""CREATE TABLE IF NOT EXISTS COMPANY(

                                      ID INT PRIMARY KEY  NOT NULL,

                                      NAME         TEXT   NOT NULL,

                                      BILL CHAR(9999) NOT NULL);""")

                cursor1.execute("INSERT INTO COMPANY(ID,NAME,BILL) VALUES(?,?,?)",(str10,str1,text))

            myconn1.commit()




    def prt(self):

        str1=self.ric.get('1.0',END)

        file=tempfile.mktemp(".txt")

        open(file,"w").write(str1)

        os.startfile(file,"print")
       

    def cal(self):

        root=Tk()

        obj=Calc(root)

        root.title("calculator")

        root.mainloop()

    def rate(self):

        var=Tk()

        obj=Menu(var)

        var.title("MENU")

        var.mainloop()
    



#====================================================

#=========================MENU=======================

#====================================================

class Menu:

    def __init__(self,root):

        #===================Font===================

        self.font1=("cinzel",50,"bold")

        self.font2=("arial",18,"bold","underline")

        self.font3=("bell mt",105,"bold")

        self.font4=("arial",14)

        self.font5=("arial",14,"bold")

        #===================FRAME===================

        self.menu=Frame(root,width=1366,height=720,bg="#4F6367")

        self.menu.propagate()

        self.menu.pack()


        #======================TOP===================

        self.top=Frame(root,width=1366,height=120,bd=5,bg="#EEF5DB",relief=RAISED)

        self.top.propagate(0)

        self.top.place(x=0,y=0)

        #===================Main label=============

        self.l1=Label(self.top,text="CENTRAL PERK",font=self.font1,

                      bg="#EEF5DB",bd=8,fg="#FE5F55",justify=CENTER)

        self.l1.place(x=235,y=0)

        #=================SNACKS MENU=================

        self.SNACKS=Frame(root,width=683,height=300,bd=5,bg="#4F6367",relief=RAISED)

        self.SNACKS.propagate(0)

        self.SNACKS.place(x=0,y=120)

        self.lab1=Label(self.SNACKS,text="SNACKS",font=self.font2,

                        width=15,bg="#4F6367",bd=8,fg="#EEF5DB",justify=CENTER)

        self.lab1.place(x=250,y=10)

        self.dish=Label(self.SNACKS,text="DISH\t\t\t RATE  DISH \t\t RATE",font=self.font5,bg="#4F6367",

                        fg="#EEF5DB",justify=RIGHT)

        self.dish.place(x=30,y=50)

        self.lb1=Label(self.SNACKS,text="CHEESE GRILLED SANDWICH 100     CHILLI CHEESE MOMOS 190",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb1.place(x=30,y=80)

        self.lb2=Label(self.SNACKS,text="CHEESE BURST PIZZA\t 160      NACHOS\t 180",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb2.place(x=30,y=110)

        self.lb3=Label(self.SNACKS,text="CHEESE BURGER\t\t 120",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb3.place(x=30,y=140)

        self.lb4=Label(self.SNACKS,text="FRENCH FRIES\t\t 110",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb4.place(x=30,y=170)

        self.lb5=Label(self.SNACKS,text="NOODLE FRANKIE\t\t 100",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb5.place(x=30,y=200)

        self.lb6=Label(self.SNACKS,text="RED SAUCE PASTA\t 200",font=self.font4,bg="#4F6367",

                        fg="#EEF5DB",justify=RIGHT)

        self.lb6.place(x=30,y=230)

        #=================SOUPS & SALADS MENU=================

        self.soupsalads=Frame(root,width=683,height=300,bd=5,bg="#4F6367",relief=RAISED)

        self.soupsalads.propagate(0)

        self.soupsalads.place(x=0,y=420)

        self.lab2=Label(self.soupsalads,text="SOUPS & SALADS",font=self.font2,

                        width=15,bg="#4F6367",bd=8,fg="#EEF5DB",justify=CENTER)

        self.lab2.place(x=190,y=10)

        self.dish=Label(self.soupsalads,text="DISH\t\t\t RATE  DISH \t\t RATE",font=self.font5,bg="#4F6367",

                        fg="#EEF5DB",justify=RIGHT)

        self.dish.place(x=30,y=50)

        self.lb1=Label(self.soupsalads,text="GREEN SALAD\t\t 200      MANCHOW SOUP\t 160",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb1.place(x=30,y=80)

        self.lb2=Label(self.soupsalads,text="CLASSIC GREEK SALAD\t 220",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb2.place(x=30,y=110)

        self.lb3=Label(self.soupsalads,text="BROCOLLI SPROUT SALAD\t 250",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb3.place(x=30,y=140)

        self.lb4=Label(self.soupsalads,text="GLAZED CARROT SALAD\t 210",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb4.place(x=30,y=170)

        self.lb5=Label(self.soupsalads,text="MANCHURIAN SOUP\t 130",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb5.place(x=30,y=200)

        self.lb6=Label(self.soupsalads,text="WHEAT CORN SOUP\t 100",font=self.font4,bg="#4F6367",

                        fg="#EEF5DB",justify=RIGHT)

        self.lb6.place(x=30,y=230)

        #=================BAKERY SWEETS===================

        self.swee=Frame(root,width=675,height=200,bd=5,bg="#4F6367",relief=RAISED)

        self.swee.propagate(0)

        self.swee.place(x=683,y=120)

        self.lab3=Label(self.swee,text="BAKERY SWEETS",font=self.font2,

                        width=15,bg="#4F6367",bd=8,fg="#EEF5DB",justify=CENTER)

        self.lab3.place(x=170,y=10)

        self.dish=Label(self.swee,text="DISH\t\t RATE  DISH \t\t RATE",font=self.font5,bg="#4F6367",

                        fg="#EEF5DB",justify=RIGHT)

        self.dish.place(x=30,y=50)

        self.lb1=Label(self.swee,text="PASTERY\t 60      COOKIE\t\t 75",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb1.place(x=30,y=80)

        self.lb2=Label(self.swee,text="CREAM ROLL\t 40       DOUGHNUT\t\t 80",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb2.place(x=30,y=110)

        self.lb3=Label(self.swee,text="MUFFIN\t\t 75      PANCAKE\t\t 85",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb3.place(x=30,y=140)
       

        #=================DESERTS===================

        self.drink=Frame(root,width=675,height=200,bd=5,bg="#4F6367",relief=RAISED)

        self.drink.propagate(0)

        self.drink.place(x=683,y=320)

        self.lab4=Label(self.drink,text="DESERTS",font=self.font2,

                        width=15,bg="#4F6367",bd=8,fg="#EEF5DB",justify=CENTER)

        self.lab4.place(x=170,y=10)

        self.dish=Label(self.drink,text="DISH\t\t\t RATE  DISH \t\t RATE",font=self.font5,bg="#4F6367",

                        fg="#EEF5DB",justify=RIGHT)

        self.dish.place(x=30,y=50)

        self.lb1=Label(self.drink,text="CHOCOLATE ICE CREAM\t 90      FRUIT SALAD\t 99",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb1.place(x=30,y=80)

        self.lb2=Label(self.drink,text="HOT CHOCOLATE BROWNIE\t 95     STRAWBERRY SUNDAE 80",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb2.place(x=30,y=110)

        self.lb3=Label(self.drink,text="NUTELLA BELLA\t\t 60      WAFFLE\t\t 50",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb3.place(x=30,y=140)

        #=================BEVERAGES===================

        self.chap=Frame(root,width=675,height=200,bd=5,bg="#4F6367",relief=RAISED)

        self.chap.propagate(0)

        self.chap.place(x=683,y=520)

        self.lab5=Label(self.chap,text="BEVERAGES",font=self.font2,

                        width=15,bg="#4F6367",bd=8,fg="#EEF5DB",justify=CENTER)

        self.lab5.place(x=170,y=10)

        self.dish=Label(self.chap,text="DISH\t\t RATE  DISH \t\t RATE",font=self.font5,bg="#4F6367",

                        fg="#EEF5DB",justify=RIGHT)

        self.dish.place(x=30,y=50)

        self.lb1=Label(self.chap,text="COLD COFFEE\t 80        SMOOTIE\t\t95",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb1.place(x=30,y=80)

        self.lb2=Label(self.chap,text="CAPPUCCINO\t 120",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb2.place(x=30,y=110)

        self.lb3=Label(self.chap,text="MOJITO\t\t 80",font=self.font4,bg="#4F6367",

                       fg="#EEF5DB",justify=RIGHT)

        self.lb3.place(x=30,y=140)

#====================================================

#=======================calculator===================

#====================================================

class Calc(Front):

     def __init__(self,root):

          #=========Frame==============

          self.f=Frame(root,width=350,height=400,bg="#4F6367")

          self.f.propagate()

          self.f.pack()

          #=========LABEL==============

          self.l1=Label(self.f,text="Calculator",

                        font=("Arial",16,"bold"),bg="#4F6367",fg="#EEF5DB")

          self.l1.place(x=120,y=10)

          #=========ENTRY==============

          self.e1=Entry(self.f,bd=5,width=33)

          self.e1.place(x=70,y=60)

          #=========Button===============

          self.b1=Button(self.f,text="1",width=4,height=2,bd=3,

                         command=self.one,bg="#4F6367",fg="#EEF5DB")

          self.b1.place(x=70,y=110)

          self.b2=Button(self.f,text="2",width=4,height=2,bd=3,

                         command=self.two,bg="#4F6367",fg="#EEF5DB")

          self.b2.place(x=130,y=110)

          self.b3=Button(self.f,text="3",width=4,height=2,bd=3,

                         command=self.three,bg="#4F6367",fg="#EEF5DB")

          self.b3.place(x=190,y=110)

          self.bsum=Button(self.f,text="+",width=4,height=2,bd=3,

                         command=self.sum,bg="#4F6367",fg="#EEF5DB")

          self.bsum.place(x=250,y=110)

          self.b4=Button(self.f,text="4",width=4,height=2,bd=3,

                         command=self.four,bg="#4F6367",fg="#EEF5DB")

          self.b4.place(x=70,y=170)

          self.b5=Button(self.f,text="5",width=4,height=2,bd=3,

                         command=self.five,bg="#4F6367",fg="#EEF5DB")

          self.b5.place(x=130,y=170)

          self.b6=Button(self.f,text="6",width=4,height=2,bd=3,

                         command=self.six,bg="#4F6367",fg="#EEF5DB")

          self.b6.place(x=190,y=170)

          self.bsub=Button(self.f,text="-",width=4,height=2,bd=3,

                           command=self.sub,bg="#4F6367",fg="#EEF5DB")

          self.bsub.place(x=250,y=170)

          self.b7=Button(self.f,text="7",width=4,height=2,bd=3,

                         command=self.seven,bg="#4F6367",fg="#EEF5DB")

          self.b7.place(x=70,y=230)

          self.b8=Button(self.f,text="8",width=4,height=2,bd=3,

                         command=self.eight,bg="#4F6367",fg="#EEF5DB")

          self.b8.place(x=130,y=230)

          self.b9=Button(self.f,text="9",width=4,height=2,bd=3,

                         command=self.nine,bg="#4F6367",fg="#EEF5DB")

          self.b9.place(x=190,y=230)

          self.bmul=Button(self.f,text="*",width=4,height=2,bd=3,

                           command=self.mul,bg="#4F6367",fg="#EEF5DB")

          self.bmul.place(x=250,y=230)

          self.bdel=Button(self.f,text="DEL",width=4,height=2,bd=3,

                           command=self.dele,bg="#4F6367",fg="#EEF5DB")

          self.bdel.place(x=70,y=290)

          self.b0=Button(self.f,text="0",width=4,height=2,bd=3,

                         command=self.zero,bg="#4F6367",fg="#EEF5DB")

          self.b0.place(x=130,y=290)

          self.bcel=Button(self.f,text="CEL",width=4,height=2,bd=3,

                           command=self.cel,bg="#4F6367",fg="#EEF5DB")

          self.bcel.place(x=190,y=290)

          self.bdiv=Button(self.f,text="/",width=4,height=2,bd=3,

                           command=self.div,bg="#4F6367",fg="#EEF5DB")

          self.bdiv.place(x=250,y=290)

          self.btotal=Button(self.f,text="=",width=30,height=1,bd=3,

                           command=self.total,bg="#4F6367",fg="#EEF5DB")

          self.btotal.place(x=70,y=350)

     #============Function==========

     def one(self):

          self.e1.insert(END,int("1"))

     def two(self):

          self.e1.insert(END,int("2"))

     def three(self):

          self.e1.insert(END,int("3"))

     def sum(self):

          self.e1.insert(END,str("+"))

     def four(self):

          self.e1.insert(END,int("4"))

     def five(self):

          self.e1.insert(END,int("5"))

     def six(self):

          self.e1.insert(END,int("6"))

     def sub(self):

          self.e1.insert(END,str("-"))

     def seven(self):

          self.e1.insert(END,int("7"))

     def eight(self):

          self.e1.insert(END,int("8"))

     def nine(self):

          self.e1.insert(END,int("9"))

     def mul(self):

          self.e1.insert(END,str("*"))

     def dele(self):

          count=int(len(self.e1.get()))

          self.e1.delete(count-1,'end')

     def zero(self):

          self.e1.insert(END,int("0"))

     def cel(self):

          self.e1.delete(0,'end')

     def div(self):

          self.e1.insert(END,str("/"))

     def total(self):

          str1=str(self.e1.get())

          self.e1.delete(0,'end')

          result=eval(str1)

          count=str(len(str1))

          self.e1.insert(END,int(result))

class Bill:

    def __init__(self,root):

        #==================Frame=====================

        self.frame=Frame(root,width=600,height=700,bd=20,bg="#4F6367",relief=RAISED)

        self.frame.propagate(0)

        self.frame.pack()

        #===================TOP=====================

        self.l1=Label(self.frame,text="CENTRAL PERK",font=("time",28,"underline"),

                      bg="#4F6367",bd=8,fg="#EEF5DB",justify=CENTER)

        self.l1.place(x=50,y=0)

        #==================searchbox=================

        self.search=Label(self.frame,text="BILL NO :-",font=("arial",20,"bold"),

                          bg="#4F6367",fg="#EEF5DB")

        self.search.place(x=70,y=65)

        self.entry=Entry(self.frame,bd=5,width=20)

        self.entry.place(x=230,y=70)

        self.sch=Button(self.frame,text="@",width=5,bd=8,bg="#4F6367",

                            fg="#EEF5DB",command=self.fun)

        self.sch.place(x=380,y=65)

        self.prt=Button(self.frame,text="Print",width=5,bd=8,bg="#4F6367",

                            fg="#EEF5DB",command=self.prt)

        self.prt.place(x=460,y=65)

        #====================Textbox================

        self.ric=Text(self.frame,width=42,height=11,font=("arial",18,"bold"),relief=RAISED)

        self.ric.place(x=0,y=130)

        self.scrollbar=Scrollbar(self.frame)

        self.scrollbar.place(x=532,y=270)

        self.scrollbar.configure(command=self.ric.yview)

        self.ric.configure(yscrollcommand=self.scrollbar.set)

        #=================Export Database============

        self.sae=Label(self.frame,text="SALES AND EXPORT",font=("arial",20,"underline"),

                          bg="#4F6367",fg="#EEF5DB")

        self.sae.place(x=140,y=470)

        self.export=Label(self.frame,text="EXPORT:-",font=("arial",18,"bold"),

                          bg="#4F6367",fg="#EEF5DB")

        self.export.place(x=140,y=520)

        self.exbt=Button(self.frame,text="EXPORT",width=6,bd=8,bg="#4F6367",

                         fg="#EEF5DB",command=self.exp)

        self.exbt.place(x=280,y=520)

    def prt(self):

        str1=self.ric.get('1.0',END)

        file=tempfile.mktemp(".txt")

        open(file,"w").write(str1)

        os.startfile(file,"print")

    def fun(self):

        if self.entry.get()=="":

            result = tkMessageBox.showwarning('WARNING', 'Please enter the bill number', icon="warning")

        else:

            self.ric.delete('1.0',END)

            conn=sqlite3.connect("restra.db")

            with conn:

                cursor=conn.cursor()

                cursor.execute('SELECT BILL FROM COMPANY WHERE ID=?',[self.entry.get()])

                fetch = cursor.fetchall()

                for data in fetch:

                    self.ric.insert(END,data)

            conn.commit()

    def exp(self):

        result = tkMessageBox.askquestion('', 'Are you sure you want to export this record?', icon="warning")

        if result == 'yes':

            conn=sqlite3.connect("restra.db")

            cursor=conn.cursor()

            cursor.execute('SELECT * FROM COMPANY')

            with open('output.csv','w')as out_csv_file:

                csv_out=csv.writer(out_csv_file)

                csv_out.writerow([d[0]for d in cursor.DISH ])

                for result in cursor:

                    csv_out.writerow(result)

            conn.close()

class About:

    def __init__(self,window):

        #================Main label=============

        self.top=Frame(window,width=1366,height=120,bd=5,bg="#EEF5DB",relief=RAISED)

        self.top.propagate(0)

        self.top.place(x=0,y=0)

        #===================Main label=============

        self.l1=Label(self.top,text="CENTRAL PERK",font=("cinzel",50,"bold"),

                      bg="#EEF5DB",bd=8,fg="#FE5F55",justify=CENTER)

        self.l1.place(x=235,y=0)

        #================Top Frame=========

        self.right=Frame(window,width=1366,height=620,bd=5,bg="#4f6367",relief=RAISED)

        self.right.propagate(0)

        self.right.place(x=0,y=120)

        #===================Main label=============

        self.l1=Label(self.right,text="The main objective of this project is to, ",font=("cinzel",18,"bold"),bg="#4F6367",bd=8,fg="#EEF5DB",justify=CENTER)

        self.l1.place(x=0,y=0)

        self.l1=Label(self.right,text="develop a standalone model, ",font=("cinzel",18,"bold"),bg="#4F6367",bd=8,fg="#EEF5DB",justify=CENTER)

        self.l1.place(x=0,y=40)

        self.l1=Label(self.right,text="which deals with  “Cafe Billing System”. The system has two parts ",font=("cinzel",18,"bold"),bg="#4F6367",bd=8,fg="#EEF5DB",justify=CENTER)

        self.l1.place(x=0,y=80)

        self.l1=Label(self.right,text="First for the selection of menu and the other for displaying Bill.",font=("cinzel",18,"bold"),bg="#4F6367",bd=8,fg="#EEF5DB",justify=CENTER)

        self.l1.place(x=0,y=120)

        self.l1=Label(self.right,text="This system generates bill including the taxes. ",font=("cinzel",18,"bold"),bg="#4F6367",bd=8,fg="#EEF5DB",justify=CENTER)

        self.l1.place(x=0,y=160)

        self.l1=Label(self.right,text="One can also check the details of all the previous customers.",font=("cinzel",18,"bold"),bg="#4F6367",bd=8,fg="#EEF5DB",justify=CENTER)

        self.l1.place(x=0,y=200)

        self.l1=Label(self.right,text="This system can store information of all bills generated.",font=("cinzel",18,"bold"),bg="#4F6367",bd=8,fg="#EEF5DB",justify=CENTER)

        self.l1.place(x=0,y=240)
        
      



window=Tk()

obj2=Front(window)

window.configure(background="#EEF5DB")

window.title("CENTRAL PERK")

window.geometry("1366x768")

window.mainloop()

