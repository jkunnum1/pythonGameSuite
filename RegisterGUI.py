# Project
# Kunnumpurath, Julie
# A 53
# McLaughlin, William
# A 51
# Wehbe, Semaan
# A 52
# Burns, John Henry
# A 52
# Trackman, Rebecca
# A 52

import tkinter
import pickle
from tkinter import *
import verification


class RegisterGUI:
    def __init__(self, users):
        self.__users = users
        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.wm_title("Register")
        self.__mainWindow.configure(background="#004c66")

        self.__title = tkinter.Frame(self.__mainWindow)
        self.__buttons = tkinter.Frame(self.__mainWindow)

        self.__titleText = tkinter.Label(self.__mainWindow,
                                         text="Register New User:",
                                         font=("fixedsys", 15), fg="#ff9900")
        self.__titleText.configure(background="#004c66")
        self.__titleText.grid(row=0, columnspan=2, pady=20)
        # User frame widgets. Format for this and all others will be:
        # (Attribute) : input : status
        self.__userLabel = tkinter.Label(self.__mainWindow, text="Username:",
                                         font=("fixedsys", 10), fg="#ff9900")
        self.__userEntry = tkinter.Entry(self.__mainWindow, width=13,
                                         bg="#c2e4f0",
                                         font=("fixedsys", 10))
        self.__userStatusLabel = tkinter.Label(self.__mainWindow, text='',
                                               fg="#ff9900")

        self.__userLabel.configure(background="#004c66")
        self.__userStatusLabel.configure(background="#004c66")

        # grid Widgets:
        self.__userLabel.grid(row=1, column=0, sticky=W, padx=20, pady=1)
        self.__userEntry.grid(row=1, column=1, sticky=E, padx=20, pady=1)
        self.__userStatusLabel.grid(row=2, column=1)

        # Create Password Widgets:
        self.__passLabel = tkinter.Label(self.__mainWindow, text="Password:",
                                         font=("fixedsys", 10), fg="#ff9900")
        self.__passEntry = tkinter.Entry(self.__mainWindow, width=13,
                                         bg="#c2e4f0", font=("fixedsys", 10))
        self.__placeholder = tkinter.Label(self.__mainWindow,
                                           text='', fg="#ff9900")

        # Configure Password Entry Widget:
        self.__passEntry.config(show='*')
        self.__passLabel.configure(background="#004c66")
        self.__placeholder.configure(background="#004c66")

        # grid Widgets:
        self.__passLabel.grid(row=3, column=0, sticky=W, padx=20, pady=1)
        self.__passEntry.grid(row=3, column=1, sticky=E, padx=20, pady=1)
        self.__placeholder.grid(row=4)

        # Create Confirm Password Widgets:
        self.__confirmPassLabel = tkinter.Label(self.__mainWindow,
                                                text="Confirm Password:",
                                                font=("fixedsys", 10),
                                                fg="#ff9900")
        self.__confirmPassEntry = tkinter.Entry(self.__mainWindow, width=13,
                                                bg="#c2e4f0",
                                                font=("fixedsys", 10))
        self.__confirmPassStatusLabel = tkinter.Label(self.__mainWindow,
                                                      text='', fg="#ff9900")

        # Configure Password Entry Widget:
        self.__confirmPassEntry.config(show='*')
        self.__confirmPassLabel.configure(background="#004c66")
        self.__confirmPassStatusLabel.configure(background="#004c66")

        # grid Widgets:
        self.__confirmPassLabel.grid(row=5, column=0, sticky=W, padx=20,
                                     pady=1)
        self.__confirmPassEntry.grid(row=5, column=1, sticky=E, padx=20,
                                     pady=1)
        self.__confirmPassStatusLabel.grid(row=6, column=1)

        # Create Name Input:
        self.__firstNameLabel = tkinter.Label(self.__mainWindow,
                                              text="First Name:",
                                              font=("fixedsys", 10),
                                              fg="#ff9900")
        self.__firstNameEntry = tkinter.Entry(self.__mainWindow, width=13,
                                              bg="#c2e4f0",
                                              font=("fixedsys", 10))
        self.__firstNameStatusLabel = tkinter.Label(self.__mainWindow,
                                                    text='', fg="#ff9900")

        self.__firstNameLabel.configure(background="#004c66")
        self.__firstNameStatusLabel.configure(background="#004c66")

        # grid Widgets:
        self.__firstNameLabel.grid(row=7, column=0, sticky=W, padx=20, pady=1)
        self.__firstNameEntry.grid(row=7, column=1, sticky=E, padx=20, pady=1)
        self.__firstNameStatusLabel.grid(row=8, column=1)

        # Create Last Name Input:
        self.__lastNameLabel = tkinter.Label(self.__mainWindow,
                                             text="Last Name:",
                                             font=("fixedsys", 10),
                                             fg="#ff9900")
        self.__lastNameEntry = tkinter.Entry(self.__mainWindow, width=13,
                                             bg="#c2e4f0",
                                             font=("fixedsys", 10))
        self.__lastNameStatusLabel = tkinter.Label(self.__mainWindow,
                                                   text='', fg="#ff9900")

        self.__lastNameLabel.configure(background="#004c66")
        self.__lastNameStatusLabel.configure(background="#004c66")

        # grid Widgets:
        self.__lastNameLabel.grid(row=9, column=0, sticky=W, padx=20, pady=1)
        self.__lastNameEntry.grid(row=9, column=1, sticky=E, padx=20, pady=1)
        self.__lastNameStatusLabel.grid(row=10, column=1)

        # Create email Input:
        self.__emailLabel = tkinter.Label(self.__mainWindow,
                                          text="Email:", font=("fixedsys",
                                                               10),
                                          fg="#ff9900")
        self.__emailEntry = tkinter.Entry(self.__mainWindow, width=13,
                                          bg="#c2e4f0", font=("fixedsys", 10))
        self.__emailStatusLabel = tkinter.Label(self.__mainWindow, text='',
                                                fg="#ff9900")

        self.__emailLabel.configure(background="#004c66")
        self.__emailStatusLabel.configure(background="#004c66")

        # grid Widgets:
        self.__emailLabel.grid(row=11, column=0, sticky=W, padx=20, pady=1)
        self.__emailEntry.grid(row=11, column=1, sticky=E, padx=20, pady=1)
        self.__emailStatusLabel.grid(row=12, column=1)

        # Create age Input:
        self.__ageLabel = tkinter.Label(self.__mainWindow,
                                        text="Age:", font=("fixedsys", 10),
                                        fg="#ff9900")
        self.__ageEntry = tkinter.Entry(self.__mainWindow, width=13,
                                        bg="#c2e4f0",
                                        font=("fixedsys", 10))
        self.__ageStatusLabel = tkinter.Label(self.__mainWindow, text='',
                                              fg="#ff9900")

        self.__ageLabel.configure(background="#004c66")
        self.__ageStatusLabel.configure(background="#004c66")

        # grid Widgets:
        self.__ageLabel.grid(row=13, column=0, sticky=W, padx=20, pady=1)
        self.__ageEntry.grid(row=13, column=1, sticky=E, padx=20, pady=1)
        self.__ageStatusLabel.grid(row=14, column=1)

        # Create buttons:
        self.__regButton = tkinter.Button(self.__buttons, text="Register",
                                          command=self.__process,
                                          relief="groove", bg="#c2e4f0",
                                          activebackground="#d6edf5", border=0,
                                          font=("fixedsys", 6))
        self.__cancelButton = tkinter.Button(self.__buttons, text="Cancel",
                                             command=self.__cancel,
                                             relief="groove", bg="#c2e4f0",
                                             activebackground="#d6edf5",
                                             border=0, font=("fixedsys", 6))

        # grid buttons:
        self.__regButton.grid(row=15, column=0, sticky=E, padx=1)
        self.__cancelButton.grid(row=15, column=1, sticky=W, padx=1)

        self.__buttons.configure(background="#004c66")
        # grid button frame:
        self.__buttons.grid(columnspan=2, padx=7, pady=20)

        tkinter.mainloop()

    def __getStati(self):
        results = self.__info
        if not results[0]:
            self.__userStatusLabel.config(text="Invalid username!")
            self.__registered = False
        if not results[1]:
            self.__confirmPassStatusLabel.config(text="Invalid password(s)!")
            self.__registered = False
        if not results[2]:
            self.__firstNameStatusLabel.config(text="First name " +
                                               "cannot be blank!")
            self.__registered = False
        if not results[3]:
            self.__lastNameStatusLabel.config(text="Last name cannot " +
                                              "be blank!")
            self.__registered = False
        if not results[4]:
            self.__emailStatusLabel.config(text="Invalid email!")
            self.__registered = False
        if not results[5]:
            self.__ageStatusLabel.config(text="Invalid age!")
            self.__registered = False
        if False not in results:
            self.__mainWindow.destroy()
        return(results[0] and results[1] and results[2] and results[3] and
               results[4] and results[5])

    def __process(self):
        self.__userStatusLabel.config(text='')
        self.__confirmPassStatusLabel.config(text='')
        self.__firstNameStatusLabel.config(text='')
        self.__lastNameStatusLabel.config(text='')
        self.__emailStatusLabel.config(text='')
        self.__ageStatusLabel.config(text='')
        user = self.__userEntry.get()
        password = self.__passEntry.get()
        confirmPassword = self.__confirmPassEntry.get()
        firstName = self.__firstNameEntry.get()
        lastName = self.__lastNameEntry.get()
        email = self.__emailEntry.get()
        age = self.__ageEntry.get()
        self.__info = verification.verify([user, password, confirmPassword,
                                           firstName, lastName, email, age],
                                          self.__users)
        valid = self.__getStati()
        if valid:
            self.__info = [user, password, firstName,
                           lastName, email, age, 0]
            self.__users[user] = self.__info
            pickle.dump(self.__users, open("users.dat", "wb"))

    def __cancel(self):
        self.__registered = False
        self.__mainWindow.destroy()

    def getInfo(self):
        if not self.__registered:
            return [False]
        else:
            return self.__info
