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

import pygame
import time
from pygame import font
import random
import pickle


class Hangman:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Load online user
        self.__allUsers = pickle.load(open("users.dat", "rb"))
        self.__user = pickle.load(open("userOnline.dat", "rb"))
        self.__highScores = pickle.load(open("Hangman/hangmanScores.dat",
                                             "rb"))
        # Append score each time there is a game over
        # Load high score to total score to be shown
        self.__highestScore = 0
        try:
            self.__highestScore = self.__highScores[self.__user[0]]
        except KeyError:
            # User is new, so key above wont work
            self.__highScores[self.__user[0]] = 0

        # Define colors
        self.__white = (255, 255, 255)
        self.__black = (0, 0, 0)
        self.__red = (255, 0, 0)

        # Set dimensions of window
        self.__displayWidth = 800
        self.__displayHeight = 600

        # Import image to be used as icon
        self.__icon = pygame.image.load("Hangman/image/hangman32.png")

        # Create a window with given dimensions and a caption and picture
        self.__gameDisplay = pygame.display.set_mode((self.__displayWidth,
                                                      self.__displayHeight))
        pygame.display.set_caption("Hangman!")
        pygame.display.set_icon(self.__icon)

        # Define clock, which will determine framerate
        self.__clock = pygame.time.Clock()

        # Define fonts
        self.__smallFont = pygame.font.SysFont("comicsansms", 20)
        self.__medFont = pygame.font.SysFont("comicsansms", 50)
        self.__largeFont = pygame.font.SysFont("comicsansms", 80)
        ####
        ####
        self.__gameIntro()
        self.__exportToFile()

        # Once final number of points is returned, program is finished
        pygame.quit()

    # Narrative: For each correct letter, determine position of letter
    # within word
    def __getIndex(self, word, guess):
        # Create counter
        idx = 0

        # Create an empty list to which letter's indexes will be appended
        indexes = []

        # For each occurrence of the correct letter in word, append index to
        # list of indexes
        for letter in word:
            if word[idx] == guess:
                indexes.append(idx)

            # Increment counter
            idx += 1

        # Return list of indexes
        return(indexes)

    # Narrative: Display title screen
    def __gameIntro(self):
        # Create sentinel to ensure loop will begin
        loop = True

        while loop:

            # Collect keystrokes from user
            for event in pygame.event.get():

                # If user hits 'X' in top right corner, game closes
                if event.type == pygame.QUIT:
                    pygame.quit()

                # User hits 'P' to play or 'E' to exit
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        loop = False
                    elif event.key == pygame.K_e:
                        pygame.quit()

            # Fill window with white
            self.__gameDisplay.fill(self.__white)

            # Create variables for message text and color
            title = self.__largeFont.render("Hangman!", True, self.__black)
            explanation = self.__smallFont.render("Press P to play or" +
                                                  "E to exit", True,
                                                  self.__black)

            # Display text
            self.__gameDisplay.blit(title, (220, 200))
            self.__gameDisplay.blit(explanation, (270, 400))

            # Update display and move time forward
            pygame.display.update()
            self.__clock.tick(4)

    # Narrative: Display win screen; ask user to play again or exit
    def __winScreen(self):

        # Initialize sentinel to ensure loop begins
        loop = True

        while loop:

            # Collect keystrokes from user
            for event in pygame.event.get():

                # If user hits 'X' in top right corner, game closes
                if event.type == pygame.QUIT:
                    pygame.quit()

                # User hits 'P' to play or 'E' to exit
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return(False)
                    elif event.key == pygame.K_e:
                        return(True)

            # Create variables for message text and color
            niceText = self.__largeFont.render("Nice", True, self.__red)
            jobText = self.__largeFont.render("Job!", True, self.__red)
            explanation = self.__smallFont.render("Press P to play or E" +
                                                  "to exit", True,
                                                  self.__black)

            # Display text
            self.__gameDisplay.blit(niceText, (550, 150))
            self.__gameDisplay.blit(jobText, (550, 250))
            self.__gameDisplay.blit(explanation, (525, 400))

            # Update display and move time forward
            pygame.display.update()
            self.__clock.tick(4)

    # Narrative: Display game over screen
    def __loseScreen(self):
        # Initialize sentinel to ensure loop begins
        loop = True

        while loop:

            # Collect keystrokes from user
            for event in pygame.event.get():

                # If user hits 'X' in top right corner, game closes
                if event.type == pygame.QUIT:
                    pygame.quit()

                # User hits 'P' to play or 'E' to exit; returns Boolean
                # variable to gameLoop to continue or quit
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return(False)
                    elif event.key == pygame.K_e:
                        return(True)

            # Create variables for message text and color
            gameText = self.__largeFont.render("Game", True, self.__red)
            overText = self.__largeFont.render("Over", True, self.__red)
            explanation = self.__smallFont.render("Press P to play or E" +
                                                  "to exit", True,
                                                  self.__black)

            # Display text
            self.__gameDisplay.blit(gameText, (550, 150))
            self.__gameDisplay.blit(overText, (550, 250))
            self.__gameDisplay.blit(explanation, (525, 400))

            # Update display and move time forward
            pygame.display.update()
            self.__clock.tick(4)

    # Narrative: Display puzzle, points, and strikes to window
    def __displayToScreen(self, points, strikes, length,
                          correctGuesses=[['', [0, 1]], ['', [2, 3]]],
                          incorrectGuesses=[], localHigh=0):
        # Import images of figure with varying numbers of limbs
        zeroLimbs = pygame.image.load("Hangman/image/hangman1000.png")
        oneLimb = pygame.image.load("Hangman/image/hangman1001.png")
        twoLimbs = pygame.image.load("Hangman/image/hangman1002.png")
        threeLimbs = pygame.image.load("Hangman/image/hangman1003.png")
        fourLimbs = pygame.image.load("Hangman/image/hangman1004.png")
        fiveLimbs = pygame.image.load("Hangman/image/hangman1005.png")
        sixLimbs = pygame.image.load("Hangman/image/hangman1006.png")

        # Fill window with white
        self.__gameDisplay.fill(self.__white)

        # Create variables for "Score" and "Strikes" text and color; score
        # and strikes are displayed according to arguments passed to function
        pointsDisplay = self.__smallFont.render("Score: " + str(points),
                                                True, self.__black)
        strikesDisplay = self.__smallFont.render("Strikes: " + str(strikes) +
                                                 "/6", True, self.__black)
        localHighDisplay = self.__smallFont.render("Today's High: " +
                                                   str(localHigh), True,
                                                   self.__black)

        # Display score and strieks
        self.__gameDisplay.blit(pointsDisplay, [0, 0])
        self.__gameDisplay.blit(strikesDisplay, [100, 0])
        self.__gameDisplay.blit(localHighDisplay, [250, 0])

        # Display a different number of limbs according to number of strikes
        if strikes == 0:
            self.__gameDisplay.blit(zeroLimbs, [300, 150])
        elif strikes == 1:
            self.__gameDisplay.blit(oneLimb, [300, 150])
        elif strikes == 2:
            self.__gameDisplay.blit(twoLimbs, [300, 150])
        elif strikes == 3:
            self.__gameDisplay.blit(threeLimbs, [300, 150])
        elif strikes == 4:
            self.__gameDisplay.blit(fourLimbs, [300, 150])
        elif strikes == 5:
            self.__gameDisplay.blit(fiveLimbs, [300, 150])
        elif strikes == 6:
            self.__gameDisplay.blit(sixLimbs, [300, 150])

        # Create a list of coordinates for incorrect guesses
        guessPositionList = [[30, 300], [85, 300], [140, 300], [30, 350],
                             [85, 350], [140, 350]]

        # Loop through list of incorrect guesses
        for index in range(len(incorrectGuesses)):

            # Create variable whose text is an incorrect letter
            letter = self.__medFont.render(incorrectGuesses[index],
                                           True, self.__black)

            # Display incorrect guesses in order guessed
            self.__gameDisplay.blit(letter, guessPositionList[index])

            # Update display
            pygame.display.update()

        # Create a list to which line coordinates will be appended
        positionList = []

        # If the length of the puzzle is odd, line position is determined by
        # this formula
        if length % 2 != 0:
            ctr = (9 - length) // 2
            positionList.append([(60 + (80 * ctr), 100),
                                 (110 + (80 * ctr), 100)])
            for location in range(length - 1):
                positionList.append([(positionList[-1][0][0] + 80, 100),
                                     (positionList[-1][0][0] + 130, 100)])

        # If the length of the puzzle is even, line position is determined by
        # this formula
        else:
            ctr = (10 - length) // 2
            positionList.append([(20 + (80 * ctr), 100),
                                 (70 + (80 * ctr), 100)])
            for location in range(length - 1):
                positionList.append([(positionList[-1][0][0] + 80, 100),
                                     (positionList[-1][0][0] + 130, 100)])

        # Display lines in window
        for position in positionList:
            pygame.draw.line(self.__gameDisplay, self.__black,
                             position[0], position[1], 4)

        # correctGuesses is a list of [letter, [list-of-indexes]] sequences
        for sequence in correctGuesses:

                # Letter is the first item in the sequence
                letter = sequence[0]

                # Create variable for each letter indicating text,
                # font, and color
                letter1 = self.__medFont.render(letter, True, self.__black)

                # Indexes are a list at index 1 in the sequence
                for idx in sequence[1]:

                    # Display letter above each line corresponding
                    # to letter's indexes
                    self.__gameDisplay.blit(letter1,
                                            [positionList[idx][0][0] + 10, 30])

        # Update display
        pygame.display.update()

    # Narrative: Collect user input to determine guessed letter
    def __getLetter(self):
        # Initialize sentinel to ensure loop
        keepGoing = True

        while keepGoing:

            # Collect keystrokes from user
            for event in pygame.event.get():

                # If user hits 'X' in top right corner, game closes
                if event.type == pygame.QUIT:
                    pygame.quit()

                # If user types a letter, it is returned as guessed letter
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        guess = 'a'
                    elif event.key == pygame.K_b:
                        guess = 'b'
                    elif event.key == pygame.K_c:
                        guess = 'c'
                    elif event.key == pygame.K_d:
                        guess = 'd'
                    elif event.key == pygame.K_e:
                        guess = 'e'
                    elif event.key == pygame.K_f:
                        guess = 'f'
                    elif event.key == pygame.K_g:
                        guess = 'g'
                    elif event.key == pygame.K_h:
                        guess = 'h'
                    elif event.key == pygame.K_i:
                        guess = 'i'
                    elif event.key == pygame.K_j:
                        guess = 'j'
                    elif event.key == pygame.K_k:
                        guess = 'k'
                    elif event.key == pygame.K_l:
                        guess = 'l'
                    elif event.key == pygame.K_m:
                        guess = 'm'
                    elif event.key == pygame.K_n:
                        guess = 'n'
                    elif event.key == pygame.K_o:
                        guess = 'o'
                    elif event.key == pygame.K_p:
                        guess = 'p'
                    elif event.key == pygame.K_q:
                        guess = 'q'
                    elif event.key == pygame.K_r:
                        guess = 'r'
                    elif event.key == pygame.K_s:
                        guess = 's'
                    elif event.key == pygame.K_t:
                        guess = 't'
                    elif event.key == pygame.K_u:
                        guess = 'u'
                    elif event.key == pygame.K_v:
                        guess = 'v'
                    elif event.key == pygame.K_w:
                        guess = 'w'
                    elif event.key == pygame.K_x:
                        guess = 'x'
                    elif event.key == pygame.K_y:
                        guess = 'y'
                    elif event.key == pygame.K_z:
                        guess = 'z'

                    # If user presses a key that isn't a letter,
                    # '' is returned; gameLoop() recognizes invalid guess
                    else:
                        guess = ''

                    return(guess)

    # Narrative: Create a puzzle of blank letters; allow user to guess letters
    # and fill in puzzle, awarding points for correct guesses
    def __gameLoop(self):
        # Fill window with white
        self.__gameDisplay.fill(self.__white)

        # Update display
        pygame.display.update()

        # Initialize sentinel to determine whether game should loop again
        over = False

        # List of all potential words
        words = ["abhor", "acquiesce", "acronym", "alacrity", "ambiguity",
                 "amiable", "analogy", "andragogy", "antonym", "appease",
                 "arcane", "assonance", "avarice", "brazen", "brusque",
                 "cajole", "callous", "candor", "chide", "coerce", "cognition",
                 "coherent", "confidant", "connive", "contrived", "conundrum",
                 "criterion", "debase", "decry", "deference", "demure",
                 "deride", "despot", "dialect", "diction", "didactic",
                 "diligent", "divergent", "egregious", "elated", "eloquence",
                 "eloquent", "embezzle", "emergent", "empathy", "enigma",
                 "enmity", "epiphany", "epitaph", "epitome", "erudite",
                 "extol", "fabricate", "feral", "formative", "forsake",
                 "fractious", "furtive", "gluttony", "haughty", "holistic",
                 "homonym", "hubris", "hyperbole", "hypocrisy", "impudent",
                 "incisive", "indolent", "inept", "infamy", "inhibit",
                 "innate", "insular", "intrepid", "irony", "jargon",
                 "jubilant", "knell", "lithe", "lurid", "maverick", "maxim",
                 "mentor", "metaphor", "mnemonic", "modicum", "monologue",
                 "morose", "motif", "myriad", "nadir", "nemesis", "nominal",
                 "norms", "novice", "nuance", "obfuscate", "oblivious",
                 "obtuse", "oxymoron", "panacea", "paradox", "parody",
                 "pedagogy", "pedantic", "penchant", "perusal", "phonemes",
                 "plethora", "pseudonym", "quaint", "rash", "refurbish",
                 "repudiate", "rife", "rubric", "salient", "sardonic",
                 "satire", "simile", "soliloquy", "staid", "sycophant",
                 "syntax", "taciturn", "thesis", "truculent", "umbrage",
                 "validity", "venerable", "vex", "virtual", "wanton", "zenith"]

        # Sets the maximum value for the random index
        maximum = len(words) - 1

        # Initialize points variable
        points = 0

        # Create list to which scores will be appended
        scores = []

        # Create a variable for this session's high score
        localHigh = 0

        # Game loops until "over" is set to True upon game's end
        while not over:
            # At the beginning of each round, set strikes to 0
            strikes = 0

            # pick a random word from the list
            randomIndex = random.randint(0, maximum)
            word = words[randomIndex]

            # Save length of puzzle into variable
            length = len(word)

            # Initialize a list for correct letters and their indexes
            correctGuesses = []

            # Initialize a list for incorrect guesses
            incorrectGuesses = []

            # Create a puzzle variable with "__ " as a placeholder
            # for each letter
            puzzle = ["__ "] * length

            # Display current status of game until guess is made
            self.__displayToScreen(points, strikes, length, incorrectGuesses,
                                   localHigh=localHigh)

            # Loop as long as user hasn't run out of strikes or
            # completed puzzle
            while strikes < 6 and "__ " in puzzle:
                # Collect keystroke for guess
                guess = self.__getLetter()

                # Guess must be unique and be a letter; '', which is returned
                # if the user types a non-letter character, will not pass
                if guess.isalpha():
                    if guess not in incorrectGuesses:

                        # Checks whether guess is correct
                        if guess in word:

                            # Get a list of indexes at which letter occurs
                            indexes = self.__getIndex(word, guess)

                            # Correct guess must be unique
                            if (guess, indexes) not in correctGuesses:

                                # Append letter and indexes to list of
                                # correct guesses
                                correctGuesses.append((guess, indexes))

                                # Add a point to Score for each
                                # occurrence of the guess
                                for letter in word:
                                    if letter == guess:
                                        points += 1

                                # Replace the "__ " placeholder
                                for index in indexes:
                                    puzzle[index] = guess + ' '

                        # If guess is incorrect
                        else:
                            # Add 1 to strikes
                            strikes += 1

                            # Append incorrect guess to incorrectGuess list
                            incorrectGuesses.append(guess)

                # Display new status of game to window
                self.__displayToScreen(points, strikes, length,
                                       correctGuesses, incorrectGuesses,
                                       localHigh=localHigh)

            # Once user has 6 strikes or the puzzle has no more placeholders,
            # the game is over

            # If user has 6 strikes, game is over with a loss
            if strikes == 6:

                # Regardless of what the user guessed, append the rest of the
                # letters to correctGuesses so they are displayed, but user
                # receives no points
                for letter in word:
                    indexes = self.__getIndex(word, letter)
                    correctGuesses.append((letter, indexes))

                    # Display new status of game to window
                    self.__displayToScreen(points, strikes, length,
                                           correctGuesses, incorrectGuesses,
                                           localHigh=localHigh)

                # loseScreen() returns a Boolean variable determining whether
                # or not game should loop again
                if self.__loseScreen():
                    """# Append user's score to list of scores
                    scores.append(points)
                    print(scores)"""

                    # If user chooses to quit, loop ends
                    over = True

                # If user chooses to play again, loop begins again, and user
                # starts with 0 points
                else:
                    # Append user's score to list of scores
                    scores.append(points)
                    localHigh = max(scores)

                    # Reset user's score
                    points = 0

            # If user finishes the puzzle without 6 srikes, then they won
            else:
                # winScreen() returns a Boolean variable determining whether
                # or not game should loop again
                over = self.__winScreen()

        # Append user's score to list of scores
        scores.append(points)
        localHigh = max(scores)

        # When user chooses to finish, number of points is returned to menu()
        return(scores)

    # Narrative: Record points
    def __exportToFile(self):
        try:
            # Call gameLoop()
            localScores = self.__gameLoop()

        except:
            num = 1

        else:
            # Add to high score
            if max(localScores) > self.__highScores[self.__user[0]]:
                self.__highScores[self.__user[0]] = max(localScores)
                pickle.dump(self.__highScores, open("Hangman/hangmanScores.dat",
                                                    "wb"))

            # Add to total score
            self.__user[-1] = (self.__allUsers[self.__user[0]][-1] +
                               sum(localScores))
            self.__allUsers[self.__user[0]] = self.__user
            pickle.dump(self.__allUsers, open("users.dat", "wb"))
