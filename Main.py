# import modules

from tkinter import *
import os


# Designing window for login

def Login():
    global Login_screen
    Login_screen = Toplevel(main_screen)
    Login_screen.title("Login")
    Login_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(Login_screen, text="Please enter details below", bg="blue").pack()
    Label(Login_screen, text="").pack()
    username_lable = Label(Login_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(Login_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(Login_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(Login_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(Login_screen, text="").pack()
    Button(Login_screen, text="Login", width=10, height=1, bg="blue", command=Login_user).pack()


# Implementing event on login button

def Login_user():
    username_info = username.get()
    password_info = password.get()
    print(username_info)
    print(password_info)


    Label(Login_screen, text="Login Success", fg="green", font=("calibri", 11)).pack()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    # Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=Login).pack()

    main_screen.mainloop()


main_account_screen()
