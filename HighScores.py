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

class HighScores:
	def __init__(self):
		#main window
		self.__mainWindow = tkinter.Tk()
		self.__mainWindow.wm_title("High Scores")
		self.__mainWindow.configure(background="#004c66")

		#button frame
		self.__buttons = tkinter.Frame(self.__mainWindow)
		self.__buttons.configure(background="#004c66")

		#scores frame
		self.__content = tkinter.Frame(self.__mainWindow)
		self.__content.configure(background="#004c66")

		self.__filename = ""
		
		self.__totalScore = tkinter.Button(self.__buttons, relief =\
                "groove", text = "Total Scores", command = self.__total,\
                bg="#c2e4f0", activebackground="#d6edf5", border=0,\
                font=("fixedsys", 6))

		self.__mazeScore = tkinter.Button(self.__buttons, relief =\
                "groove", text = "Maze Game", command = self.__maze1,\
                bg="#c2e4f0", activebackground="#d6edf5", border=0,\
                font=("fixedsys", 6))

		
		self.__mazeScore2 = tkinter.Button(self.__buttons, relief =\
                "groove", text = "Maze Game 2", command = self.__maze2,\
                bg="#c2e4f0", activebackground="#d6edf5", border=0,\
                font=("fixedsys", 6))

		
		self.__guitarScores = tkinter.Button(self.__buttons, relief =\
                "groove",text = "Guitar Hero", command = self.__guitarHero,\
                bg="#c2e4f0", activebackground="#d6edf5", border=0,\
                font=("fixedsys", 6))

		
		self.__hangman = tkinter.Button(self.__buttons, relief =\
                "groove", text = "Hangman", command = self.__hangman,\
                bg="#c2e4f0", activebackground="#d6edf5", border=0,\
                font=("fixedsys", 6))

		
		self.__quitButton = tkinter.Button(self.__buttons,\
                relief = "groove", text = "Quit", command = \
                self.__mainWindow.destroy, bg="#c2e4f0", activebackground=\
                "#d6edf5", border=0, font=("fixedsys", 6))

		self.__scoreLabel = tkinter.Label(self.__content, text='',\
                        font=("fixedsys",10), fg="#ff9900", bg="#d6edf5")

		self.__mainWindow.geometry("350x100")
		self.__buttons.grid()
		self.__content.grid(row=1)
		self.__mazeScore.grid(row=0, column=0, sticky=E, padx=1)
		self.__mazeScore2.grid(row=0, column=2,sticky=E, padx=1)
		self.__guitarScores.grid(row=0, column=4, sticky=E, padx=1)
		self.__hangman.grid(row=0, column=6, sticky=E, padx=1)
		self.__totalScore.grid(row=0, column=8, sticky=E, padx=1)
		self.__quitButton.grid(row=0, column=10, sticky=E, padx=1)
		self.__scoreLabel.grid(rowspan=5, columnspan=5, sticky=E, padx=1)

		tkinter.mainloop()

	def __maze1(self):
		self.__filename = "mazeGames/mazeScores.dat"
		self.__mazeScore.configure(state="active")
		self.__mazeScore2.configure(state="normal")
		self.__guitarScores.configure(state="normal")
		self.__hangman.configure(state="normal")
		self.__totalScore.configure(state="normal")
		self.__score()

	def __maze2(self):
		self.__filename = "mazeGames/mazeScores2.dat"
		self.__mazeScore.configure(state="normal")
		self.__mazeScore2.configure(state="active")
		self.__guitarScores.configure(state="normal")
		self.__hangman.configure(state="normal")
		self.__totalScore.configure(state="normal")
		self.__score()

	def __guitarHero(self):
		self.__filename = "guitarHero/guitarHero.dat"
		self.__mazeScore.configure(state="normal")
		self.__mazeScore2.configure(state="normal")
		self.__guitarScores.configure(state="active")
		self.__hangman.configure(state="normal")
		self.__totalScore.configure(state="normal")
		self.__score()

	def __hangman(self):
		self.__filename = "Hangman/hangmanScores.dat"
		self.__mazeScore.configure(state="normal")
		self.__mazeScore2.configure(state="normal")
		self.__guitarScores.configure(state="normal")
		self.__hangman.configure(state="active")
		self.__totalScore.configure(state="normal")
		self.__score()

	def __total(self):
		self.__filename = "users.dat"
		self.__mazeScore.configure(state="normal")
		self.__mazeScore2.configure(state="normal")
		self.__guitarScores.configure(state="normal")
		self.__hangman.configure(state="normal")
		self.__totalScore.configure(state="active")
		self.__loadTotal()

	def __loadTotal(self):
		ranks = ""
		try:
			myDict = pickle.load(open(self.__filename, "rb"))
			scoresList = []
			for key in myDict:
				scoresList.append(myDict[key][-1])

			if len(myDict) > 0:
				if len(myDict) > 3:
					numScores = 3
				else:
					numScores = 1
				for i in range(numScores):
					highest = max(scoresList)
					found = False
					for key in myDict:
						if not found and myDict[key][-1] == highest:
							highKey = key
							found = True
					ranks += highKey +  "     :    " + str(highest) + "\n"
					myDict.pop(highKey)
					scoresList.remove(max(scoresList))
			else:
				ranks = "No scores yet!"
		except IOError:
			ranks = "Invalid Entry"
		self.__scoreLabel.configure(text=ranks)

	def __score(self):
		ranks = ""
		try:
			myDict = pickle.load(open(self.__filename, "rb"))
			scoresList = []
			for key in myDict:
				scoresList.append(myDict[key])

			if len(myDict) > 0:
				if len(myDict) > 3:
					numScores = 3
				else:
					numScores = 1
				for i in range(numScores):
					highest = max(scoresList)
					found = False
					for key in myDict:
						if not found and myDict[key] == highest:
							highKey = key
							found = True
					ranks += highKey +  "     :    " + str(myDict.pop(highKey)) + "\n"
					scoresList.remove(max(scoresList))
			else:
				ranks = "No scores yet!"
		except IOError:
			ranks = "Invalid Entry"
		self.__scoreLabel.configure(text=ranks)

