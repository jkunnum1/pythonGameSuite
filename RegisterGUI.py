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

        self.__userFrame = tkinter.Frame(self.__mainWindow)
        self.__passFrame = tkinter.Frame(self.__mainWindow)
        self.__confirmPassFrame = tkinter.Frame(self.__mainWindow)
        self.__firstNameFrame = tkinter.Frame(self.__mainWindow)
        self.__lastNameFrame = tkinter.Frame(self.__mainWindow)
        self.__emailFrame = tkinter.Frame(self.__mainWindow)
        self.__ageFrame = tkinter.Frame(self.__mainWindow)
        self.__buttons = tkinter.Frame(self.__mainWindow)
        # User frame widgets. Format for this and all others will be:
        # (Attribute) : input : status
        self.__userLabel = tkinter.Label(self.__userFrame, text="Username:")
        self.__userEntry = tkinter.Entry(self.__userFrame, width=10)
        self.__userStatusLabel = tkinter.Label(self.__userFrame, text = '')
        # grid Widgets:
        self.__userLabel.grid(row=0, column=0)
        self.__userEntry.grid(row=0, column=1)
        self.__userStatusLabel.grid(row=0, column=2)
        # Create Password Widgets:
        self.__passLabel = tkinter.Label(self.__passFrame, text="Password:")
        self.__passEntry = tkinter.Entry(self.__passFrame, width=10)
        self.__passStatusLabel = tkinter.Label(self.__passFrame, text='')

        # Configure Password Entry Widget:
        self.__passEntry.config(show='*')
        # grid Widgets:
        self.__passLabel.grid(row=1, column=0)
        self.__passEntry.grid(row=1, column=1)
        self.__passStatusLabel.grid(row=1, column=3)

        # Create Confirm Password Widgets:
        self.__confirmPassLabel = tkinter.Label(self.__confirmPassFrame,
                                                text="Confirm:")
        self.__confirmPassEntry = tkinter.Entry(self.__confirmPassFrame,
                                                width=10)
        self.__confirmPassStatusLabel = tkinter.Label(self.__confirmPassFrame,
                                                      text='')
        # Configure Password Entry Widget:
        self.__confirmPassEntry.config(show='*')
        # grid Widgets:
        self.__confirmPassLabel.grid(row=2, column=0)
        self.__confirmPassEntry.grid(row=2, column=1)
        self.__confirmPassStatusLabel.grid(row=2, column=3)

        # Create Name Input:
        self.__firstNameLabel = tkinter.Label(self.__firstNameFrame,
                                              text="First Name:")
        self.__firstNameEntry = tkinter.Entry(self.__firstNameFrame,
                                              width=10)
        self.__firstNameStatusLabel = tkinter.Label(self.__firstNameFrame, text='')
        # grid Widgets:
        self.__firstNameLabel.grid(row=3, column=0)
        self.__firstNameEntry.grid(row=3, column=1)
        self.__firstNameStatusLabel.grid(row=3, column=3)

        # Create Last Name Input:
        self.__lastNameLabel = tkinter.Label(self.__lastNameFrame,
                                              text="Last Name:")
        self.__lastNameEntry = tkinter.Entry(self.__lastNameFrame,
                                              width=10)
        self.__lastNameStatusLabel = tkinter.Label(self.__lastNameFrame, text='')
        # grid Widgets:
        self.__lastNameLabel.grid(row=4, column=0)
        self.__lastNameEntry.grid(row=4, column=1)
        self.__lastNameStatusLabel.grid(row=4, column=3)
        
        # Create email Input:
        self.__emailLabel = tkinter.Label(self.__emailFrame,
                                              text="Email:")
        self.__emailEntry = tkinter.Entry(self.__emailFrame,
                                              width=20)
        self.__emailStatusLabel = tkinter.Label(self.__emailFrame, text='')
        # grid Widgets:
        self.__emailLabel.grid(row=5, column=0)
        self.__emailEntry.grid(row=5, column=1)
        self.__emailStatusLabel.grid(row=5, column=3)

        # Create age Input:
        self.__ageLabel = tkinter.Label(self.__ageFrame,
                                              text="Age:")
        self.__ageEntry = tkinter.Entry(self.__ageFrame,
                                              width=10)
        self.__ageStatusLabel = tkinter.Label(self.__ageFrame, text='')
        # grid Widgets:
        self.__ageLabel.grid(row=6, column=0)
        self.__ageEntry.grid(row=6, column=1)
        self.__ageStatusLabel.grid(row=6, column=3)

        # Create buttons:
        self.__regButton = tkinter.Button(self.__buttons, text="Register",
                                          command=self.__process)
        self.__cancelButton = tkinter.Button(self.__buttons, text="Cancel",
                                             command=self.__cancel)
        # grid buttons:
        self.__regButton.grid(row=7, column=0)
        self.__cancelButton.grid(row=7, column=1)


        # grid Frames:
        self.__userFrame.grid(padx=5, pady=5, sticky=E)
        self.__passFrame.grid(padx=5, pady=5, sticky=E)
        self.__confirmPassFrame.grid(padx=5, pady=5, sticky=E)
        self.__firstNameFrame.grid(padx=5, pady=5, sticky=E)
        self.__lastNameFrame.grid(padx=5, pady=5, sticky=E)
        self.__emailFrame.grid(padx=5, pady=5, sticky=E)
        self.__ageFrame.grid(padx=5, pady=5, sticky=E)
        self.__buttons.grid(padx=5, pady=5, sticky=E)
        # Start the main loop
        tkinter.mainloop()

    def __getStati(self):
        results = self.__info
        if not results[0]:
            self.__userStatusLabel.config(text="Invalid username!")
            self.__registered = False
        if not results[1]:
            self.__confirmPassStatusLabel.config(text="Invalid password/passwords don't match!")
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
                           lastName, email, age]
            self.__users[user] = self.__info
            print(self.__users)
            pickle.dump(self.__users, open("users.dat", "wb"))
        

    def __cancel(self):
        self.__registered = False
        self.__mainWindow.destroy()

    def getInfo(self):
        if not self.__registered:
            return [False]
        else:
            return self.__info
