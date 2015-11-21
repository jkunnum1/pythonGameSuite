import pygame
import time
from mazeGames import NewBarrier

pygame.init()

# append score each time there is a game over
totalScore = [0]
# set colors rgb
white = (255, 255, 255)
black = (0, 0, 0)
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
gameDisplay.blit(backgroundImage, [0, 0])

# updates the surface
pygame.display.update()

# frames per second and font
clock = pygame.time.Clock()
framePerSec = 15
font = pygame.font.SysFont(None, 40)


def displayScore(score):
    # display high score and current score
    msg = "H: " + str(max(totalScore))
    screenText = font.render(msg, True, black)
    gameDisplay.blit(screenText, [10, 10])
    msg = "C: " + str(score)
    screenText = font.render(msg, True, black)
    gameDisplay.blit(screenText, [10, 40])


# prints whatever message you give with color specified
def messageToScreen(msg, color, score):
    if score > max(totalScore):
        msg2 = "You have a new high of " + str(score)
        screenText = font.render(msg2, True, color)
        gameDisplay.blit(screenText, [displayWidth // 4, 40])
    screenText = font.render(msg, True, color)
    gameDisplay.blit(screenText, [displayWidth // 4, 0])

##    textPosition = screenText.get_rect()
##    textPosition.centerx = gameDisplay.get_rect().centerx
##    gameDisplay.blit(screenText, textPosition)


# redraws the vehicle
def mazeVehicle(leadX, leadY, blockSize):
    pygame.draw.rect(gameDisplay, black, [leadX, leadY, blockSize, blockSize])


# adds a new barrier to the list
def addBarrier(barriers, leadX=0, move=20):
    if len(barriers) == 0:
        barrier = NewBarrier.NewBarrier(displayWidth, displayHeight,
                                        blockSize, leadX, move, True)
    else:
        xPosition = barriers[-1].getX()
        barrier = NewBarrier.NewBarrier(displayWidth, displayHeight,
                                        blockSize, xPosition, move)

    barriers.append(barrier)
    if barriers[0].getY() > displayHeight:
        del barriers[0]


def gameLoop():
    gameExit = False
    gameOver = False
    leadX = displayWidth / 2
    leadY = displayHeight // 1.5
    # start with counter at 0 so that counter % 20 is not 0
    counter = 2
    leadXChange = 0
    score = 0
    barriers = []
    addBarrier(barriers, leadX)
    difficulty = 20

    while not gameExit:
        # for every time that there is an event
        for event in pygame.event.get():
            # the type of the event
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                # if left/right key is pressed, add/subtract change in x
                if event.key == pygame.K_LEFT:
                    leadXChange = -blockSize
                if event.key == pygame.K_RIGHT:
                    leadXChange = blockSize
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    leadXChange = 0
        # check that the vehicle is still on the screen
        if ((leadX >= displayWidth or leadX < 0) or (leadY >= displayHeight or
                                                     leadY < 0)):
            gameOver = True

        # add changes to the x coordinate of the vehicle
        leadX += leadXChange
        gameDisplay.blit(backgroundImage, [0, 0])
        # make rectangle (where, color, [coordinateX, coordinateY, width,
        # height])
        for obj in barriers:
            obj.moveY()
            pygame.draw.rect(gameDisplay, orange, [obj.getX(),
                                                   obj.getY(),
                                                   obj.getWidth(),
                                                   obj.getHeight()])
            # check to see that the vehicle is still on the path
            if ((leadY >= obj.getY() and leadY < obj.getY() +
                 obj.getHeight()) and (leadX < obj.getX() or
                                       leadX > obj.getX() + obj.getWidth())):
                gameOver = True
            # if the user passes this object then add, to the counter
            if not gameOver:
                counter += 1
        # add the next zone
        addBarrier(barriers, 0, difficulty)
        mazeVehicle(leadX, leadY, blockSize)
        # increment score
        if counter % 20 == 0:
            score += 1
            counter = 0
            # check to see if it is time to increment difficulty
            if score > 60:
                difficulty = 30
            elif score > 40:
                difficulty = 25
            elif score > 20:
                difficulty = 20
            else:
                difficulty = 15
            #######################################
        displayScore(score)

        while gameOver:
            # print instructions to continue and check for input
            messageToScreen("Game over, press p to play to e to exit", red,
                            score)
            pygame.draw.rect(gameDisplay, black, [leadX, leadY, blockSize,
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
                        difficulty = 20
                        barriers = []
                        addBarrier(barriers, leadX)

        pygame.display.update()

        # sleep -> frames per second (lower number = slower)
        clock.tick(framePerSec)

    # un-initializes and quits pygame
    pygame.quit()
    quit()

gameLoop()
