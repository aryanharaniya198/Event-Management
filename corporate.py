from tkinter import *

def location():
    master.destroy()
    import Page1

def goback():
    master.destroy()
    import templates



master=Tk()
master.title('Corporate Type')
master.config(background="light blue")
master.geometry('750x600')
T=Label(master,height=2,width=40,text="What type of Corporate Event would you like?",font=("Times New Roman",24),fg="black",bg="light blue")
T.place(x=0,y=30)
T1=Button(master,text="Fundraising",command=location,bg="white",fg="black",activebackground="blue",height=0,width=15,font=("Times New Roman",24))
T1.place(x=225,y=150)
T2=Button(master,text="Party",command=location,bg="white",fg="black",activebackground="blue",height=0,width=15,font=("Times New Roman",24))
T2.place(x=225,y=250)
T3=Button(master,text="Product Launch",command=location,bg="white",fg="black",activebackground="blue",height=0,width=15,font=("Times New Roman",24))
T3.place(x=225,y=350)
T4=Button(master,text="Go Back",command=goback,bg="white",fg="black",activebackground="blue",height=0,width=15,font=("Times New Roman",24))
T4.place(x=225,y=450)

master.mainloop()
