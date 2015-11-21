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
icon = pygame.image.load("hangman32.png")
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
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        text = largeFont.render("Hangman!", True, black)
        explanation = smallFont.render("Press C to play or Q to quit", True, black)
        gameDisplay.blit(text, (220, 200))
        gameDisplay.blit(explanation, (250, 400))
        pygame.display.update()
        clock.tick(4)


def gameEnd():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return(False)
                elif event.key == pygame.K_q:
                    return(True)

        text = largeFont.render("Nice", True, red)
        text3 = largeFont.render("Job!", True, red)
        text2 = smallFont.render("C for play, Q for quit", True, black)
        gameDisplay.blit(text, (550, 150))
        gameDisplay.blit(text3, (550, 250))
        gameDisplay.blit(text2, (550, 400))
        pygame.display.update()
        clock.tick(4)


def gameOver():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return(False)
                elif event.key == pygame.K_q:
                    return(True)

        text = largeFont.render("Game", True, red)
        text3 = largeFont.render("Over", True, red)
        text2 = smallFont.render("C for play, Q for quit", True, black)
        gameDisplay.blit(text, (550, 150))
        gameDisplay.blit(text3, (550, 250))
        gameDisplay.blit(text2, (550, 400))
        pygame.display.update()
        clock.tick(4)

