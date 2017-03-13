# Project
# William McLaughlin
# A 51
# S. Douglas Wehbe
# A 52
# Julie Kunnumpurath
# A 53
# John Henry Burns
# A 52
# Rebecca Trackman
# A 52

import pygame
import time
import pickle
from mazeGames import NewBarrier
from mazeGames import Vehicle


class NewMaze:
    def __init__(self):
        pygame.init()

        '''LOAD ONLINE USER'''
        self.__allUsers = pickle.load(open("users.dat", "rb"))
        self.__user = pickle.load(open("userOnline.dat", "rb"))
        self.__highScores = pickle.load(open("mazeGames/" +
                                             "mazeScores2.dat", "rb"))
        #  append score each time there is a game over  #
        # LOAD HIGHSCORE TO TOTAL SCORE TO BE SHOWN #
        self.__highestScore = 0
        try:
            self.__highestScore = self.__highScores[self.__user[0]]
        except KeyError:
            # User is new, so key above wont work
            self.__highScores[self.__user[0]] = 0

        # set colors rgb
        self.__white = (255, 255, 255)
        self.__black = (0, 0, 0)
        self.__red = (255, 0, 0)
        self.__green = (0, 155, 0)
        self.__orange = (255, 165, 0)
        self.__teal = (32, 178, 170)
        # set display dimensions
        self.__displayWidth = 800
        self.__displayHeight = 600
        # set width of block
        self.__blockSize = 10

        # returns a game surface object for the game
        self.__gameDisplay = pygame.display.set_mode((self.__displayWidth,
                                                      self.__displayHeight))

        # set title of the game
        pygame.display.set_caption('Mazerunner')
        # set background
        self.__backgroundImage = pygame.image.load("mazeGames/images/maze" +
                                                   "Background.png").convert()
        self.__gameDisplay.blit(self.__backgroundImage, [0, 0])

        # updates the surface
        pygame.display.update()

        # frames per second and font
        self.__clock = pygame.time.Clock()
        self.__framePerSec = 15
        self.__font = pygame.font.SysFont(None, 40)
        play = True
        while play:
            play = self.__gameLoop()
        # un-initializes and quits pygame
        pygame.quit()

    def __gameLoop(self):
        gameExit = False
        gameOver = False
        # start with counter at 0 so that counter % 20 is not 0
        counter = 2
        score = 0
        barriers = []
        self.__addBarrier(barriers, self.__displayWidth / 2)
        difficulty = 20
        vehicle = Vehicle.Vehicle(self.__gameDisplay, self.__black,
                                  self.__blockSize, self.__displayWidth / 2,
                                  self.__displayHeight // 1.5)

        while not gameExit:
            # for every time that there is an event
            for event in pygame.event.get():
                # the type of the event
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    # if left/right key is pressed, add/subtract change in x
                    if event.key == pygame.K_LEFT:
                        vehicle.moveX(-self.__blockSize)
                    if event.key == pygame.K_RIGHT:
                        vehicle.moveX(self.__blockSize)
                if event.type == pygame.KEYUP:
                    if (event.key == pygame.K_LEFT or
                            event.key == pygame.K_RIGHT):
                        vehicle.moveX(0)
            # check that the vehicle is still on the screen
            if ((vehicle.getX() >= self.__displayWidth or
                 vehicle.getX() < 0) or
                (vehicle.getY() >= self.__displayHeight or
                 vehicle.getY() < 0)):
                gameOver = True
            self.__gameDisplay.blit(self.__backgroundImage, [0, 0])
            # make rectangle (where, color, [coordinateX, coordinateY, width,
            # height])
            for obj in barriers:
                obj.moveY()
                pygame.draw.rect(self.__gameDisplay, self.__orange,
                                 [obj.getX(), obj.getY(), obj.getWidth(),
                                  obj.getHeight()])
                # check to see that the vehicle is still on the path
                if ((vehicle.getY() >= obj.getY() and
                     vehicle.getY() < obj.getY() + obj.getHeight()) and
                    (vehicle.getX() < obj.getX() or
                     vehicle.getX() > obj.getX() + obj.getWidth())):
                    gameOver = True
                # if the user passes this object then add, to the counter
                if not gameOver:
                    counter += 1
            # add the next zone
            self.__addBarrier(barriers, 0, difficulty)
            vehicle.drawVehicle()
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
            self.__displayScore(score)

            while gameOver:
                # print instructions to continue and check for input
                self.__messageToScreen("Game over, press p to play or e " +
                                       "to exit", self.__red, score)
                vehicle.moveX(0)
                vehicle.drawVehicle()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.__addToTotal(score)
                        return False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_e:
                            self.__addToTotal(score)
                            return False
                        if event.key == pygame.K_p:
                            self.__addToTotal(score)
                            return True

            pygame.display.update()

            # sleep -> frames per second (lower number = slower)
            self.__clock.tick(self.__framePerSec)

    def __displayScore(self, score):
        # display high score and current score
        msg = "H: " + str(self.__highestScore)
        screenText = self.__font.render(msg, True, self.__black)
        self.__gameDisplay.blit(screenText, [10, 10])
        msg = "C: " + str(score)
        screenText = self.__font.render(msg, True, self.__black)
        self.__gameDisplay.blit(screenText, [10, 40])

    # prints whatever message you give with color specified
    def __messageToScreen(self, msg, color, score):
        if score > self.__highScores[self.__user[0]]:
            msg2 = "You have a new high of " + str(score)
            # SAVE HIGH SCORE
            self.__highestScore = score
            self.__highScores[self.__user[0]] = self.__highestScore
            pickle.dump(self.__highScores, open("mazeGames/maze" +
                                                "Scores2.dat", "wb"))
            screenText = self.__font.render(msg2, True, color)
            self.__gameDisplay.blit(screenText, [self.__displayWidth // 4, 40])
        screenText = self.__font.render(msg, True, color)
        self.__gameDisplay.blit(screenText, [self.__displayWidth // 4, 0])

    def __addToTotal(self, score):
        # ADD TO THE TOTAL SCORE
        self.__user[-1] = self.__allUsers[self.__user[0]][-1] + score
        self.__allUsers[self.__user[0]] = self.__user
        pickle.dump(self.__allUsers, open("users.dat", "wb"))

    # adds a new barrier to the list
    def __addBarrier(self, barriers, leadX=0, move=20):
        if len(barriers) == 0:
            barrier = NewBarrier.NewBarrier(self.__displayWidth,
                                            self.__displayHeight,
                                            self.__blockSize,
                                            leadX, move, True)
        else:
            xPosition = barriers[-1].getX()
            barrier = NewBarrier.NewBarrier(self.__displayWidth,
                                            self.__displayHeight,
                                            self.__blockSize, xPosition, move)

        barriers.append(barrier)
        if barriers[0].getY() > self.__displayHeight:
            del barriers[0]
