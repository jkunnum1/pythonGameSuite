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
from mazeGames import Barriers
import pickle
from mazeGames import Vehicle


class Maze():
    def __init__(self):
        pygame.init()

        ############################
        '''LOAD ONLINE USER'''
        self.__allUsers = pickle.load(open("users.dat", "rb"))
        self.__user = pickle.load(open("userOnline.dat", "rb"))
        self.__highScores = pickle.load(open("mazeGames/mazeScores.dat", "rb"))
        ############################
        #  append score each time there is a game over  #
        ### LOAD HIGHSCORE TO TOTAL SCORE TO BE SHOWN ###
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
        self.__backgroundImage = pygame.image.load("mazeGames" +
                                "/images/mazeBackground.png").convert()
        self.__gameDisplay.blit(self.__backgroundImage, [0, 0])
        # set power-up image
        self.__powerUpImg = pygame.image.load("mazeGames/images/powerUp.png").convert()
        # updates the surface
        pygame.display.update()
        # frames per second and font
        self.__clock = pygame.time.Clock()
        self.__framePerSec = 15
        self.__font = pygame.font.SysFont(None, 40)
        # start of the game
        play = True
        while play:
            play = self.__gameLoop()
        # un-initializes and quits pygame
        pygame.quit()

    def __gameLoop(self):
        gameExit = False
        gameOver = False
        score = 0
        # difficulty variable - decreasing this number will increase difficulty
        difficulty = 10
        counter = 0
        # boolean for has powerup
        hasPower = False
        # color of the blocks
        color = self.__black
        # counter to determine how long the power up will last
        powerUsedCount = 0
        vehicle = Vehicle.Vehicle(self.__gameDisplay, self.__orange,
                                  self.__blockSize, self.__displayWidth / 2,
                                  self.__displayHeight // 1.5)
        barriers = []
        self.__addBarrier(barriers)
        while not gameExit:
            while gameOver:
                # print instructions to continue and check for input
                self.__messageToScreen("Game over, press p to play or " +
                                       "e to exit", self.__red, score)
                vehicle.moveX(0)
                vehicle.drawVehicle()
                pygame.display.update()
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT or
                       (event.type == pygame.KEYDOWN and
                       event.key == pygame.K_e)):
                        self.__addToTotal(score)
                        return False
                    if (event.type == pygame.KEYDOWN and
                        event.key == pygame.K_p):
                        self.__addToTotal(score)
                        return True
            # for every time that there is an event
            for event in pygame.event.get():
                # the type of the event
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    # check to see if the user wants to use the power up
                    if event.key == pygame.K_p and hasPower:
                        hasPower = False
                        color = self.__white
                        powerUsedCount = score
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
            if (vehicle.getX() >= self.__displayWidth or vehicle.getX() < 0 or
                 vehicle.getY() >= self.__displayHeight or vehicle.getY() < 0):
                gameOver = True
            self.__gameDisplay.blit(self.__backgroundImage, [0, 0])
            vehicle.drawVehicle()
            # make rectangle (where, color, [coordinateX, coordinateY,
            # width, height])
#####
            for obj in barriers:
                obj.moveY()
                pygame.draw.rect(self.__gameDisplay, color,
                                 [obj.getX(), obj.getY(), obj.getWidth(),
                                  self.__blockSize])
                # check to see if there is a collision, else add point to score
                if powerUsedCount == 0:
                    if ((vehicle.getX() >= obj.getX() and
                         vehicle.getX() + 10 <= obj.getX() + obj.getWidth())
                         and vehicle.getY() == obj.getY()):
                        gameOver = True
                if obj.getY() - 10 == vehicle.getY():
                    score += 1
                # check to see that it is time to end the power-up
                if powerUsedCount + 10 == score:
                    powerUsedCount = 0
                    color = self.__black
#####
            self.__displayScore(score)
            counter += 1
            # check to see if it's time to add a new barrier and
            # increase difficulty
            difficulty = self.__makeHarder(counter, difficulty, barriers,
                                           score)
            # check to see if the player deserves a power up
            hasPower = self.__checkPower(score, hasPower)
            pygame.display.update()
            # sleep -> frames per second (lower number = slower)
            self.__clock.tick(self.__framePerSec)

    def __checkPower(self, score, hasPower):
        if score != 0 and score % 30 == 0:
            hasPower = True
        if hasPower:
            self.__gameDisplay.blit(self.__powerUpImg, [10, 540])
        return hasPower

    def __makeHarder(self, counter, difficulty, barriers, score):
        if counter % difficulty == 0:
            if score > 60:
                difficulty = 5
            elif score > 40:
                difficulty = 7
            elif score > 20:
                difficulty = 8
            else:
                difficulty = 10
            self.__addBarrier(barriers)
        return difficulty

    def __displayScore(self, score):
        # display high score and current score
        msg = "H: " + str(self.__highestScore)
        screenText = self.__font.render(msg, True, self.__orange)
        self.__gameDisplay.blit(screenText, [10, 10])
        msg = "C: " + str(score)
        screenText = self.__font.render(msg, True, self.__orange)
        self.__gameDisplay.blit(screenText, [10, 40])

    # prints whatever message you give with color specified
    def __messageToScreen(self, msg, color, score):
        if score > self.__highScores[self.__user[0]]:
            msg2 = "You have a new high of " + str(score)
            ###### SAVE HIGH SCORE ######
            self.__highestScore = score
            self.__highScores[self.__user[0]] = self.__highestScore
            pickle.dump(self.__highScores, open("mazeGames/mazeScores.dat", "wb"))
            #############################
            screenText = self.__font.render(msg2, True, color)
            self.__gameDisplay.blit(screenText, [self.__displayWidth // 4, 40])
        screenText = self.__font.render(msg, True, color)
        self.__gameDisplay.blit(screenText, [self.__displayWidth // 4, 0])

    def __addToTotal(self, score):
        ##### ADD TO THE TOTAL SCORE #####
        self.__user[-1] = self.__allUsers[self.__user[0]][-1] + score
        self.__allUsers[self.__user[0]] = self.__user
        pickle.dump(self.__allUsers, open("users.dat", "wb"))
        ##################################
        
    # adds a new barrier to the list
    def __addBarrier(self, barriers):
        barrier = Barriers.Barriers(self.__displayWidth, self.__displayHeight,
                                    self.__blockSize)
        barriers.append(barrier)
        if barriers[0].getY() > self.__displayHeight:
            del barriers[0]
