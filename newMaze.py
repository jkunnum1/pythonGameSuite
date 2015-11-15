import pygame
import time
import Barriers

pygame.init()

white = (255, 255, 255) # set colors rgb
black = (0,0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

displayWidth = 800
displayHeight = 600
rect
# returns a game surface object for the game
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

# set title of the game
pygame.display.set_caption('Mazerunner')

blockSize = 10
# updates the surface
pygame.display.update()

# frames per second and font
clock = pygame.time.Clock()
framePerSec = 15
font = pygame.font.SysFont(None, 30)

# prints whatever message you give with color specified
def messageToScreen(msg, color):
    screenText = font.render(msg, True, color)
    gameDisplay.blit(screenText, [displayWidth / 2, displayHeight / 2])

# redraws the vehicle 
def snake(leadX, leadY, blockSize):
    pygame.draw.rect(gameDisplay, green, [leadX, leadY, blockSize, blockSize])

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
    leadY = displayHeight / 2
    leadXChange = 0
    leadYChange = 0
    counter = 0
    barriers = []
    addBarrier(barriers)
    while not gameExit:
        while gameOver:
            gameDisplay.fill(white)
            messageToScreen("Game over, press p to play to e to exit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_p:
                        gameOver = False
                        gameExit = False
                        leadX = display_width / 2
                        leadY = display_height / 2
                        leadXChange = 0
                        leadYChange = 0
                        barriers = []
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
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    leadYChange = 0
        # check that the vehicle is still on the screen
        if leadX >= displayWidth or leadX < 0 or leadY >= displayHeight or leadY < 0:
            gameOver = True

        # add changes to the x,y coordinates of the vehicle
        leadX += leadXChange
        leadX += leadYChange
        # set background to white
        gameDisplay.fill(white)
        snake(leadX, leadY, blockSize)
        # make rectangle (where, color, [coordinateX, coordinateY, width, height])
        for obj in barriers:
            obj.moveY()
            pygame.draw.rect(gameDisplay, black, [obj.getX(),
                                                  obj.getY(),
                                                  obj.getWidth(), blockSize])
            if ((leadX >= obj.getX() and
                leadX <= obj.getX() + obj.getWidth()) and
                leadY == obj.getY()):
                gameOver = True
        pygame.display.update()
        counter += 1
        if counter % 10 == 0:
            addBarrier(barriers)
            pygame.display.update()
        

        # sleep -> frames per second (lower number = slower)
        clock.tick(frame_per_sec)
        
    
    # un-initializes and quits pygame
    pygame.quit()
    quit()

gameLoop()
