import pygame
import time
import Barriers

pygame.init()

white = (255, 255, 255) # set colors rgb
black = (0,0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600
# returns a game surface object for the game
gameDisplay = pygame.display.set_mode((display_width, display_height))

# set title of the game
pygame.display.set_caption('Mazerunner')

blockSize = 10
# updates the surface
pygame.display.update()

# frames per second and font
clock = pygame.time.Clock()
frame_per_sec = 15
font = pygame.font.SysFont(None, 30)

# prints whatever message you give with color specified
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])

# redraws the vehicle 
def snake(lead_x, lead_y, block_size):
    pygame.draw.rect(gameDisplay, green, [lead_x, lead_y, blockSize, blockSize])

# adds a new barrier to the list
def addBarrier(barriers):
    barrier = Barriers.Barriers(display_width, display_height, blockSize)
    barriers.append(barrier)
    if barriers[0].getY() > display_height:
        del barriers[0]

def gameLoop():
    gameExit = False
    gameOver = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0
    counter = 0
    barriers = []
    addBarrier(barriers)
    while not gameExit:
        while gameOver:
            gameDisplay.fill(white)
            message_to_screen("Game over, press p to play to e to exit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_p:
                        gameOver = False
                        gameExit = False
                        lead_x = display_width / 2
                        lead_y = display_height / 2
                        lead_x_change = 0
                        lead_y_change = 0
                        barriers = []
        # for every time that there is an event
        for event in pygame.event.get():
            # the type of the event
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                # if left/right key is pressed, add/subtract change in x
                if event.key == pygame.K_LEFT:
                    lead_x_change = -blockSize
                if event.key == pygame.K_RIGHT:
                    lead_x_change = blockSize
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_change = 0
        # check that the vehicle is still on the screen
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        # add changes to the x,y coordinates of the vehicle
        lead_x += lead_x_change
        lead_y += lead_y_change
        # set background to white
        gameDisplay.fill(white)
        snake(lead_x, lead_y, blockSize)
        # make rectangle (where, color, [coordinateX, coordinateY, width, height])
        for obj in barriers:
            obj.moveY()
            pygame.draw.rect(gameDisplay, black, [obj.getX(),
                                                  obj.getY(),
                                                  obj.getWidth(), blockSize])
            if ((lead_x >= obj.getX() and
                lead_x <= obj.getX() + obj.getWidth()) and
                lead_y == obj.getY()):
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