def score(points, strikes, length, exportGuesses=[['', [0, 1]], ['', [2, 3]]], guessList=[]):
    image0 = pygame.image.load("hangman1000.png")
    image1 = pygame.image.load("hangman1001.png")
    image2 = pygame.image.load("hangman1002.png")
    image3 = pygame.image.load("hangman1003.png")
    image4 = pygame.image.load("hangman1004.png")
    image5 = pygame.image.load("hangman1005.png")
    image6 = pygame.image.load("hangman1006.png")
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


    for letter in guessList:
        if guessList[0] == letter:
            letter = medFont.render(letter, True, black)
            gameDisplay.blit(letter, [30, 300])
            pygame.display.update()
        elif guessList[1] == letter:
            letter = medFont.render(",  " + letter, True, black)
            gameDisplay.blit(letter, [60, 300])
            pygame.display.update()
        elif guessList[2] == letter:
            letter = medFont.render(",  " + letter, True, black)
            gameDisplay.blit(letter, [140, 300])
            pygame.display.update()
        elif guessList[3] == letter:
            letter = medFont.render(letter, True, black)
            gameDisplay.blit(letter, [30, 350])
            pygame.display.update()
        elif guessList[4] == letter:
            letter = medFont.render(",  " + letter, True, black)
            gameDisplay.blit(letter, [60, 350])
            pygame.display.update()
        else:
            letter = medFont.render(",  " + letter, True, black)
            gameDisplay.blit(letter, [140, 350])
            pygame.display.update()

    if length == 3:
        pygame.draw.line(gameDisplay, black, (300, 100), (350, 100), 4)
        pygame.draw.line(gameDisplay, black, (380, 100), (430, 100), 4)
        pygame.draw.line(gameDisplay, black, (460, 100), (510, 100), 4)

        for sequence in exportGuesses:
            letter = sequence[0]
            letter1 = medFont.render(letter, True, black)
            for idx in sequence[1]:
                if idx == 0:
                    gameDisplay.blit(letter1, [310, 30])
                elif idx == 1:
                    gameDisplay.blit(letter1, [390, 30])
                else:
                    gameDisplay.blit(letter1, [470, 30])

    elif length == 4:
        pygame.draw.line(gameDisplay, black, (260, 100), (310, 100), 4)
        pygame.draw.line(gameDisplay, black, (340, 100), (390, 100), 4)
        pygame.draw.line(gameDisplay, black, (420, 100), (470, 100), 4)
        pygame.draw.line(gameDisplay, black, (500, 100), (550, 100), 4)

        for sequence in exportGuesses:
            letter = sequence[0]
            letter1 = medFont.render(letter, True, black)
            for idx in sequence[1]:
                if idx == 0:
                    gameDisplay.blit(letter1, [270, 30])
                elif idx == 1:
                    gameDisplay.blit(letter1, [350, 30])
                elif idx == 2:
                    gameDisplay.blit(letter1, [430, 30])
                else:
                    gameDisplay.blit(letter1, [510, 30])

    elif length == 5:
        pygame.draw.line(gameDisplay, black, (220, 100), (270, 100), 4)
        pygame.draw.line(gameDisplay, black, (300, 100), (350, 100), 4)
        pygame.draw.line(gameDisplay, black, (380, 100), (430, 100), 4)
        pygame.draw.line(gameDisplay, black, (460, 100), (510, 100), 4)
        pygame.draw.line(gameDisplay, black, (540, 100), (590, 100), 4)

        for sequence in exportGuesses:
            letter = sequence[0]
            letter1 = medFont.render(letter, True, black)
            for idx in sequence[1]:
                if idx == 0:
                    gameDisplay.blit(letter1, [230, 30])
                elif idx == 1:
                    gameDisplay.blit(letter1, [310, 30])
                elif idx == 2:
                    gameDisplay.blit(letter1, [390, 30])
                elif idx == 3:
                    gameDisplay.blit(letter1, [470, 30])
                else:
                    gameDisplay.blit(letter1, [550, 30])

    elif length == 6:
        pygame.draw.line(gameDisplay, black, (180, 100), (230, 100), 4)
        pygame.draw.line(gameDisplay, black, (260, 100), (310, 100), 4)
        pygame.draw.line(gameDisplay, black, (340, 100), (390, 100), 4)
        pygame.draw.line(gameDisplay, black, (420, 100), (470, 100), 4)
        pygame.draw.line(gameDisplay, black, (500, 100), (550, 100), 4)
        pygame.draw.line(gameDisplay, black, (580, 100), (630, 100), 4)

        for sequence in exportGuesses:
            letter = sequence[0]
            letter1 = medFont.render(letter, True, black)
            for idx in sequence[1]:
                if idx == 0:
                    gameDisplay.blit(letter1, [190, 30])
                elif idx == 1:
                    gameDisplay.blit(letter1, [270, 30])
                elif idx == 2:
                    gameDisplay.blit(letter1, [350, 30])
                elif idx == 3:
                    gameDisplay.blit(letter1, [430, 30])
                elif idx == 4:
                    gameDisplay.blit(letter1, [510, 30])
                else:
                    gameDisplay.blit(letter1, [590, 30])

    elif length == 7:
        pygame.draw.line(gameDisplay, black, (140, 100), (190, 100), 4)
        pygame.draw.line(gameDisplay, black, (220, 100), (270, 100), 4)
        pygame.draw.line(gameDisplay, black, (300, 100), (350, 100), 4)
        pygame.draw.line(gameDisplay, black, (380, 100), (430, 100), 4)
        pygame.draw.line(gameDisplay, black, (460, 100), (510, 100), 4)
        pygame.draw.line(gameDisplay, black, (540, 100), (590, 100), 4)
        pygame.draw.line(gameDisplay, black, (620, 100), (670, 100), 4)

        for sequence in exportGuesses:
            letter = sequence[0]
            letter1 = medFont.render(letter, True, black)
            for idx in sequence[1]:
                if idx == 0:
                    gameDisplay.blit(letter1, [150, 30])
                elif idx == 1:
                    gameDisplay.blit(letter1, [230, 30])
                elif idx == 2:
                    gameDisplay.blit(letter1, [310, 30])
                elif idx == 3:
                    gameDisplay.blit(letter1, [390, 30])
                elif idx == 4:
                    gameDisplay.blit(letter1, [470, 30])
                elif idx == 5:
                    gameDisplay.blit(letter1, [550, 30])
                else:
                    gameDisplay.blit(letter1, [630, 30])

    elif length == 8:
        pygame.draw.line(gameDisplay, black, (100, 100), (150, 100), 4)
        pygame.draw.line(gameDisplay, black, (180, 100), (230, 100), 4)
        pygame.draw.line(gameDisplay, black, (260, 100), (310, 100), 4)
        pygame.draw.line(gameDisplay, black, (340, 100), (390, 100), 4)
        pygame.draw.line(gameDisplay, black, (420, 100), (470, 100), 4)
        pygame.draw.line(gameDisplay, black, (500, 100), (550, 100), 4)
        pygame.draw.line(gameDisplay, black, (580, 100), (630, 100), 4)
        pygame.draw.line(gameDisplay, black, (660, 100), (710, 100), 4)

        for sequence in exportGuesses:
            letter = sequence[0]
            letter1 = medFont.render(letter, True, black)
            for idx in sequence[1]:
                if idx == 0:
                    gameDisplay.blit(letter1, [110, 30])
                elif idx == 1:
                    gameDisplay.blit(letter1, [190, 30])
                elif idx == 2:
                    gameDisplay.blit(letter1, [270, 30])
                elif idx == 3:
                    gameDisplay.blit(letter1, [350, 30])
                elif idx == 4:
                    gameDisplay.blit(letter1, [430, 30])
                elif idx == 5:
                    gameDisplay.blit(letter1, [510, 30])
                elif idx == 6:
                    gameDisplay.blit(letter1, [590, 30])
                else:
                    gameDisplay.blit(letter1, [670, 30])

    elif length == 9:
        pygame.draw.line(gameDisplay, black, (60, 100), (110, 100), 4)
        pygame.draw.line(gameDisplay, black, (140, 100), (190, 100), 4)
        pygame.draw.line(gameDisplay, black, (220, 100), (270, 100), 4)
        pygame.draw.line(gameDisplay, black, (300, 100), (350, 100), 4)
        pygame.draw.line(gameDisplay, black, (380, 100), (430, 100), 4)
        pygame.draw.line(gameDisplay, black, (460, 100), (510, 100), 4)
        pygame.draw.line(gameDisplay, black, (540, 100), (590, 100), 4)
        pygame.draw.line(gameDisplay, black, (620, 100), (670, 100), 4)
        pygame.draw.line(gameDisplay, black, (700, 100), (750, 100), 4)

        for sequence in exportGuesses:
            letter = sequence[0]
            letter1 = medFont.render(letter, True, black)
            for idx in sequence[1]:
                    if idx == 0:
                        gameDisplay.blit(letter1, [70, 30])
                    elif idx == 1:
                        gameDisplay.blit(letter1, [150, 30])
                    elif idx == 2:
                        gameDisplay.blit(letter1, [230, 30])
                    elif idx == 3:
                        gameDisplay.blit(letter1, [310, 30])
                    elif idx == 4:
                        gameDisplay.blit(letter1, [390, 30])
                    elif idx == 5:
                        gameDisplay.blit(letter1, [470, 30])
                    elif idx == 6:
                        gameDisplay.blit(letter1, [550, 30])
                    elif idx == 7:
                        gameDisplay.blit(letter1, [630, 30])
                    else:
                        gameDisplay.blit(letter1, [710, 30])

    else:
        pygame.draw.line(gameDisplay, black, (20, 100), (70, 100), 4)
        pygame.draw.line(gameDisplay, black, (100, 100), (150, 100), 4)
        pygame.draw.line(gameDisplay, black, (180, 100), (230, 100), 4)
        pygame.draw.line(gameDisplay, black, (260, 100), (310, 100), 4)
        pygame.draw.line(gameDisplay, black, (340, 100), (390, 100), 4)
        pygame.draw.line(gameDisplay, black, (420, 100), (470, 100), 4)
        pygame.draw.line(gameDisplay, black, (500, 100), (550, 100), 4)
        pygame.draw.line(gameDisplay, black, (580, 100), (630, 100), 4)
        pygame.draw.line(gameDisplay, black, (660, 100), (710, 100), 4)
        pygame.draw.line(gameDisplay, black, (740, 100), (790, 100), 4)

        for sequence in exportGuesses:
            letter = sequence[0]
            letter1 = medFont.render(letter, True, black)
            for idx in sequence[1]:
                if idx == 0:
                    gameDisplay.blit(letter1, [30, 30])
                elif idx == 1:
                    gameDisplay.blit(letter1, [110, 30])
                elif idx == 2:
                    gameDisplay.blit(letter1, [190, 30])
                elif idx == 3:
                    gameDisplay.blit(letter1, [270, 30])
                elif idx == 4:
                    gameDisplay.blit(letter1, [350, 30])
                elif idx == 5:
                    gameDisplay.blit(letter1, [430, 30])
                elif idx == 6:
                    gameDisplay.blit(letter1, [510, 30])
                elif idx == 7:
                    gameDisplay.blit(letter1, [590, 30])
                elif idx == 8:
                    gameDisplay.blit(letter1, [670, 30])
                else:
                    gameDisplay.blit(letter1, [670, 30])

    pygame.display.update()


