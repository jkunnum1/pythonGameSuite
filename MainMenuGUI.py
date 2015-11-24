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
        self.__mazeButton = tkinter.Button(self.__mainWindow, relief = "groove",\
                           text = "Maze Game", command = self.openMazeGame1)
        #Second maze game button
        self.__mazeButton2 = tkinter.Button(self.__mainWindow, relief = "groove",\
                           text = "Maze Game 2", command = self.openMazeGame2)
        #Hangman button
        self.__hangManButton = tkinter.Button(self.__mainWindow, relief = "groove",\
                            text = "Hang Man", command = self.openHangMan)
        #Guitar Hero button
        self.__guitarHeroButton = tkinter.Button(self.__mainWindow,\
        relief = "groove", text = "Guitar Hero", command = self.openGuitarHero)
        #Quit button
        self.__quitButton = tkinter.Button(self.__mainWindow, relief = "groove",\
                            text = "Quit", command =  self.__mainWindow.destroy)
        #Packing
        self.__welcome.pack()
        self.__mazeButton.pack()
        self.__mazeButton2.pack()
        self.__hangManButton.pack()
        self.__guitarHeroButton.pack()
        self.__quitButton.pack()
        tkinter.mainloop()

    #When maze game button is hit, it will open a window, when user hits 'ok'
    #The game will start
    def openMazeGame1(self):
        from mazeGames import maze
        #quit()

    def openMazeGame2(self):
        from mazeGames import newMaze

    #Same as above but with Hang man
    def openHangMan(self):
        from Hangman import hangmanV4

    def openGuitarHero(self):
        from guitarHero import guitarHero

