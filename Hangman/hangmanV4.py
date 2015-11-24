import pygame
import time
from pygame import font
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

displayWidth = 800
displayHeight = 600
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Hangman!")
icon = pygame.image.load("Hangman/hangman32.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
FPS = 10

smallFont = pygame.font.SysFont("comicsansms", 20)
medFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 80)


def getIndex(word, guess):
    idx = 0
    indexes = []
    for letter in word:
        if word[idx] == guess:
            indexes.append(idx)
        idx += 1
    return(indexes)


def gameIntro():
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    loop = False
                elif event.key == pygame.K_e:
                    pygame.quit()


        gameDisplay.fill(white)
        title = largeFont.render("Hangman!", True, black)
        explanation = smallFont.render("Press P to play or E to exit", True, black)
        gameDisplay.blit(title, (220, 200))
        gameDisplay.blit(explanation, (270, 400))
        pygame.display.update()
        clock.tick(4)


def gameEnd():
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return(False)
                elif event.key == pygame.K_e:
                    return(True)

        niceText = largeFont.render("Nice", True, red)
        jobText = largeFont.render("Job!", True, red)
        explanation = smallFont.render("Press P to play or E to exit", True, black)
        gameDisplay.blit(niceText, (550, 150))
        gameDisplay.blit(jobText, (550, 250))
        gameDisplay.blit(explanation, (525, 400))
        pygame.display.update()
        clock.tick(4)


def gameOver():
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return(False)
                elif event.key == pygame.K_e:
                    return(True)

        gameText = largeFont.render("Game", True, red)
        overText = largeFont.render("Over", True, red)
        explanation = smallFont.render("Press P to play or E to exit", True, black)
        gameDisplay.blit(gameText, (550, 150))
        gameDisplay.blit(overText, (550, 250))
        gameDisplay.blit(explanation, (525, 400))
        pygame.display.update()
        clock.tick(4)

def score(points, strikes, length, correctGuesses=[['', [0, 1]], ['', [2, 3]]], incorrectGuesses=[]):
    image0 = pygame.image.load("Hangman/hangman1000.png")
    image1 = pygame.image.load("Hangman/hangman1001.png")
    image2 = pygame.image.load("Hangman/hangman1002.png")
    image3 = pygame.image.load("Hangman/hangman1003.png")
    image4 = pygame.image.load("Hangman/hangman1004.png")
    image5 = pygame.image.load("Hangman/hangman1005.png")
    image6 = pygame.image.load("Hangman/hangman1006.png")
    gameDisplay.fill(white)
    pointsDisplay = smallFont.render("Score: " + str(points), True, black)
    strikesDisplay = smallFont.render("Strikes: " + str(strikes) + "/6", True, black)
    gameDisplay.blit(pointsDisplay, [0, 0])
    gameDisplay.blit(strikesDisplay, [100, 0])
    if strikes == 0:
        gameDisplay.blit(image0, [300, 150])
    elif strikes == 1:
        gameDisplay.blit(image1, [300, 150])
    elif strikes == 2:
        gameDisplay.blit(image2, [300, 150])
    elif strikes == 3:
        gameDisplay.blit(image3, [300, 150])
    elif strikes == 4:
        gameDisplay.blit(image4, [300, 150])
    elif strikes == 5:
        gameDisplay.blit(image5, [300, 150])
    elif strikes == 6:
        gameDisplay.blit(image6, [300, 150])

    guessPositionList = [[30, 300], [85, 300], [140, 300], [30, 350], [85, 350], [140, 350]]
    for index in range(len(incorrectGuesses)):
        letter = medFont.render(incorrectGuesses[index], True, black)
        gameDisplay.blit(letter, guessPositionList[index])
        pygame.display.update()


    # list of lists for the location of the lines
    positionList = []
    if length % 2 != 0:
        ctr = (9 - length) // 2
        positionList.append([(60 + (80 * ctr), 100), (110 + (80 * ctr), 100)])
        for location in range(length - 1):
            positionList.append([(positionList[-1][0][0] + 80, 100), (positionList[-1][0][0] + 130, 100)])
    else:
        ctr = (10 - length) // 2
        positionList.append([(20 + (80 * ctr), 100), (70 + (80 * ctr), 100)])
        for location in range(length - 1):
            positionList.append([(positionList[-1][0][0] + 80, 100), (positionList[-1][0][0] + 130, 100)])
    # print(positionList)

    # draw the lines
    for position in positionList:
        pygame.draw.line(gameDisplay, black, position[0], position[1], 4)


    ###### putting the letters in place
    for sequence in correctGuesses:
            letter = sequence[0]
            letter1 = medFont.render(letter, True, black)
            for idx in sequence[1]:
                gameDisplay.blit(letter1, [positionList[idx][0][0] + 10, 30])

    pygame.display.update()


