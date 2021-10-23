from tkinter import *

def personal():
    master.destroy()
    import personal
    

def corporate():
    master.destroy()
    import corporate

def goback():
    master.destroy()
    import Login_Signup




master=Tk()
master.title('Event Type')
master.config(background="light blue")
master.geometry('600x500')
T=Label(master,height=2,width=30,text="What type of Event would you like?",font=("Times New Roman",24),fg="black",bg="light blue")
T.place(x=30,y=30)
T1=Button(master,text="Personal",command=personal,bg="white",fg="black",activebackground="blue",height=5,width=10,font=("Times New Roman",24))
T1.place(x=90,y=150)
T2=Button(master,text="Corporate",command=corporate,bg="white",fg="black",activebackground="blue",height=5,width=10,font=("Times New Roman",24))
T2.place(x=330,y=150)
T3=Button(master,text="Go Back",command=goback,bg="white",fg="black",activebackground="blue",height=0,width=15,font=("Times New Roman",24))
T3.place(x=150,y=400)


master.mainloop()
