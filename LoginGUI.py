#tkinter
import tkinter
from tkinter import *
import pickle
import registration
import RegisterGUI

class LoginGUI:
    def __init__(self, users):
        self.__users = users
        # Create main window
        self.__mainWindow = tkinter.Tk()
        # Set Window Title
        self.__mainWindow.wm_title("Login")
        self.__mainWindow.configure(background="#004c66")
        # Create Sections:
        self.__statusZone = tkinter.Frame(self.__mainWindow)
        self.__bottomFrame = tkinter.Frame(self.__mainWindow)
        # Create Widgets:
        self.__title = tkinter.Label(self.__mainWindow, text="Login to Play!",
                                     font=("fixedsys", 15), fg="#ff9900")
        self.__userLabel = tkinter.Label(self.__mainWindow, text="Username:",
                                         font=("fixedsys", 10), fg="#ff9900")
        self.__userEntry = tkinter.Entry(self.__mainWindow, width=13, bg="#c2e4f0",
                                         font=("fixedsys", 10))
        #Configure:
        self.__title.configure(background="#004c66")
        self.__userLabel.configure(background="#004c66")
        # Pack Widgets:
        self.__title.grid(row=0, columnspan=2, sticky=NSEW, pady=20)
        self.__userLabel.grid(row=1, column=0, sticky=W, padx=20, pady=2)
        self.__userEntry.grid(row=1, column=1, sticky=E, padx=20, pady=2)
        # Create Widgets
        self.__passLabel = tkinter.Label(self.__mainWindow, text="Password:",
                                         font=("fixedsys", 10), fg="#ff9900")
        self.__passEntry = tkinter.Entry(self.__mainWindow, width=13, bg="#c2e4f0",
                                         font=("fixedsys", 10))
        # Configure Password Entry Widget:
        self.__passEntry.configure(show='*')
        self.__passLabel.configure(background="#004c66")
        # Pack Widgets:
        self.__passLabel.grid(row=2, column=0, sticky=W, padx=20, pady=2)
        self.__passEntry.grid(row=2, column=1, sticky=E, padx=20, pady=2)
        # Create Login Status Zone:
        self.__result = tkinter.StringVar()
        self.__statusLabel = tkinter.Label(self.__statusZone,
                                      textvariable=self.__result)
        self.__statusLabel.configure(background="#004c66", fg="#ff9900")
        # Pack Status
        self.__statusLabel.grid(row=3, padx=10, sticky=NSEW)
        
        # Create Buttons:
        self.__logButton = tkinter.Button(self.__bottomFrame, text="Login",
                                          command=self.__login,
                                          relief="groove", bg="#c2e4f0",
                                          activebackground="#d6edf5", border=0,
                                          font=("fixedsys", 6))
        self.__regButton = tkinter.Button(self.__bottomFrame, text="Register",
                                          command=self.__register,
                                          relief="groove", bg="#c2e4f0",
                                          activebackground="#d6edf5", border=0,
                                          font=("fixedsys", 6))
        # Pack Widgets:
        self.__logButton.grid(row=4, column=0, sticky=E, padx=1)
        self.__regButton.grid(row=4, column=1, sticky=W, padx=1)

        self.__bottomFrame.configure(background="#004c66")
        self.__statusZone.configure(background="#004c66")

        # Pack the frames(padx and pady add padding to the frames):
        self.__statusZone.grid(columnspan=2)
        self.__bottomFrame.grid(columnspan=2, padx=7, pady=20)

        # Enter the main loop:
        tkinter.mainloop()

    def __login(self):
        self.__username = self.__userEntry.get()
        self.__password = self.__passEntry.get()
        if self.__username in self.__users:
            if self.__password == self.__users[self.__username][1]:
                self.__mainWindow.destroy()
                self.__valid = True
            else:
                self.__result.set("Incorrect Username/Password!")
                self.__valid = False
        else:
            self.__result.set("Incorrect Username/Password!")
            self.__valid = False

    def getUsername(self):
        if self.__valid:
            return self.__username
        else:
            return ''

    def getUsers(self):
        return self.__users

    def __startGUI(self):
        self.__newUser = RegisterGUI.RegisterGUI(self.__users)

    def __register(self):
        self.__startGUI()
        self.__update()

    def __update(self):
        self.__users = pickle.load(open("users.dat", "rb"))
