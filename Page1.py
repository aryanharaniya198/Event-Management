import tkinter as tk
from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

master=Tk()
master.title('Location and Venue')
master.geometry("700x300")

def insert():
       venue=locate.get()

       if(venue==""):
               MessageBox.showinfo("Insert Venue to book")
       else:
                con= mysql.connect(host="localhost", user="master", password="",database="project_main")
                cursor=con.cursor()
                cursor.execute("insert into detail values('"+venue+"')")
                cursor.execute("commit")
                 
                MessageBox.showinfo(" Insert Status", "Inserted Succesfully")
                con.close()


def andheri():
        Andheri="Kohinoor Continental - Mumbai = Kohinoor Continental, Andheri East"
        label.config(text = Andheri)
def chembur():
        Chembur="Diamond Banquet- Chembur West"
        label.config(text = Chembur)
def bandra():
        Bandra=" Taj Lands End, Bandra, Mumbai "
        label.config(text = Bandra)
def juhu():
        Juhu=" Sun-n-Sand Hotel , Juhu Beach "
        label.config(text = Juhu)
def lux():
        Lux=" JW Marriott Mumbai Juhu  "
        label.config(text = Lux)
def airport():
        Airport="Sahara star 5-Star Deluxe Hotel Vile Parle(E)"
        label.config(text = Airport)

R1= Radiobutton(master, text="1.Andheri",
                value=1,
                command=andheri)
R1.pack()
R2 = Radiobutton(master, text="2.Chembur West",
                 value=2,
                 command= chembur )
R2.pack(  )

R3 = Radiobutton(master, text="3.Bandra ",
                 value=3,
                 command=bandra)
R3.pack( )
R4 = Radiobutton(master, text="4.Juhu Beach",
                 value=4,
                 command=juhu)
R4.pack( )
R5 = Radiobutton(master, text="5.Most Luxurious ",
                 value=5,
                 command=lux)
R5.pack( )
R6 = Radiobutton(master, text="6.Near Airport",
                 value=6,
                 command=airport)
R6.pack( )


label=Label(master, font=12)
label.pack()

Label(master,text="Enter Venue prefered:").pack()
locate=Entry(master,width=35)
locate.pack()
Button(master,text="Book",command=insert).pack()

bottomframe = Frame(master)
bottomframe.pack( side = BOTTOM )
def nextpage():
        bottomframe.destroy()
        import page2
        
blackbutton = Button(bottomframe, text ='Next Page', fg ='black', command= nextpage)
blackbutton.pack( side = BOTTOM)



master.mainloop()




