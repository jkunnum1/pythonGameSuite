import pygame
import time
from mazeGames import Barriers
import pickle

pygame.init()

############################
'''LOAD ONLINE USER'''
user = pickle.load(open("userOnline.dat", "rb"))
highScores = pickle.load(open("mazeGames/mazeScores.dat", "rb"))
############################

#  append score each time there is a game over  #
### LOAD HIGHSCORE TO TOTAL SCORE TO BE SHOWN ###
try:
    totalScore = [highScores[user[0]], 0]
except KeyError:
    # User is new, so key above wont work
    highScores[user[0]] = 0
    totalScore = [0]
# set colors rgb
white = (255, 255, 255) 
black = (0,0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
orange = (255, 165, 0)
teal = (32, 178, 170)
# set display dimensions
displayWidth = 800
displayHeight = 600
# set width of block
blockSize = 10

# returns a game surface object for the game
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

# set title of the game
pygame.display.set_caption('Mazerunner')
# set background
backgroundImage = pygame.image.load("mazeGames/mazeBackground.png").convert()
gameDisplay.blit(backgroundImage, [0,0])
# set power-up image
powerUpImg = pygame.image.load("mazeGames/powerUp.png").convert()

# updates the surface
pygame.display.update()

# frames per second and font
clock = pygame.time.Clock()
framePerSec = 15
font = pygame.font.SysFont(None, 40)

def displayScore(score):
    # display high score and current score
    msg = "H: " + str(max(totalScore))
    screenText = font.render(msg, True, orange)
    gameDisplay.blit(screenText, [10, 10])
    msg = "C: " + str(score)
    screenText = font.render(msg, True, orange)
    gameDisplay.blit(screenText, [10, 40])

# prints whatever message you give with color specified
def messageToScreen(msg, color, score):
    if score > max(totalScore):
        msg2 = "You have a new high of " + str(score)
        ###### SAVE HIGH SCORE ######
        highScores[user[0]] = score
        pickle.dump(highScores, open("mazeGames/mazeScores.dat", "wb"))
        #############################
        screenText = font.render(msg2, True, color)
        gameDisplay.blit(screenText, [displayWidth // 4, 40])
    screenText = font.render(msg, True, color)
    gameDisplay.blit(screenText, [displayWidth // 4, 0])

##    previously how to center text 
##    textPosition = screenText.get_rect()
##    textPosition.centerx = gameDisplay.get_rect().centerx
##    gameDisplay.blit(screenText, textPosition)

# redraws the vehicle 
def vehicle(leadX, leadY, blockSize):
    pygame.draw.rect(gameDisplay, orange, [leadX, leadY, blockSize, blockSize])

# adds a new barrier to the list
def addBarrier(barriers):
    barrier = Barriers.Barriers(displayWidth, displayHeight, blockSize)
    barriers.append(barrier)
    if barriers[0].getY() > displayHeight:
        del barriers[0]

def gameLoop():
    gameExit = False
    gameOver = False
    leadX = displayWidth / 2
    leadY = displayHeight // 1.5
    leadXChange = 0
    score = 0
    # difficulty variable - decreasing this number will increase difficulty
    difficulty = 10
    counter = 0
    # boolean for has powerup
    hasPower = False
    # color of the blocks
    color = black
    # counter to determine how long the power up will last
    powerUsedCount = 0
    barriers = []
    addBarrier(barriers)
    while not gameExit:
        while gameOver:
            # print instructions to continue and check for input
            messageToScreen("Game over, press p to play to e to exit", red,
                            score)
            pygame.draw.rect(gameDisplay, orange, [leadX, leadY, blockSize,
                                                  blockSize])
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
                        leadX = displayWidth / 2
                        leadY = displayHeight // 1.5
                        leadXChange = 0
                        totalScore.append(score)
                        score = 0
                        counter = 0
                        hasPower = False
                        barriers = []
        # for every time that there is an event
        for event in pygame.event.get():
            # the type of the event
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                # check to see if the user wants to use the power up
                if event.key == pygame.K_p and hasPower == True:
                    hasPower = False
                    color = white
                    powerUsedCount = score
                # if left/right key is pressed, add/subtract change in x
                if event.key == pygame.K_LEFT:
                    leadXChange = -blockSize
                if event.key == pygame.K_RIGHT:
                    leadXChange = blockSize
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    leadXChange = 0
        # check that the vehicle is still on the screen
        if (leadX >= displayWidth or leadX < 0 or leadY >= displayHeight or 
            leadY < 0):
            gameOver = True
        # add changes to the x coordinate of the vehicle
        leadX += leadXChange
        gameDisplay.blit(backgroundImage, [0,0])
        vehicle(leadX, leadY, blockSize)
        # make rectangle (where, color, [coordinateX, coordinateY, 
        # width, height])
        for obj in barriers:
            obj.moveY()
            pygame.draw.rect(gameDisplay, color, [obj.getX(),
                                                  obj.getY(),
                                                  obj.getWidth(), blockSize])
            # check to see if there is a collision, else add point to score
            if powerUsedCount == 0:
                if ((leadX >= obj.getX() and
                    leadX + 10 <= obj.getX() + obj.getWidth()) and
                    leadY == obj.getY()):
                    gameOver = True
            if obj.getY() - 10 == leadY:
                score += 1
            # check to see that it is time to end the power-up
            if powerUsedCount + 10 == score:
                powerUsedCount = 0
                color = black
        displayScore(score)
        counter += 1
        # check to see if it's time to add a new barrier and 
        # increase difficulty
        if counter % difficulty == 0:
            if score > 60:
                difficulty = 5
            elif score > 40:
                difficulty = 7
            elif score > 20:
                difficulty = 8
            else:
                difficulty = 10
            counter = 0
            addBarrier(barriers)
        # check to see if the player deserves a power up
        if score != 0 and score % 30 == 0:
            hasPower = True
        if hasPower:
            gameDisplay.blit(powerUpImg, [10, 540])
        pygame.display.update()

        # sleep -> frames per second (lower number = slower)
        clock.tick(framePerSec)
    
    # un-initializes and quits pygame
    pygame.quit()

gameLoop()
