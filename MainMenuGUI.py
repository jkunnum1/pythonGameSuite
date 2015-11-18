#Main Menu Page

import pickle

import tkinter

import tkinter.messagebox

class MyGUI:
    def __init__(self):
        #Imports online user, and saves username
        inFile = pickle.load(open("userOnline.dat", "rb"))
        user = inFile[0]
        #Main window
        self.__mainWindow = tkinter.Tk()
        #Welcome message in main window
        self.__welcome = tkinter.Label(self.__mainWindow, text = "Hello " + \
user + ", and welcome to the python game suite! please select a \
game you would like to play!")
        #Maze game button
        self.__mazeButton = tkinter.Button(self.__mainWindow,\
                           text = "Maze Game", command = self.openMazeGame)
        #Hangman button
        self.__hangManButton = tkinter.Button(self.__mainWindow,\
                            text = "Hang Man", command = self.openHangMan)
        #Quit button
        self.__quitButton = tkinter.Button(self.__mainWindow,\
                            text = "Quit", command =  self.__mainWindow.destroy)
        #Paccking
        self.__welcome.pack()
        self.__mazeButton.pack()
        self.__hangManButton.pack()
        self.__quitButton.pack()
        tkinter.mainloop()

    #When maze game button is hit, it will open a window, when user hits 'ok'
    #The game will start
    def openMazeGame(self):
        tkinter.messagebox.showinfo(message = "Play maze game")
        import maze

    #Same as above but with Hang man
    def openHangMan(self):
        tkinter.messagebox.showinfo(message = "Play Hang man")
        from Hangman import hangman