def getLetter():
    keepGoing = True
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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

def hangman():
    gameDisplay.fill(white)
    pygame.display.update()

    over = False
    words = ["abhor", "acquiesce", "acronym", "alacrity", "ambiguity", "amiable", "analogy", "andragogy", "antonym", "appease", "arcane", "assonance", "avarice", "brazen", "brusque", "cajole", "callous", "candor", "chide", "coerce", "cognition", "coherent", "confidant", "connive", "contrived", "conundrum", "criterion", "debase", "decry", "deference", "demure", "deride", "despot", "dialect", "diction", "didactic", "diligent", "divergent", "egregious", "elated", "eloquence", "eloquent", "embezzle", "emergent", "empathy", "enigma", "enmity", "epiphany", "epitaph", "epitome", "erudite", "extol", "fabricate", "feral", "formative", "forsake", "fractious", "furtive", "gluttony", "haughty", "holistic", "homonym", "hubris", "hyperbole", "hypocrisy", "impudent", "incisive", "indolent", "inept", "infamy", "inhibit", "innate", "insular", "intrepid", "irony", "jargon", "jubilant", "knell", "lithe", "lurid", "maverick", "maxim", "mentor", "metaphor", "mnemonic", "modicum", "monologue", "morose", "motif", "myriad", "nadir", "nemesis", "nominal", "norms", "novice", "nuance", "obfuscate", "oblivious", "obtuse", "oxymoron", "panacea", "paradox", "parody", "pedagogy", "pedantic", "penchant", "perusal", "phonemes", "plethora", "pseudonym", "quaint", "rash", "refurbish", "repudiate", "rife", "rubric", "salient", "sardonic", "satire", "simile", "soliloquy", "staid", "sycophant", "syntax", "taciturn", "thesis", "truculent", "umbrage", "validity", "venerable", "vex", "virtual", "wanton", "zenith"]
    maximum = len(words) - 1
    points = 0
    while not over:
        strikes = 0
        exportGuesses = []
        randomIndex = random.randint(0, maximum)
        word = words[randomIndex]
        length = len(word)
        guessList = []
        puzzle = ["__ "] * length
        score(points, strikes, length, guessList)
        while strikes < 6 and "__ " in puzzle:
            guess = getLetter()
            if guess.isalpha():
                if guess not in guessList:
                    if guess in word:
                        indexes = getIndex(word, guess)
                        if (guess, indexes) not in exportGuesses:
                            exportGuesses.append((guess, indexes))
                            for letter in word:
                                if letter == guess:
                                    points += 1
                            for index in indexes:
                                puzzle[index] = guess + ' '
                    else:
                        strikes += 1
                        guessList.append(guess)
            score(points, strikes, length, exportGuesses, guessList)
        if strikes == 6:
            for letter in word:
                indexes = getIndex(word, letter)
                exportGuesses.append((letter, indexes))
                score(points, strikes, length, exportGuesses, guessList)
            if gameOver():
                over = True
            else:
                points = 0
        else:
            over = gameEnd()
    return(points)


def menu():
    gameIntro()
    finalScore = hangman()
    print("The final score was", finalScore)

menu()
