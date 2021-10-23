from tkinter import *
import os
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="gray").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username  ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password  ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
    
def nextpage():
       
        import templates
 

 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    Home=Button(login_screen, text="Home Page", width=10, height=1,command=nextpage).pack()
 

 
def register_user():
 
    
    try:
        username=username_entry.get()
        password=password_entry.get()
        

        if(username=="" or password==""):
                MessageBox.showinfo("Insert the username and password")
        else:
                con= mysql.connect(host="localhost", user="r_screen", password="",database="project_main")
                cursor=con.cursor()
                cursor.execute("insert into data_info values('"+username+"','"+password+"')")
                cursor.execute("commit")
               
                                    
                     
                MessageBox.showinfo(" Insert Status", "Inserted Succesfully")
                con.close()
    except mysql.connector.errors.IntegrityError as e:
        MessageBox.showinfo("Alert","username exists")
    except Exception as e:
        MessageBox.showinfo("Alert","some error has occured")
 

 
def login_verify():
    username=username_login_entry.get()
    password=password_login_entry.get()
    print(username)
    print(password)
    try:
        if(username=="" or password==""):
                MessageBox.showinfo("Insert the username and password")
        else:
                con= mysql.connect(host="localhost", user="login_screen", password="",database="project_main")
                cursor=con.cursor()
                qry="select password from data_info where username='"+username+ "'"
                print(qry)
                cursor.execute(qry)
                row=cursor.fetchall()
                print(row)
                if len(row)== 0:
                    MessageBox.showerror("Error" , "Username does not exist")
                else:
                    db_password=row[0][0]
                    if(password==db_password):
                        MessageBox.showinfo("logged in", "Successfull")
                    else:
                        MessageBox.showinfo("Alert","password is incorrect")
                con.close()
    except mysql.errors.IntegrityError as e:
        MessageBox.showinfo("Alert","some database error has occured")
    except Exception as e:
        MessageBox.showinfo("Alert","some error has occured")
##           
##		
##           
##				con = pymysql.connect(host="localhost",user="root",password="",database="docterapp")
##	cur = con.cursor()
##
##	cur.execute("select * from user_information where username ='"+ user_name.get() + "'")
##	row = cur.fetchall()
##                 
##      
    
 

 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 

 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 

 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
    
def insert():
    username=username_entry.get()
    password=password_entry.get()
    

    if(username=="" or password==""):
            MessageBox.showinfo("Insert Venue to book")
    else:
            con= mysql.connect(host="localhost", user="register_screen", password="",database="project")
            cursor=con.cursor()
            cursor.execute("insert into mysql values('"+username+"','"+password+"')")
            cursor.execute("commit")
                 
            MessageBox.showinfo(" Insert Status", "Inserted Succesfully")
            con.close()
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("900x250")
    main_screen.title("Account Login")
    Label(text="Book your events with us !", bg="gray", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