def getLetter():
    keepGoing = True
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

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
                else:
                    guess = ''
                return(guess)

def gameLoop():
    gameDisplay.fill(white)
    pygame.display.update()

    over = False
    words = ["abhor", "acquiesce", "acronym", "alacrity", "ambiguity", "amiable", "analogy", "andragogy", "antonym", "appease", "arcane", "assonance", "avarice", "brazen", "brusque", "cajole", "callous", "candor", "chide", "coerce", "cognition", "coherent", "confidant", "connive", "contrived", "conundrum", "criterion", "debase", "decry", "deference", "demure", "deride", "despot", "dialect", "diction", "didactic", "diligent", "divergent", "egregious", "elated", "eloquence", "eloquent", "embezzle", "emergent", "empathy", "enigma", "enmity", "epiphany", "epitaph", "epitome", "erudite", "extol", "fabricate", "feral", "formative", "forsake", "fractious", "furtive", "gluttony", "haughty", "holistic", "homonym", "hubris", "hyperbole", "hypocrisy", "impudent", "incisive", "indolent", "inept", "infamy", "inhibit", "innate", "insular", "intrepid", "irony", "jargon", "jubilant", "knell", "lithe", "lurid", "maverick", "maxim", "mentor", "metaphor", "mnemonic", "modicum", "monologue", "morose", "motif", "myriad", "nadir", "nemesis", "nominal", "norms", "novice", "nuance", "obfuscate", "oblivious", "obtuse", "oxymoron", "panacea", "paradox", "parody", "pedagogy", "pedantic", "penchant", "perusal", "phonemes", "plethora", "pseudonym", "quaint", "rash", "refurbish", "repudiate", "rife", "rubric", "salient", "sardonic", "satire", "simile", "soliloquy", "staid", "sycophant", "syntax", "taciturn", "thesis", "truculent", "umbrage", "validity", "venerable", "vex", "virtual", "wanton", "zenith"]
    maximum = len(words) - 1
    points = 0
    while not over:
        strikes = 0
        correctGuesses = []
        randomIndex = random.randint(0, maximum)
        word = words[randomIndex]
        length = len(word)
        incorrectGuesses = []
        puzzle = ["__ "] * length
        score(points, strikes, length, incorrectGuesses)
        while strikes < 6 and "__ " in puzzle:
            guess = getLetter()
            if guess.isalpha():
                if guess not in incorrectGuesses:
                    if guess in word:
                        indexes = getIndex(word, guess)
                        if (guess, indexes) not in correctGuesses:
                            correctGuesses.append((guess, indexes))
                            for letter in word:
                                if letter == guess:
                                    points += 1
                            for index in indexes:
                                puzzle[index] = guess + ' '
                    else:
                        strikes += 1
                        incorrectGuesses.append(guess)
            score(points, strikes, length, correctGuesses, incorrectGuesses)
        if strikes == 6:
            for letter in word:
                indexes = getIndex(word, letter)
                correctGuesses.append((letter, indexes))
                score(points, strikes, length, correctGuesses, incorrectGuesses)
            if gameOver():
                over = True
            else:
                points = 0
        else:
            over = gameEnd()
    return(points)


def menu():
    gameIntro()
    finalScore = gameLoop()
    print("The final score was", finalScore)
    pygame.quit()

menu()
