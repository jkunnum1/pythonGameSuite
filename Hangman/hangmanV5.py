import pygame
import time
from pygame import font
import random
import pickle

# Initialize pygame
pygame.init()





############################
'''LOAD ONLINE USER'''
allUsers = pickle.load(open("users.dat", "rb"))
user = pickle.load(open("userOnline.dat", "rb"))
highScores = pickle.load(open("Hangman/hangmanScores.dat", "rb"))
############################
#  append score each time there is a game over  #
### LOAD HIGHSCORE TO TOTAL SCORE TO BE SHOWN ###
highestScore = 0
try:
    highestScore = highScores[user[0]]
except KeyError:
    # User is new, so key above wont work
    highScores[user[0]] = 0








# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set dimensions of window
displayWidth = 800
displayHeight = 600

# Import image to be used as icon
icon = pygame.image.load("Hangman/hangman32.png")

# Create a window with given dimensions and a caption and picture
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Hangman!")
pygame.display.set_icon(icon)

# Define clock, which will determine framerate
clock = pygame.time.Clock()

# Define fonts
smallFont = pygame.font.SysFont("comicsansms", 20)
medFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 80)


def writeToFile():
    ###### SAVE HIGH SCORE ######
    highScores[user[0]] = score
    pickle.dump(highScores, open("hangmanScores.dat", "wb"))
    #############################


##Narrative: For each correct letter, determine position of letter within word
def getIndex(word, guess):
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


##Narrative: Display title screen
def gameIntro():
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
        gameDisplay.fill(white)

        # Create variables for message text and color
        title = largeFont.render("Hangman!", True, black)
        explanation = smallFont.render("Press P to play or E to exit", True, black)

        # Display text
        gameDisplay.blit(title, (220, 200))
        gameDisplay.blit(explanation, (270, 400))


        # Update display and move time forward
        pygame.display.update()
        clock.tick(4)


##Narrative: Display win screen; ask user to play again or exit
def winScreen():

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
        niceText = largeFont.render("Nice", True, red)
        jobText = largeFont.render("Job!", True, red)
        explanation = smallFont.render("Press P to play or E to exit", True, black)

        # Display text
        gameDisplay.blit(niceText, (550, 150))
        gameDisplay.blit(jobText, (550, 250))
        gameDisplay.blit(explanation, (525, 400))

        # Update display and move time forward
        pygame.display.update()
        clock.tick(4)


##Narrative: Display game over screen
def loseScreen():
    # Initialize sentinel to ensure loop begins
    loop = True

    while loop:

        # Collect keystrokes from user
        for event in pygame.event.get():

            # If user hits 'X' in top right corner, game closes
            if event.type == pygame.QUIT:
                pygame.quit()

            # User hits 'P' to play or 'E' to exit; returns Boolean variable
            # to gameLoop to continue or quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return(False)
                elif event.key == pygame.K_e:
                    return(True)

        # Create variables for message text and color
        gameText = largeFont.render("Game", True, red)
        overText = largeFont.render("Over", True, red)
        explanation = smallFont.render("Press P to play or E to exit", True, black)

        # Display text
        gameDisplay.blit(gameText, (550, 150))
        gameDisplay.blit(overText, (550, 250))
        gameDisplay.blit(explanation, (525, 400))

        # Update display and move time forward
        pygame.display.update()
        clock.tick(4)


