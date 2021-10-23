# pip install tkcalendar before using this


import tkinter as tk
from tkinter import *
from tkcalendar import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import ImageTk,Image

master = Tk()
master.title("Details")
master.geometry("400x700")
master.config(background="light blue")
fram1 = Frame(master)
fram1.pack()

menusel = 1

def image_id():
       
    import Payment

def insert():
       date_main=cal.get_date()
       menu_main=menu_ava.get()

       if(date_main=="" or menu_main==""):
               MessageBox.showinfo("Insert Venue to book")
       else:
                con= mysql.connect(host="localhost", user="master", password="",database="project_main")
                cursor=con.cursor()
                cursor.execute("insert into location values('"+date_main+"', '"+menu_main+"')")
                cursor.execute("commit")
                 
                MessageBox.showinfo(" Insert Status", " Succesfully")
                con.close()




def expense():
    if menusel == 1:
        Cost = "Any event at this venue with 250 people will cost Rs.45000- Rs.60000\n To organise event above 250 people email us on xyz.gmail.com"
        expnd.config(text=Cost, bg="light blue")

    elif menusel == 2:
        print(menusel)
        Cost = "Any event at this venue with 250 people will cost Rs.35000- Rs.50000\n To organise event above 250 people email us on xyz.gmail.com"
        expnd.config(text=Cost, bg="light blue")



    
    # add date to a list which SQL wants


# ------------------------------DATE-----------------------------#
Label(fram1, text="Date", font=17).pack()

cal = Calendar(fram1, selectmode="day", year=2020, month=5, day=22)

cal.pack(pady=20)


Label(fram1, text="Catering", font=17).pack()

fm = Frame(fram1)
fm.pack()


m1 = Radiobutton(
    fm,
    text="Menu 1\n\nMutton Shawrma\nSprite/Coco Cola/ Fanta\nNoodles\nButter chicken\nVeg Fired Rice\nPanner Tikka Masala\nKalimirhi Chicken\nRoti\nMishti Doi",
    value=1,
)
m1.pack(side="left")

m2 = Radiobutton(
    fm,
    text="Menu 2\n\nVeg Pulao\nVeg Biryani\nFruit Beer\nPita Bread\nPanner65\nIcecream\nVeg roll\nAloo Tikka Masala",
    value=2)
            
m2.pack(side="right")

menu_ava=Entry(fram1,width=35)
menu_ava.pack()
Button(fram1,text="Confirm date and menu",command=insert).pack()

Button(fram1, text="Expediture", command=expense).pack(pady=20)
expnd = Label(fram1, text="")
expnd.pack()


Button(fram1, text="Payment", command=image_id, background="gray").pack(pady=20)


master.mainloop()
