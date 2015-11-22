import pygame
import time
from pygame import font
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

displayWidth = 800
displayHeight = 600
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Hangman!")
icon = pygame.image.load("hangman32.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
FPS = 30
# oneLimb = pygame.image.load("oneLimb.png")
# twoLimb = pygame.image.load("twoLimb.png")
# threeLimb = pygame.image.load("threeLimb.png")
# fourLimb = pygame.image.load("fourLimb.png")
# fiveLimb = pygame.image.load("fiveLimb.png")
# sixLimb = pygame.image.load("sixLimb.png")
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
    print(indexes)
    return(indexes)


def gameIntro():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()

        gameDisplay.fill(white)
        text = largeFont.render("Hello", True, black)
        explanation = smallFont.render("Press C to play or Q to quit", True, black)
        gameDisplay.blit(text, (300, 200))
        gameDisplay.blit(explanation, (250, 400))
        pygame.display.update()
        clock.tick(4)


def gameEnd():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return(False)
                elif event.key == pygame.K_q:
                    return(True)

        gameDisplay.fill(white)
        text = largeFont.render("Nice Job!", True, black)
        text2 = smallFont.render("C for play, Q for quit", True, black)
        gameDisplay.blit(text, (200, 200))
        gameDisplay.blit(text2, (250, 400))
        pygame.display.update()
        clock.tick(4)


def gameOver():
    image6 = pygame.image.load("hangman1006.png")
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return(False)
                elif event.key == pygame.K_q:
                    return(True)

        gameDisplay.fill(white)
        text = largeFont.render("Game Over", True, black)
        text2 = smallFont.render("C for play, Q for quit", True, black)
        gameDisplay.blit(image6, [300, 150])
        gameDisplay.blit(text, (300, 200))
        gameDisplay.blit(text2, (300, 400))
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

    """if len(guessList) == 6:
        leaveScreen = False
        while not leaveScreen:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        leaveScreen = True"""


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
        #letter1 = medFont.render("a", True, black)
        #gameDisplay.blit(letter1, [110, 30])

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


def actualGame():
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

def hangman():
    gameDisplay.fill(white)
    pygame.display.update()

    over = False
    words = ["aardvark", "arangatan", "alligator", "antelope", "bear", "bee", "boar", "gecko", "cat", "chimpanzee", "dog", "elephant", "echidna", "sphynx"]
    maximum = len(words) - 1
    #print(word)
    points = 0
    #strikes = 0
    while not over:
        strikes = 0
        exportGuesses = []
        randomIndex = random.randint(0, maximum)
        #print(randomIndex)
        word = words[randomIndex]
        length = len(word)
        guessList = []
        puzzle = ["__ "] * length
        score(points, strikes, length,guessList)
        while strikes < 6 and "__ " in puzzle:
            #print(puzzle)
            for element in puzzle:
                print(element, end='')
            if len(guessList) == 0:
                print("\t| Guessed: [none]")
            else:
                print("\t| Guessed:", guessList)
            # guess = input("\n\nGuess a letter: ")
            guess = actualGame()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessList:
                    print("You already guessed that.")
                elif guess in word:
                    for letter in word:
                        if letter == guess:
                            points += 1
                    indexes = getIndex(word, guess)
                    #print(indexes)
                    exportGuesses.append((guess, indexes))
                    #print(exportGuesses)
                    for index in indexes:
                        puzzle[index] = guess + ' '
                    #guessList.append(guess)
                else:
                    strikes += 1
                    guessList.append(guess)

            else:
                print("Guess a single letter.")
            print("\nPoints:", points)
            print("Strikes:", strikes, '\n')
            score(points, strikes, length, exportGuesses, guessList)
        if strikes == 6:
            print("\nThe word was", word)
            print("\nGame Over. U looz")
            for letter in word:
                indexes = getIndex(word, letter)
            #print(indexes)
                exportGuesses.append((letter, indexes))
                score(points, strikes, length, exportGuesses, guessList)
            if gameOver():
                over = True
                print(points)
            else:
                points = 0
        else:
            print("\nYou won!")
            over = gameEnd()
    print("\nTHANKS FOR PLAYING!\nFINAL SCORE:", points)
    return(points)


def menu():
    gameIntro()
    finalScore = hangman()

menu()
