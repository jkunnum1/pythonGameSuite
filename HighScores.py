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

import pickle
from tkinter import *
import tkinter.messagebox


class HighScores:
    def __init__(self):
        # main window
        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.wm_title("High Scores")
        self.__mainWindow.configure(background="#004c66")

        # button frame
        self.__buttons = tkinter.Frame(self.__mainWindow)
        self.__buttons.configure(background="#004c66")

        # scores frame
        self.__content = tkinter.Frame(self.__mainWindow)
        self.__content.configure(background="#004c66")

        self.__filename = ""

        self.__totalScore = tkinter.Button(self.__buttons, relief="flat",
                                           text="Total Scores", bg="#c2e4f0",
                                           command=self.__total,
                                           activebackground="#d6edf5",
                                           border=0, font=("fixedsys", 6))

        self.__mazeScore = tkinter.Button(self.__buttons, relief="flat",
                                          text="Maze Game", bg="#c2e4f0",
                                          command=self.__maze1,
                                          activebackground="#d6edf5",
                                          border=0, font=("fixedsys", 6))

        self.__mazeScore2 = tkinter.Button(self.__buttons, relief="flat",
                                           text="Maze Game 2", bg="#c2e4f0",
                                           command=self.__maze2,
                                           activebackground="#d6edf5",
                                           border=0, font=("fixedsys", 6))

        self.__guitarScores = tkinter.Button(self.__buttons, relief="flat",
                                             text="Guitar Hero", bg="#c2e4f0",
                                             command=self.__guitarHero,
                                             activebackground="#d6edf5",
                                             border=0, font=("fixedsys", 6))

        self.__hangman = tkinter.Button(self.__buttons, relief="flat",
                                        text="Hangman", command=self.__hangman,
                                        bg="#c2e4f0", border=0,
                                        activebackground="#d6edf5",
                                        font=("fixedsys", 6))

        self.__quitButton = tkinter.Button(self.__buttons, relief="flat",
                                           text="Quit", bg="#c2e4f0",
                                           command=self.__mainWindow.destroy,
                                           activebackground="#d6edf5",
                                           border=0, font=("fixedsys", 6))

        self.__scoreLabel = tkinter.Label(self.__content, text='',
                                          font=("fixedsys", 10), fg="#ff9900",
                                          bg="#004c66")

        self.__buttons.grid()
        self.__content.grid(row=1)
        self.__mazeScore.grid(row=0, column=0)
        self.__mazeScore2.grid(row=0, column=2)
        self.__guitarScores.grid(row=0, column=4)
        self.__hangman.grid(row=0, column=6)
        self.__totalScore.grid(row=0, column=8)
        self.__quitButton.grid(row=0, column=10)
        self.__scoreLabel.grid(rowspan=5, columnspan=5, pady=50)

        tkinter.mainloop()

    def __maze1(self):
        self.__filename = "mazeGames/mazeScores.dat"
        self.__mazeScore.configure(bg="#ebf6fa")
        self.__mazeScore2.configure(bg="#addbeb")
        self.__guitarScores.configure(bg="#addbeb")
        self.__hangman.configure(bg="#addbeb")
        self.__totalScore.configure(bg="#addbeb")
        self.__score(True)

    def __maze2(self):
        self.__filename = "mazeGames/mazeScores2.dat"
        self.__mazeScore.configure(bg="#addbeb")
        self.__mazeScore2.configure(bg="#ebf6fa")
        self.__guitarScores.configure(bg="#addbeb")
        self.__hangman.configure(bg="#addbeb")
        self.__totalScore.configure(bg="#addbeb")
        self.__score(True)

    def __guitarHero(self):
        self.__filename = "guitarHero/guitarHero.dat"
        self.__mazeScore.configure(bg="#addbeb")
        self.__mazeScore2.configure(bg="#addbeb")
        self.__guitarScores.configure(bg="#ebf6fa")
        self.__hangman.configure(bg="#addbeb")
        self.__totalScore.configure(bg="#addbeb")
        self.__score(False)

    def __hangman(self):
        self.__filename = "Hangman/hangmanScores.dat"
        self.__mazeScore.configure(bg="#addbeb")
        self.__mazeScore2.configure(bg="#addbeb")
        self.__guitarScores.configure(bg="#addbeb")
        self.__hangman.configure(bg="#ebf6fa")
        self.__totalScore.configure(bg="#addbeb")
        self.__score(True)

    def __total(self):
        self.__filename = "users.dat"
        self.__mazeScore.configure(bg="#addbeb")
        self.__mazeScore2.configure(bg="#addbeb")
        self.__guitarScores.configure(bg="#addbeb")
        self.__hangman.configure(bg="#addbeb")
        self.__totalScore.configure(bg="#ebf6fa")
        self.__loadTotal()

    def __loadTotal(self):
        ranks = ""
        try:
            myDict = pickle.load(open(self.__filename, "rb"))
            scoresList = []
            for key in myDict:
                scoresList.append(myDict[key][-1])

            if len(myDict) > 0:
                for i in range(3):
                    try:
                        highest = max(scoresList)
                        found = False
                        for key in myDict:
                            if not found and myDict[key][-1] == highest:
                                highKey = key
                                found = True
                        ranks += highKey + "     :    " + str(highest) + "\n"
                        myDict.pop(highKey)
                        scoresList.remove(max(scoresList))
                    except:
                        ranks += "None     :    --\n"
            else:
                ranks = "No scores yet!"
        except IOError:
            ranks = "Invalid Entry"
        self.__scoreLabel.configure(text=ranks)
    # normal refers to whether the high score if supposed to be the 
    # highest number of the lowest number
    def __score(self, normal):
        ranks = ""
        try:
            myDict = pickle.load(open(self.__filename, "rb"))
            scoresList = []
            for key in myDict:
                scoresList.append(myDict[key])

            if len(myDict) > 0:
                for i in range(3):
                    try:
                        highest = max(scoresList)
                        if not normal:
                            highest = min(scoresList)
                        found = False
                        for key in myDict:
                            if not found and myDict[key] == highest:
                                highKey = key
                                found = True
                        ranks += (highKey + "     :    " +
                                  str(myDict.pop(highKey)) + "\n")
                        if normal:
                            scoresList.remove(max(scoresList))
                        else:
                            scoresList.remove(min(scoresList))
                    except:
                        ranks += "None     :    --\n"
            else:
                ranks = "No scores yet!"
        except IOError:
            ranks = "Invalid Entry"
        self.__scoreLabel.configure(text=ranks)