##Narrative: Display puzzle, points, and strikes to window
def displayToScreen(points, strikes, length, correctGuesses=[['', [0, 1]], ['', [2, 3]]], incorrectGuesses=[], localHigh=0):
    # Import images of figure with varying numbers of limbs
    zeroLimbs = pygame.image.load("Hangman/hangman1000.png")
    oneLimb = pygame.image.load("Hangman/hangman1001.png")
    twoLimbs = pygame.image.load("Hangman/hangman1002.png")
    threeLimbs = pygame.image.load("Hangman/hangman1003.png")
    fourLimbs = pygame.image.load("Hangman/hangman1004.png")
    fiveLimbs = pygame.image.load("Hangman/hangman1005.png")
    sixLimbs = pygame.image.load("Hangman/hangman1006.png")

    # Fill window with white
    gameDisplay.fill(white)

    # Create variables for "Score" and "Strikes" text and color; score
    # and strikes are displayed according to arguments passed to function
    pointsDisplay = smallFont.render("Score: " + str(points), True, black)
    strikesDisplay = smallFont.render("Strikes: " + str(strikes) + "/6", True, black)
    localHighDisplay = smallFont.render("Today's High: " + str(localHigh), True, black)

    # Display score and strieks
    gameDisplay.blit(pointsDisplay, [0, 0])
    gameDisplay.blit(strikesDisplay, [100, 0])
    gameDisplay.blit(localHighDisplay, [250, 0])

    # Display a different number of limbs according to number of strikes
    if strikes == 0:
        gameDisplay.blit(zeroLimbs, [300, 150])
    elif strikes == 1:
        gameDisplay.blit(oneLimb, [300, 150])
    elif strikes == 2:
        gameDisplay.blit(twoLimbs, [300, 150])
    elif strikes == 3:
        gameDisplay.blit(threeLimbs, [300, 150])
    elif strikes == 4:
        gameDisplay.blit(fourLimbs, [300, 150])
    elif strikes == 5:
        gameDisplay.blit(fiveLimbs, [300, 150])
    elif strikes == 6:
        gameDisplay.blit(sixLimbs, [300, 150])

    # Create a list of coordinates for incorrect guesses
    guessPositionList = [[30, 300], [85, 300], [140, 300], [30, 350], [85, 350], [140, 350]]

    # Loop through list of incorrect guesses
    for index in range(len(incorrectGuesses)):

        # Create variable whose text is an incorrect letter
        letter = medFont.render(incorrectGuesses[index], True, black)

        # Display incorrect guesses in order guessed
        gameDisplay.blit(letter, guessPositionList[index])

        # Update display
        pygame.display.update()


    # Create a list to which line coordinates will be appended
    positionList = []

    # If the length of the puzzle is odd, line position is determined by
    # the formula ??????????????
    if length % 2 != 0:
        ctr = (9 - length) // 2
        positionList.append([(60 + (80 * ctr), 100), (110 + (80 * ctr), 100)])
        for location in range(length - 1):
            positionList.append([(positionList[-1][0][0] + 80, 100), (positionList[-1][0][0] + 130, 100)])

    # If the length of the puzzle is even, line position is determined by
    # the formula ??????????????
    else:
        ctr = (10 - length) // 2
        positionList.append([(20 + (80 * ctr), 100), (70 + (80 * ctr), 100)])
        for location in range(length - 1):
            positionList.append([(positionList[-1][0][0] + 80, 100), (positionList[-1][0][0] + 130, 100)])

    # Display lines in window
    for position in positionList:
        pygame.draw.line(gameDisplay, black, position[0], position[1], 4)


    # correctGuesses is a list of [letter, [list-of-indexes]] sequences
    for sequence in correctGuesses:

            # Letter is the first item in the sequence
            letter = sequence[0]

            # Create variable for each letter indicating text, font, and color
            letter1 = medFont.render(letter, True, black)

            # Indexes are a list at index 1 in the sequence
            for idx in sequence[1]:

                # Display letter above each line corresponding to letter's
                # indexes
                gameDisplay.blit(letter1, [positionList[idx][0][0] + 10, 30])

    # Update display
    pygame.display.update()


##Narrative: Collect user input to determine guessed letter
def getLetter():
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

                # If user presses a key that isn't a letter, '' is returned;
                # gameLoop() recognizes invalid guess
                else:
                    guess = ''

                return(guess)

