from tkinter import *

def location():
    master.destroy()
    import Page1

def goback():
    master.destroy()
    import templates



master=Tk()
master.title('Personal Type')
master.config(background="light blue")
master.geometry('750x600')
T=Label(master,height=2,width=40,text="What type of Personal Event would you like?",font=("Times New Roman",24),fg="black",bg="light blue")
T.place(x=0,y=30)
T1=Button(master,text="Party",command=location,bg="white",fg="black",activebackground="blue",height=2,width=10,font=("Times New Roman",24))
T1.place(x=150,y=150)
T2=Button(master,text="Birthday",command=location,bg="white",fg="black",activebackground="blue",height=2,width=10,font=("Times New Roman",24))
T2.place(x=390,y=150)
T3=Button(master,text="Anniversary",command=location,bg="white",fg="black",activebackground="blue",height=2,width=10,font=("Times New Roman",24))
T3.place(x=150,y=300)
T4=Button(master,text="Wedding",command=location,bg="white",fg="black",activebackground="blue",height=2,width=10,font=("Times New Roman",24))
T4.place(x=390,y=300)
T5=Button(master,text="Go Back",command=goback,bg="white",fg="black",activebackground="blue",height=2,width=10,font=("Times New Roman",24))
T5.place(x=270,y=450)

master.mainloop()
