# Main Menu Page
# Project
# William McLaughlin
# A 51
# S. Douglas Wehbe
# A 52
# Julie Kunnumpurath
# A 53
# John Henry Burns
# A 52
# Rebecca Trackman
# A 52

import pickle

from tkinter import *

import tkinter.messagebox

from mazeGames import Maze

from mazeGames import NewMaze

from guitarHero import GuitarHero

from Hangman import Hangman

import HighScores

class MyGUI:
    def __init__(self):
        #Imports online user, and saves username
        inFile = pickle.load(open("userOnline.dat", "rb"))
        user = inFile[0]
        
        #Main window
        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.wm_title("Main Menu")
        self.__mainWindow.configure(background = "#004c66")

        #Frames
        self.__title = tkinter.Frame(self.__mainWindow)
        self.__buttons = tkinter.Frame(self.__mainWindow)
        self.__title.configure(background="#004c66")
        self.__buttons.configure(background="#004c66")
        
        #Welcome message in main window
        self.__welcome = tkinter.Label(self.__title, text = "Hello " + \
user + ", and welcome to\n the python game suite! Please select a\n\
game you would like to play!", font=("fixedsys", 15), fg="#ff9900")
        self.__welcome.configure(background = "#004c66")
        
        #Maze game button
        self.__mazeButton = tkinter.Button(self.__buttons, relief = "groove",\
                        text = "Maze Game", command = self.openMazeGame1,\
                        bg="#c2e4f0", activebackground="#d6edf5", border=0,
                        font=("fixedsys", 6))
        
        #Second maze game button
        self.__mazeButton2 = tkinter.Button(self.__buttons, relief = "groove",\
                           text = "Maze Game 2", command = self.openMazeGame2,
                           bg="#c2e4f0", activebackground="#d6edf5", border=0,\
                           font=("fixedsys", 6))
        
        #Hangman button
        self.__hangManButton = tkinter.Button(self.__buttons, relief\
                = "groove", text = "Hang Man", command = self.openHangMan,\
                bg="#c2e4f0", activebackground="#d6edf5", border=0,\
                font=("fixedsys", 6))
        
        #Guitar Hero button
        self.__guitarHeroButton = tkinter.Button(self.__buttons,\
        relief = "groove", text = "Guitar Hero", command = self.openGuitarHero\
        ,bg="#c2e4f0", activebackground="#d6edf5", border=0, \
        font=("fixedsys", 6))

        self.__highScores = tkinter.Button(self.__buttons, relief = "groove",\
                           text = "High Scores", command = self.viewHighScores,
                           bg="#c2e4f0", activebackground="#d6edf5", border=0,\
                           font=("fixedsys", 6))
        
        #Quit button
        self.__quitButton = tkinter.Button(self.__buttons, relief = "groove",\
                            text = "Quit",command =  self.__mainWindow.destroy,\
                            bg="#c2e4f0", activebackground="#d6edf5", border=0,\
                           font=("fixedsys", 6))
        
        #Packing
        self.__welcome.grid(column=1)
        self.__mazeButton.grid(column=0, sticky=E, padx=1, pady=5)
        self.__mazeButton2.grid(column=1, sticky=E, padx=1, pady=5)
        self.__hangManButton.grid(column=2, sticky=E, padx=1, pady=5)
        self.__guitarHeroButton.grid(column=3, sticky=E, padx=1, pady=5)
        self.__highScores.grid(column=4, sticky=E, padx=1, pady=5)
        self.__quitButton.grid(column=5, sticky=E, padx=1, pady=5)
        self.__title.grid()
        self.__buttons.grid()
        tkinter.mainloop()

    #When maze game button is hit, it will open a window, when user hits 'ok'
    #The game will start
    def openMazeGame1(self):
        Maze.Maze()

    def openMazeGame2(self):
        NewMaze.NewMaze()

    #Same as above but with Hang man
    def openHangMan(self):
        Hangman.Hangman()

    def openGuitarHero(self):
        GuitarHero.GuitarHero()

    def viewHighScores(self):
        HighScores.HighScores()