def gameLoop():
    # Fill window with white
    gameDisplay.fill(white)

    # Update display
    pygame.display.update()

    # Initialize sentinel to determine whether game should loop again
    over = False

    # List of all potential words
    words = ["abhor", "acquiesce", "acronym", "alacrity", "ambiguity", "amiable", "analogy", "andragogy", "antonym", "appease", "arcane", "assonance", "avarice", "brazen", "brusque", "cajole", "callous", "candor", "chide", "coerce", "cognition", "coherent", "confidant", "connive", "contrived", "conundrum", "criterion", "debase", "decry", "deference", "demure", "deride", "despot", "dialect", "diction", "didactic", "diligent", "divergent", "egregious", "elated", "eloquence", "eloquent", "embezzle", "emergent", "empathy", "enigma", "enmity", "epiphany", "epitaph", "epitome", "erudite", "extol", "fabricate", "feral", "formative", "forsake", "fractious", "furtive", "gluttony", "haughty", "holistic", "homonym", "hubris", "hyperbole", "hypocrisy", "impudent", "incisive", "indolent", "inept", "infamy", "inhibit", "innate", "insular", "intrepid", "irony", "jargon", "jubilant", "knell", "lithe", "lurid", "maverick", "maxim", "mentor", "metaphor", "mnemonic", "modicum", "monologue", "morose", "motif", "myriad", "nadir", "nemesis", "nominal", "norms", "novice", "nuance", "obfuscate", "oblivious", "obtuse", "oxymoron", "panacea", "paradox", "parody", "pedagogy", "pedantic", "penchant", "perusal", "phonemes", "plethora", "pseudonym", "quaint", "rash", "refurbish", "repudiate", "rife", "rubric", "salient", "sardonic", "satire", "simile", "soliloquy", "staid", "sycophant", "syntax", "taciturn", "thesis", "truculent", "umbrage", "validity", "venerable", "vex", "virtual", "wanton", "zenith"]

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

        # Create a puzzle variable with "__ " as a placeholder for each letter
        puzzle = ["__ "] * length

        # Display current status of game until guess is made
        displayToScreen(points, strikes, length, incorrectGuesses, localHigh=localHigh)

        # Loop as long as user hasn't run out of strikes or completed puzzle
        while strikes < 6 and "__ " in puzzle:
            # Collect keystroke for guess
            guess = getLetter()

            # Guess must be unique and be a letter; '', which is returned
            # if the user types a non-letter character, will not pass
            if guess.isalpha():
                if guess not in incorrectGuesses:

                    # Checks whether guess is correct
                    if guess in word:

                        # Get a list of indexes at which letter occurs
                        indexes = getIndex(word, guess)

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
            displayToScreen(points, strikes, length, correctGuesses, incorrectGuesses, localHigh=localHigh)

        # Once user has 6 strikes or the puzzle has no more placeholders,
        # the game is over

        # If user has 6 strikes, game is over with a loss
        if strikes == 6:

            # Regardless of what the user guessed, append the rest of the
            # letters to correctGuesses so they are displayed, but user
            # receives no points
            for letter in word:
                indexes = getIndex(word, letter)
                correctGuesses.append((letter, indexes))

                # Display new status of game to window
                displayToScreen(points, strikes, length, correctGuesses, incorrectGuesses, localHigh=localHigh)

            # loseScreen() returns a Boolean variable determining whether
            # or not game should loop again
            if loseScreen():
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
            over = winScreen()

    # Append user's score to list of scores
    scores.append(points)
    localHigh = max(scores)

    # When user chooses to finish, number of points is returned to menu()
    return(scores)


def menu():
    gameIntro()
    localScores = gameLoop()
    ##### ADD TO HIGH SCORE  ######
    if max(localScores) > highScores[user[0]]:
        highScores[user[0]] = max(localScores)
        pickle.dump(highScores, open("Hangman/hangmanScores.dat", "wb"))
    ##### ADD TO THE TOTAL SCORE #####
    user[-1] = allUsers[user[0]][-1] + sum(localScores)
    allUsers[user[0]] = user
    pickle.dump(allUsers, open("users.dat", "wb"))
    ##################################

    # Once final number of points is returned, program is finished
    pygame.quit()

menu()
