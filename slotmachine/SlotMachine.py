# Project
# Kunnumpurath, Julie
# A 53
# McLaughlin, William
# A 51
# Wehbe, Semaan
# A 52
# Burns, John Henry
# A 52
# Trackman, Rebecca
# A 52

import pygame
import time
import random
import pickle


class SlotMachine:

    def __init__(self):
        # initialize pygame
        pygame.init()

        '''LOAD ONLINE USER'''
        self.__allUsers = pickle.load(open("users.dat", "rb"))
        self.__user = pickle.load(open("userOnline.dat", "rb"))

        # Set colors
        self.__white = (255, 255, 255)
        self.__black = (0, 0, 0)
        self.__gold = (199, 114, 47)

        # sets dimensions of screen
        self.__displayWidth = 800
        self.__displayHeight = 600
        self.__gameDisplay = pygame.display.set_mode((self.__displayWidth,
                                                     self.__displayHeight))

        # Makes title
        pygame.display.set_caption('Slot Machine')
        self.__oneImage = pygame.image.load("slotmachine/images/" +
                                            "aPic.png").convert()
        self.__twoImage = pygame.image.load("slotmachine/images/" +
                                            "bearPic.png").convert()
        self.__threeImage = pygame.image.load("slotmachine/images/" +
                                              "deerPic.png").convert()
        self.__fourImage = pygame.image.load("slotmachine/images/" +
                                             "foxPic.png").convert()
        self.__fiveImage = pygame.image.load("slotmachine/images/" +
                                             "jPic.png").convert()
        self.__sixImage = pygame.image.load("slotmachine/images/" +
                                            "kPic.png").convert()
        self.__sevenImage = pygame.image.load("slotmachine/images/" +
                                              "naturePic.png").convert()
        self.__eightImage = pygame.image.load("slotmachine/images/" +
                                              "qPic.png").convert()
        self.__nineImage = pygame.image.load("slotmachine/images/" +
                                             "wolfPic.png").convert()
        self.__bgImage = pygame.image.load("slotmachine/images/" +
                                           "background.png").convert()
        self.__fullBGImage = pygame.image.load("slotmachine/images/" +
                                               "fullBackground.png").convert()
        self.__imageList = [self.__oneImage, self.__twoImage,
                            self.__threeImage, self.__fourImage,
                            self.__fiveImage, self.__sixImage,
                            self.__sevenImage, self.__eightImage,
                            self.__nineImage, "blank"]

        self.__clock = pygame.time.Clock()

        # Set font
        self.__font = pygame.font.SysFont("timesnewroman", 40)
        self.__gameMain()
        pygame.quit()

    def __drawSpins(self, jSpin, kSpin, lSpin, score):
        self.__gameDisplay.blit(self.__fullBGImage, [0, 0])
        text = self.__font.render("Score:" + str(score), False, self.__white)
        self.__gameDisplay.blit(text, (0, 0))
        pygame.draw.rect(self.__gameDisplay, self.__gold, [175, 185, 450, 160])
        self.__gameDisplay.blit(self.__bgImage, (185, 195))
        self.__gameDisplay.blit(self.__bgImage, (330, 195))
        self.__gameDisplay.blit(self.__bgImage, (475, 195))
        if jSpin == 9:
            tempVar = jSpin
            jSpin = random.randint(0, 8)
            while tempVar == jSpin:
                jSpin = random.randint(0, 8)
        self.__gameDisplay.blit(self.__imageList[jSpin], (190, 200))
        if kSpin == 9:
            tempVar = kSpin
            kSpin = random.randint(0, 8)
            while tempVar == kSpin:
                kSpin = random.randint(0, 8)
        self.__gameDisplay.blit(self.__imageList[kSpin], (335, 200))
        if lSpin == 9:
            tempVar = lSpin
            lSpin = random.randint(0, 8)
            while tempVar == lSpin:
                lSpin = random.randint(0, 8)
        self.__gameDisplay.blit(self.__imageList[lSpin], (480, 200))

    def __getRandImage(self):
        # the number of random things to land on
        randWheel = random.randint(0, 8)
        return randWheel

    def __addScore(self, score, firstWheel, secondWheel, thirdWheel):
        if firstWheel == secondWheel and firstWheel == thirdWheel:
            score += 50
        elif firstWheel == secondWheel:
            score += 5
        elif firstWheel == thirdWheel:
            score += 5
        elif secondWheel == thirdWheel:
            score += 5
        else:
            score += 0
        return score

    def __gameLoop(self, score):
        game = True
        jSpin = 9
        wheel1 = False
        kSpin = 9
        wheel2 = False
        lSpin = 9
        wheel3 = False
        try:
            while game:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        # j, k and l will be the buttons to stop the
                        # corresponding wheel
                        if event.key == pygame.K_j and not wheel1:
                            jSpin = self.__getRandImage()
                            wheel1 = True
                        if event.key == pygame.K_k and not wheel2:
                            kSpin = self.__getRandImage()
                            wheel2 = True
                        if event.key == pygame.K_l and not wheel3:
                            lSpin = self.__getRandImage()
                            wheel3 = True
                self.__drawSpins(jSpin, kSpin, lSpin, score)
                if wheel1 and wheel2 and wheel3:
                    text = self.__font.render("Score:" + str(score), False,
                                              self.__black)
                    self.__gameDisplay.blit(text, (0, 0))
                    return [jSpin, kSpin, lSpin]
                pygame.display.update()
                self.__clock.tick(15)
        except:
            return

    def __welcomeLoop(self, message):
        # loop through game so it doesnt exit
        exitGame = False
        while not exitGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return True
                    elif event.key == pygame.K_e:
                        return False
            # Make background/title screen
            self.__gameDisplay.blit(self.__fullBGImage, [0, 0])
            text = self.__font.render(message, False, self.__white)
            keepPlaying = self.__font.render("Press P for play, E for exit",
                                             False, self.__white)
            self.__gameDisplay.blit(text, (150, 200))
            self.__gameDisplay.blit(keepPlaying, (150, 300))
            pygame.display.update()
            self.__clock.tick(7)

            # Update display
            pygame.display.update()

    def __endGame(self, message, score):
        restartGame = False
        while not restartGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return True
                    elif event.key == pygame.K_e:
                        return False
            text = self.__font.render("Score:" + str(score), False,
                                      self.__white)
            self.__gameDisplay.blit(text, (0, 0))
            text = self.__font.render(message, True, self.__white)
            text2 = self.__font.render("Press P for play, E for exit", True,
                                       self.__white)
            self.__gameDisplay.blit(text, (310, 100))
            self.__gameDisplay.blit(text2, (200, 400))
            pygame.display.update()
            self.__clock.tick(7)

    def __noPoints(self):
        exit = False
        while not exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        return
            text = self.__font.render("You have no points to gamble!", True,
                                      self.__white)
            text2 = self.__font.render("Earn points to play slots", True,
                                       self.__white)
            text3 = self.__font.render("Press e to exit", True, self.__white)
            self.__gameDisplay.blit(text, (160, 100))
            self.__gameDisplay.blit(text2, (200, 400))
            self.__gameDisplay.blit(text3, (290, 450))
            pygame.display.update()
            self.__clock.tick(7)

    def __continueGame(self, score):
        play = True
        sendBack = False
        while play:
            try:
                score -= 5
                spins = self.__gameLoop(score)
                originalScore = score
                score = self.__addScore(score, spins[0], spins[1], spins[2])
                if score - 5 < 0:
                    self.__noPoints()
                    play = False
                elif score > originalScore:
                    play = self.__endGame("You Won!", score)

                else:
                    play = self.__endGame("You Lost!", score)
            except:
                play = False
        # ADD TO THE TOTAL SCORE #
        self.__user[-1] = score
        self.__allUsers[self.__user[0]] = self.__user
        pickle.dump(self.__allUsers, open("users.dat", "wb"))
        #
        return sendBack

    def __gameMain(self):
        score = self.__allUsers[self.__user[0]][-1]
        if score < 5:
            self.__noPoints()
        else:
            playAgain = self.__welcomeLoop("Welcome to The Slot Machines!")
            while playAgain:
                playAgain = self.__continueGame(score)
