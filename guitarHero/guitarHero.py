import pygame
import time
import pickle
from guitarHero import Notes
import random

class GuitarHero:
    def __init__(self):
        pygame.init()

        ############################
        '''LOAD ONLINE USER'''
        self.__user = pickle.load(open("userOnline.dat", "rb"))
        self.__highScores = pickle.load(open("guitarHero/guitarHero.dat", "rb"))
        ############################
        #  append score each time there is a game over  #
        ### LOAD HIGHSCORE TO TOTAL SCORE TO BE SHOWN ###
        try:
            self.__totalScore = [self.__highScores[self.__user[0]], 0]
        except KeyError:
            # User is new, so key above wont work
            self.__highScores[self.__user[0]] = 0
            self.__totalScore = [0]

        # set colors rgb
        self.__white = (255, 255, 255) 
        self.__black = (0, 0, 0)
        self.__blue = (0, 0, 202)
        # set display dimensions
        self.__displayWidth = 800
        self.__displayHeight = 600

        # returns a game surface object for the game
        self.__gameDisplay = pygame.display.set_mode((self.__displayWidth, self.__displayHeight))

        # set title of the game
        pygame.display.set_caption('Guitar Hero')
        # load all the images for the game
        self.__blueFill = pygame.image.load("guitarHero/blueFill.png").convert()
        self.__blueOpen = pygame.image.load("guitarHero/blueOpen.png").convert()
        self.__greenFill = pygame.image.load("guitarHero/greenFill.png").convert()
        self.__greenOpen = pygame.image.load("guitarHero/greenOpen.png").convert()
        self.__orangeFill = pygame.image.load("guitarHero/orangeFill.png").convert()
        self.__orangeOpen = pygame.image.load("guitarHero/orangeOpen.png").convert()
        self.__redFill = pygame.image.load("guitarHero/redFill.png").convert()
        self.__redOpen = pygame.image.load("guitarHero/redOpen.png").convert()
        self.__meter = pygame.image.load("guitarHero/meter.png").convert()

        self.__gameDisplay.fill(self.__black)
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
        score = 0
        counter = 1
        color = self.__black
        redImage = self.__redOpen
        blueImage = self.__blueOpen
        orangeImage = self.__orangeOpen
        greenImage = self.__greenOpen
        targets = []
        meter = 0
        targets.append(Notes.Notes())
        while not gameExit:
            self.__gameDisplay.fill(self.__black)
            while gameOver:
                if checkWin:
                    self.__messageToScreen("You won! Press p to play to e to exit",
                        score)
                else:
                # print instructions to continue and check for input
                    self.__messageToScreen("Game over, press p to play to e to exit",
                        score)
                self.__totalScore.append(score)
                pygame.display.update()
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT or
                       (event.type == pygame.KEYDOWN and
                       event.key == pygame.K_e)):
                        return False
                    if event.key == pygame.K_p:
                        return True
            # for every time that there is an event
            for event in pygame.event.get():
                # the type of the event
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    # check which button they click, then check to see
                    # if they hit the target at the right time
                    # j == blue button 
                    if event.key == pygame.K_j:
                        score = self.__checkHit(1, targets, score)
                        blueImage = self.__blueFill
                    # k == green button
                    if event.key == pygame.K_k:
                        score = self.__checkHit(2, targets, score)
                        greenImage = self.__greenFill
                    # l == orange button
                    if event.key == pygame.K_l:
                        score = self.__checkHit(3, targets, score)
                        orangeImage = self.__orangeFill
                    # ; == red button
                    if event.key == pygame.K_SEMICOLON:
                        score = self.__checkHit(4, targets, score)
                        redImage = self.__redFill
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_j:
                        blueImage = self.__blueOpen
                    # k == green button
                    if event.key == pygame.K_k:
                        greenImage = self.__greenOpen
                    # l == orange button
                    if event.key == pygame.K_l:
                        orangeImage = self.__orangeOpen
                    # ; == red button
                    if event.key == pygame.K_SEMICOLON:
                        redImage = self.__redOpen
            counter += 1
            if counter % 7 == 0:
                meter += 1
                randNum = random.randint(1,2)
                if randNum == 1:
                    targets.append(Notes.Notes())
                counter = 1
            self.__drawBasics(blueImage, greenImage, orangeImage, redImage)
            score = self.__displayNotes(targets, score)
            checkWin = self.__displayScore(score, meter)
            if checkWin:
                gameOver = True
            pygame.display.update()
            # sleep -> frames per second (lower number = slower)
            self.__clock.tick(self.__framePerSec)

    def __displayScore(self, score, meter):
        # display high score and current score
        msg = "H: " + str(max(self.__totalScore))
        screenText = self.__font.render(msg, True, self.__white)
        self.__gameDisplay.blit(screenText, [10, 10])
        msg = "C: " + str(score)
        screenText = self.__font.render(msg, True, self.__white)
        self.__gameDisplay.blit(screenText, [10, 40])

        ## fill the meter ##
        if (score * 5 - meter) >= 0:
            yValue = score * 5 - meter
            pygame.draw.rect(self.__gameDisplay, self.__blue, [10, 400 - yValue, 50, yValue])
            if yValue >= 200:
                return True
            else:
                return False
        else:
            return False


    # prints whatever message you give with color specified
    def __messageToScreen(self, msg, score):
        if score > max(self.__totalScore):
            msg2 = "You have a new high of " + str(score)
            ###### SAVE HIGH SCORE ######
            self.__highScores[self.__user[0]] = score
            pickle.dump(self.__highScores, open("guitarHero/guitarHero.dat", "wb"))
            #############################
            screenText = self.__font.render(msg2, True, self.__white)
            self.__gameDisplay.blit(screenText, [self.__displayWidth // 4, 40])
        screenText = self.__font.render(msg, True, self.__white)
        self.__gameDisplay.blit(screenText, [self.__displayWidth // 4, 0])



    def __drawBasics(self, bImage, gImage, oImage, rImage):
        self.__gameDisplay.blit(bImage, [225, 550])
        self.__gameDisplay.blit(gImage, [325, 550])
        self.__gameDisplay.blit(oImage, [425, 550])
        self.__gameDisplay.blit(rImage, [525, 550])
        self.__gameDisplay.blit(self.__meter, [10, 200])
        # draw columns
        pygame.draw.line(self.__gameDisplay, self.__white, (200, 0), (200, 800), 2)
        pygame.draw.line(self.__gameDisplay, self.__white, (300, 0), (300, 800), 2)
        pygame.draw.line(self.__gameDisplay, self.__white, (400, 0), (400, 800), 2)
        pygame.draw.line(self.__gameDisplay, self.__white, (500, 0), (500, 800), 2)
        pygame.draw.line(self.__gameDisplay, self.__white, (600, 0), (600, 800), 2)


    def __displayNotes(self, targets, score):
        for obj in targets:
            color = obj.getRandColor()
            if color == 1:
                self.__gameDisplay.blit(self.__blueFill, [225, obj.getYValue()])
            elif color == 2:
                self.__gameDisplay.blit(self.__greenFill, [325, obj.getYValue()])
            elif color == 3:
                self.__gameDisplay.blit(self.__orangeFill, [425, obj.getYValue()])
            else:
                self.__gameDisplay.blit(self.__redFill, [525, obj.getYValue()])
            obj.moveY()
        if len(targets) != 0 and targets[0].getYValue() > self.__displayHeight:
            del targets[0]
            if score > 0:
                score -= 1
        return score


    def __checkHit(self, color, targets, score):
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
            if score > 0:
                score -= 1
        return score
