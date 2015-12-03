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

import tkinter

import tkinter.messagebox

class HighScores:
	def __init__(self):
		#main window
		self.__mainWindow = tkinter.Tk()

		#button frame
		self.__buttons = tkinter.Frame(self.__mainWindow)

		#scores frame
		self.__content = tkinter.Frame(self.__mainWindow)

		self.__filename = ""
		self.__mazeScore = tkinter.Button(self.__buttons, relief = "groove",\
                           text = "Maze Game", command = self.__maze1)
		self.__mazeScore2 = tkinter.Button(self.__buttons, relief = "groove",\
                           text = "Maze Game 2", command = self.__maze2)
		self.__guitarScores = tkinter.Button(self.__buttons, relief = "groove",\
                           text = "Guitar Hero", command = self.__guitarHero)
		self.__hangman = tkinter.Button(self.__buttons, relief = "groove",\
                           text = "Hangman", command = self.__hangman)
		self.__quitButton = tkinter.Button(self.__buttons, relief = "groove",\
                            text = "Quit", command =  self.__mainWindow.destroy)

		self.__scoreLabel = tkinter.Label(self.__content, text='')

		self.__mainWindow.geometry("350x100")
		self.__buttons.grid()
		self.__content.grid(row=1)
		self.__mazeScore.grid(row=0, column=0)
		self.__mazeScore2.grid(row=0, column=2)
		self.__guitarScores.grid(row=0, column=4)
		self.__hangman.grid(row=0, column=6)
		self.__quitButton.grid(row=0, column=8)
		self.__scoreLabel.grid(rowspan=5, columnspan=5)

		tkinter.mainloop()

	def __maze1(self):
		self.__filename = "mazeGames/mazeScores.dat"
		self.__score()

	def __maze2(self):
		self.__filename = "mazeGames/mazeScores2.dat"
		self.__score()

	def __guitarHero(self):
		self.__filename = "guitarHero/guitarHero.dat"
		self.__score()

	def __hangman(self):
		self.__filename = "Hangman/hangmanScores.dat"
		self.__score()

	def __score(self):
		try:
			myDict = pickle.load(open(self.__filename, "rb"))
			scoresList = []
			for key in myDict:
				scoresList.append(myDict[key])

			ranks = ""
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
				self.__scoreLabel.configure(text=ranks)
			else:
				tkinter.messagebox.showinfo("ERROR", "No scores yet!")
		except IOError:
			tkinter.messagebox.showinfo("ERROR", "Invalid Entry")
