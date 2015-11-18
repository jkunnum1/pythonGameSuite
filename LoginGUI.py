#tkinter
import tkinter
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
        # Create Sections:
        self.__topFrame = tkinter.Frame(self.__mainWindow)
        self.__middleFrame = tkinter.Frame(self.__mainWindow)
        self.__statusZone = tkinter.Frame(self.__mainWindow)
        self.__bottomFrame = tkinter.Frame(self.__mainWindow)
        # Create Widgets For Top Frame:
        self.__userLabel = tkinter.Label(self.__topFrame, text="Username:")
        self.__userEntry = tkinter.Entry(self.__topFrame, width=10)
        # Pack Widgets:
        self.__userLabel.pack(side="left")
        self.__userEntry.pack(side="left")
        # Create Widgets For Middle Frame:
        self.__passLabel = tkinter.Label(self.__middleFrame, text="Password:")
        self.__passEntry = tkinter.Entry(self.__middleFrame, width=10)
        # Configure Password Entry Widget:
        self.__passEntry.config(show='*')
        # Pack Widgets:
        self.__passLabel.pack(side="left")
        self.__passEntry.pack(side="left")
        # Create Login Status Zone:
        self.__result = tkinter.StringVar()
        self.__statusLabel = tkinter.Label(self.__statusZone,
                                      textvariable=self.__result)
        # Pack Status
        self.__statusLabel.pack(side="left")
        
        # Create Buttons:
        self.__logButton = tkinter.Button(self.__bottomFrame, text="Login",
                                          command=self.__login)
        self.__regButton = tkinter.Button(self.__bottomFrame, text="Register",
                                          command=self.__register)
        # Pack Widgets:
        self.__logButton.pack(side="left")
        self.__regButton.pack(side="left")

        # Pack the frames(padx and pady add padding to the frames):
        self.__topFrame.pack(padx=40, pady=10)
        self.__middleFrame.pack(padx=40, pady=0)
        self.__statusZone.pack()
        self.__bottomFrame.pack(padx=40, pady=10)

        # Enter the main loop:
        tkinter.mainloop()

    def __login(self):
        self.__username = self.__userEntry.get()
        self.__password = self.__passEntry.get()
        if self.__username in self.__users:
            if self.__password == self.__users[self.__username][1]:
                self.__mainWindow.destroy()
            else:
                self.__result.set("Incorrect Username/Password!")
        else:
            self.__result.set("Incorrect Username/Password!")       

    def getUsername(self):
        return self.__username

    def getUsers(self):
        return self.__users

    def __startGUI(self):
        self.__newUser = RegisterGUI.RegisterGUI(self.__users)

    def __register(self):
        self.__startGUI()
        self.__update()

    def __update(self):
        self.__users = pickle.load(open("users.dat", "rb"))














