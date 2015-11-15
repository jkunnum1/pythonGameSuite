# Registration

import tkinter
from tkinter import *

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
        self.__userStatus = tkinter.StringVar()
        self.__userStatusLabel = tkinter.Label(self.__userFrame,
                                               textvariable=self.__userStatus)
        # grid Widgets:
        self.__userLabel.grid(row=0, column=0, sticky=W)
        self.__userEntry.grid(row=0, column=1)
        self.__userStatusLabel.grid(row=0, column=3)
        # Create Password Widgets:
        self.__passLabel = tkinter.Label(self.__passFrame, text="Password:")
        self.__passEntry = tkinter.Entry(self.__passFrame, width=10)
        self.__passStatus = tkinter.StringVar()
        self.__passStatusLabel = tkinter.Label(self.__passFrame,
                                               textvariable=self.__passStatus)
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
        self.__confirmPassStatus = tkinter.StringVar()
        self.__confirmPassStatusLabel = tkinter.Label(self.__confirmPassFrame,
                                                      textvariable=self.__confirmPassStatus)
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
        self.__firstNameStatus = tkinter.StringVar()
        self.__firstNameStatusLabel = tkinter.Label(self.__firstNameFrame,
                                                    textvariable=self.__firstNameStatus)
        # grid Widgets:
        self.__firstNameLabel.grid(row=3, column=0)
        self.__firstNameEntry.grid(row=3, column=1)
        self.__firstNameStatusLabel.grid(row=3, column=3)

        # Create Last Name Input:
        self.__lastNameLabel = tkinter.Label(self.__lastNameFrame,
                                              text="Last Name:")
        self.__lastNameEntry = tkinter.Entry(self.__lastNameFrame,
                                              width=10)
        self.__lastNameStatus = tkinter.StringVar()
        self.__lastNameStatusLabel = tkinter.Label(self.__lastNameFrame,
                                                    textvariable=self.__lastNameStatus)
        # grid Widgets:
        self.__lastNameLabel.grid(row=4, column=0)
        self.__lastNameEntry.grid(row=4, column=1)
        self.__lastNameStatusLabel.grid(row=4, column=3)
        
        # Create email Input:
        self.__emailLabel = tkinter.Label(self.__emailFrame,
                                              text="Email:")
        self.__emailEntry = tkinter.Entry(self.__emailFrame,
                                              width=20)
        self.__emailStatus = tkinter.StringVar()
        self.__emailStatusLabel = tkinter.Label(self.__emailFrame,
                                                    textvariable=self.__emailStatus)
        # grid Widgets:
        self.__emailLabel.grid(row=5, column=0)
        self.__emailEntry.grid(row=5, column=1)
        self.__emailStatusLabel.grid(row=5, column=3)

        # Create age Input:
        self.__ageLabel = tkinter.Label(self.__ageFrame,
                                              text="Age:")
        self.__ageEntry = tkinter.Entry(self.__ageFrame,
                                              width=10)
        self.__ageStatus = tkinter.StringVar()
        self.__ageStatusLabel = tkinter.Label(self.__ageFrame,
                                                    textvariable=self.__ageStatus)
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

    def __process(self):
        print("hi")

    def __cancel(self):
        self.__registered = False
        self.__mainWindow.destroy()

    def getInfo(self):
        if not self.__registered:
            return [False]
        else:
            self.__info = [self.__userEntry.get(), self.__passEntry.get(),
                    self.__firstNameEntry.get(), self.lastNameEntry.get(),
                    self.__emailEntry.get(), self.__ageEntry.get()]
            return self.__info
