# Registration

import tkinter
import pickle
from tkinter import *
import verification

class RegisterGUI:
    def __init__(self, users):
        self.__users = users
        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.wm_title("Register")

        self.__title = tkinter.Frame(self.__mainWindow)
        self.__buttons = tkinter.Frame(self.__mainWindow)
        
        self.__titleText = tkinter.Label(self.__mainWindow,
                                         text="Register New User:")
        self.__titleText.grid(row=0, columnspan=2, pady=10)
        # User frame widgets. Format for this and all others will be:
        # (Attribute) : input : status
        self.__userLabel = tkinter.Label(self.__mainWindow, text="Username:")
        self.__userEntry = tkinter.Entry(self.__mainWindow, width=20)
        self.__userStatusLabel = tkinter.Label(self.__mainWindow, text = '')

        # grid Widgets:
        self.__userLabel.grid(row=1, column=0, sticky=W, padx=7, pady=1)
        self.__userEntry.grid(row=1, column=1, sticky=E, padx=10, pady=1)
        self.__userStatusLabel.grid(row=2, column=1)

        # Create Password Widgets:
        self.__passLabel = tkinter.Label(self.__mainWindow, text="Password:")
        self.__passEntry = tkinter.Entry(self.__mainWindow, width=20)
        self.__placeholder = tkinter.Label(self.__mainWindow, text='')

        # Configure Password Entry Widget:
        self.__passEntry.config(show='*')
        
        # grid Widgets:
        self.__passLabel.grid(row=3, column=0, sticky=W, padx=7, pady=1)
        self.__passEntry.grid(row=3, column=1, sticky=E, padx=10, pady=1)
        self.__placeholder.grid(row=4)

        # Create Confirm Password Widgets:
        self.__confirmPassLabel = tkinter.Label(self.__mainWindow,
                                                text="Confirm Password:")
        self.__confirmPassEntry = tkinter.Entry(self.__mainWindow,
                                                width=20)
        self.__confirmPassStatusLabel = tkinter.Label(self.__mainWindow,
                                                      text='')

        # Configure Password Entry Widget:
        self.__confirmPassEntry.config(show='*')
        # grid Widgets:
        self.__confirmPassLabel.grid(row=5, column=0, sticky=W, padx=7, pady=1)
        self.__confirmPassEntry.grid(row=5, column=1, sticky=E, padx=10, pady=1)
        self.__confirmPassStatusLabel.grid(row=6, column=1)

        # Create Name Input:
        self.__firstNameLabel = tkinter.Label(self.__mainWindow,
                                              text="First Name:")
        self.__firstNameEntry = tkinter.Entry(self.__mainWindow,
                                              width=20)
        self.__firstNameStatusLabel = tkinter.Label(self.__mainWindow,
                                                    text='')

        # grid Widgets:
        self.__firstNameLabel.grid(row=7, column=0, sticky=W, padx=7, pady=1)
        self.__firstNameEntry.grid(row=7, column=1, sticky=E, padx=10, pady=1)
        self.__firstNameStatusLabel.grid(row=8, column=1)

        # Create Last Name Input:
        self.__lastNameLabel = tkinter.Label(self.__mainWindow,
                                              text="Last Name:")
        self.__lastNameEntry = tkinter.Entry(self.__mainWindow,
                                              width=20)
        self.__lastNameStatusLabel = tkinter.Label(self.__mainWindow,
                                                   text='')

        # grid Widgets:
        self.__lastNameLabel.grid(row=9, column=0, sticky=W, padx=7, pady=1)
        self.__lastNameEntry.grid(row=9, column=1, sticky=E, padx=10, pady=1)
        self.__lastNameStatusLabel.grid(row=10, column=1)
        
        # Create email Input:
        self.__emailLabel = tkinter.Label(self.__mainWindow,
                                              text="Email:")
        self.__emailEntry = tkinter.Entry(self.__mainWindow,
                                              width=20)
        self.__emailStatusLabel = tkinter.Label(self.__mainWindow, text='')

        # grid Widgets:
        self.__emailLabel.grid(row=11, column=0, sticky=W, padx=7, pady=1)
        self.__emailEntry.grid(row=11, column=1, sticky=E, padx=10, pady=1)
        self.__emailStatusLabel.grid(row=12, column=1)

        # Create age Input:
        self.__ageLabel = tkinter.Label(self.__mainWindow,
                                              text="Age:")
        self.__ageEntry = tkinter.Entry(self.__mainWindow,
                                              width=20)
        self.__ageStatusLabel = tkinter.Label(self.__mainWindow, text='')

        # grid Widgets:
        self.__ageLabel.grid(row=13, column=0, sticky=W, padx=7, pady=1)
        self.__ageEntry.grid(row=13, column=1, sticky=E, padx=10, pady=1)
        self.__ageStatusLabel.grid(row=14, column=1)

        # Create buttons:
        self.__regButton = tkinter.Button(self.__buttons, text="Register",
                                          command=self.__process)
        self.__cancelButton = tkinter.Button(self.__buttons, text="Cancel",
                                             command=self.__cancel)
        # grid buttons:
        self.__regButton.grid(row=15, column=0, sticky=E)
        self.__cancelButton.grid(row=15, column=1, sticky=W)
        # grid button frame:
        self.__buttons.grid(columnspan=2, padx=7, pady=10)
        

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
            self.__firstNameStatusLabel.config(text="First name cannot be blank!")
            self.__registered = False
        if not results[3]:
            self.__lastNameStatusLabel.config(text="Last name cannot be blank!")
            self.__registered = False
        if not results[4]:
            self.__emailStatusLabel.config(text="Invalid email!")
            self.__registered = False
        if not results[5]:
            self.__ageStatusLabel.config(text="Invalid age!")
            self.__registered = False
        if False not in results:
            self.__mainWindow.destroy()
        return results[0] and results[1] and results[2] and results[3] and \
               results[4] and results[5]
        

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
