import pygame
import time
import pickle
from guitarHero import Notes
import random

pygame.init()

# set colors rgb
white = (255, 255, 255) 
black = (0, 0, 0)
blue = (0, 0, 202)
# set display dimensions
displayWidth = 800
displayHeight = 600

# returns a game surface object for the game
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

# set title of the game
pygame.display.set_caption('Guitar Hero')
# load all the images for the game
blueFill = pygame.image.load("guitarHero/blueFill.png").convert()
blueOpen = pygame.image.load("guitarHero/blueOpen.png").convert()
greenFill = pygame.image.load("guitarHero/greenFill.png").convert()
greenOpen = pygame.image.load("guitarHero/greenOpen.png").convert()
orangeFill = pygame.image.load("guitarHero/orangeFill.png").convert()
orangeOpen = pygame.image.load("guitarHero/orangeOpen.png").convert()
redFill = pygame.image.load("guitarHero/redFill.png").convert()
redOpen = pygame.image.load("guitarHero/redOpen.png").convert()
meter = pygame.image.load("guitarHero/meter.png").convert()

gameDisplay.fill(black)
# updates the surface
pygame.display.update()

# frames per second and font
clock = pygame.time.Clock()
framePerSec = 15
font = pygame.font.SysFont(None, 40)


def displayScore(score, meter):
    # display high score and current score
    msg = "C: " + str(score)
    screenText = font.render(msg, True, white)
    gameDisplay.blit(screenText, [10, 40])

    ## fill the meter ##
    if (score * 5 - meter) >= 0:
        yValue = score * 5 - meter
        pygame.draw.rect(gameDisplay, blue, [10, 400 - yValue, 50, yValue])
        if yValue >= 200:
            return True
        else:
            return False
    else:
        pygame.draw.rect(gameDisplay, blue, [10, 400, 50, 0])
        return False


# prints whatever message you give with color specified
def messageToScreen(msg, color, score):
    screenText = font.render(msg, True, color)
    gameDisplay.blit(screenText, [displayWidth // 4, 0])


def drawBasics(bImage, gImage, oImage, rImage):
    gameDisplay.blit(bImage, [225, 550])
    gameDisplay.blit(gImage, [325, 550])
    gameDisplay.blit(oImage, [425, 550])
    gameDisplay.blit(rImage, [525, 550])
    gameDisplay.blit(meter, [10, 200])
    # draw columns
    pygame.draw.line(gameDisplay, white, (200, 0), (200, 800), 2)
    pygame.draw.line(gameDisplay, white, (300, 0), (300, 800), 2)
    pygame.draw.line(gameDisplay, white, (400, 0), (400, 800), 2)
    pygame.draw.line(gameDisplay, white, (500, 0), (500, 800), 2)
    pygame.draw.line(gameDisplay, white, (600, 0), (600, 800), 2)


def displayNotes(targets, score):
    for obj in targets:
        color = obj.getRandColor()
        if color == 1:
            gameDisplay.blit(blueFill, [225, obj.getYValue()])
        elif color == 2:
            gameDisplay.blit(greenFill, [325, obj.getYValue()])
        elif color == 3:
            gameDisplay.blit(orangeFill, [425, obj.getYValue()])
        else:
            gameDisplay.blit(redFill, [525, obj.getYValue()])
        obj.moveY()
    if len(targets) != 0 and targets[0].getYValue() > displayHeight:
        del targets[0]
        score -= 1
    return score


def checkHit(color, targets, score):
    # index of target to be deleted
    # the index will never be negative 1
    toDelete = -1
    addScore = False
    for index in range(len(targets)):
        if targets[index].getYValue() >= 540 and targets[index].getYValue() <= 560:
            if targets[index].getRandColor() == color:
                addScore = True
                toDelete = index
    if toDelete != -1:
        del targets[toDelete]
    if addScore:
        score += 1
    else:
        if score != 0:
            score -= 1
    return score


def gameLoop():
    gameExit = False
    gameOver = False
    score = 0
    counter = 1
    color = black
    redImage = redOpen
    blueImage = blueOpen
    orangeImage = orangeOpen
    greenImage = greenOpen
    targets = []
    meter = 0
    targets.append(Notes.Notes())
    while not gameExit:
        gameDisplay.fill(black)
        while gameOver:
            if checkWin:
                messageToScreen("You won! Press p to play to e to exit",
                    white, score)
            else:
            # print instructions to continue and check for input
                messageToScreen("Game over, press p to play to e to exit",
                    white, score)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_p:
                        # re-assign the variables to the start positions
                        gameOver = False
                        gameExit = False
                        counter = 1
                        meter = 0
                        score = 0
                        targets = []
        # for every time that there is an event
        for event in pygame.event.get():
            # the type of the event
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                # check which button they click, then check to see
                # if they hit the target at the right time
                # j == blue button 
                if event.key == pygame.K_j:
                    score = checkHit(1, targets, score)
                    blueImage = blueFill
                # k == green button
                if event.key == pygame.K_k:
                    score = checkHit(2, targets, score)
                    greenImage = greenFill
                # l == orange button
                if event.key == pygame.K_l:
                    score = checkHit(3, targets, score)
                    orangeImage = orangeFill
                # ; == red button
                if event.key == pygame.K_SEMICOLON:
                    score = checkHit(4, targets, score)
                    redImage = redFill
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_j:
                    blueImage = blueOpen
                # k == green button
                if event.key == pygame.K_k:
                    greenImage = greenOpen
                # l == orange button
                if event.key == pygame.K_l:
                    orangeImage = orangeOpen
                # ; == red button
                if event.key == pygame.K_SEMICOLON:
                    redImage = redOpen
        counter += 1
        if counter % 7 == 0:
            meter += 1
            randNum = random.randint(1,2)
            if randNum == 1:
                targets.append(Notes.Notes())
            counter = 1
        score = displayNotes(targets, score)
        drawBasics(blueImage, greenImage, orangeImage, redImage)
        checkWin = displayScore(score, meter)
        if checkWin:
            gameOver = True
        pygame.display.update()
        # sleep -> frames per second (lower number = slower)
        clock.tick(framePerSec)
    
    # un-initializes and quits pygame
    pygame.quit()

gameLoop()
