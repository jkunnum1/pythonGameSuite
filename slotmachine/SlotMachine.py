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

########## STUFF TO DO ##########
# possibly change images
# possible add gif
########## STUFF TO DO ##########


import pygame
import time
import random
import pickle


class SlotMachine:

    def __init__(self):
        #initialize pygame
        pygame.init()

        '''LOAD ONLINE USER'''
        self.__allUsers = pickle.load(open("users.dat", "rb"))
        self.__user = pickle.load(open("userOnline.dat", "rb"))

        #Set colors
        self.__white = (255,255,255)
        self.__black = (0,0,0)
        self.__gold = (255,205,0)

        #sets dimensions of screen
        self.__displayWidth = 800
        self.__displayHeight = 600
        self.__gameDisplay = pygame.display.set_mode((self.__displayWidth, self.__displayHeight))

        #Makes title
        pygame.display.set_caption('Slot Machine')
        self.__spinImage = pygame.image.load("slotmachine/pic0.png").convert()
        self.__oneImage = pygame.image.load("slotmachine/pic1.png").convert()
        self.__twoImage = pygame.image.load("slotmachine/pic2.png").convert()
        self.__threeImage = pygame.image.load("slotmachine/pic3.png").convert()
        self.__fourImage = pygame.image.load("slotmachine/pic4.png").convert()
        self.__imageList = [self.__spinImage, self.__oneImage, self.__twoImage, self.__threeImage, self.__fourImage]


        #set picture
        #titlePicture = pygame.image.load("slotMachine/slotMachinePicture.png")
        #pygame.display.set_icon(titlePicture)

        #What does this do?
        self.__clock = pygame.time.Clock()
        #####FPS = 35

        #Set font
        self.__font = pygame.font.SysFont("timesnewroman", 40)
        self.__main()
        pygame.quit()

    def __drawSpins(self, jSpin, kSpin, lSpin, score):
        self.__gameDisplay.fill(self.__black)
        text = self.__font.render("Score:" + str(score), False, self.__white)
        self.__gameDisplay.blit(text, (0, 0))
        pygame.draw.rect(self.__gameDisplay, self.__gold, [95, 145, 620, 242])
        self.__gameDisplay.blit(self.__imageList[jSpin], (100, 150))
        self.__gameDisplay.blit(self.__imageList[kSpin], (305, 150))
        self.__gameDisplay.blit(self.__imageList[lSpin], (510, 150))

    def __getRandImage(self):
        # the number of random things to land on
        randWheel = random.randint(1, 4)
        return randWheel

    def __addScore(self, score, firstWheel, secondWheel, thirdWheel):
        if firstWheel == secondWheel and firstWheel == thirdWheel:
            score += 50
        elif firstWheel == secondWheel:
            score += 10
        elif firstWheel == thirdWheel:
            score += 10
        elif secondWheel == thirdWheel:
            score += 10
        else:
            score += 0
        return score


    def __gameLoop(self, score):
        game = True
        jSpin = 0
        wheel1 = False
        kSpin = 0
        wheel2 = False
        lSpin = 0
        wheel3 = False
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                elif event.type == pygame.KEYDOWN:
                    # j, k and l will be the buttons to stop the corresponding
                    # wheel
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
            if jSpin != 0 and kSpin != 0 and lSpin != 0:
                text = self.__font.render("Score:" + str(score), False, self.__black)
                self.__gameDisplay.blit(text, (0, 0))
                return [jSpin, kSpin, lSpin]
            pygame.display.update()
            self.__clock.tick(7)

    def __welcomeLoop(self, message):
    #loop through game so it doesnt exit
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
            #Make background/title screen
            self.__gameDisplay.fill(self.__white)
            text = self.__font.render(message, False, self.__black)
            keepPlaying = self.__font.render("Press P for play, E for exit", False, self.__black)
            self.__gameDisplay.blit(text, (150,200))
            self.__gameDisplay.blit(keepPlaying, (150, 300))
            pygame.display.update()
            self.__clock.tick(7)

            #Update display
            pygame.display.update()

    def __endGame(self, message, score):
        restartGame = False
        while not restartGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return True
                    elif event.key == pygame.K_e:
                        return False
            text = self.__font.render("Score:" + str(score), False, self.__white)
            self.__gameDisplay.blit(text, (0, 0))
            text = self.__font.render(message, True, self.__white)
            text2 = self.__font.render("Press P for play, E for exit", True, self.__white)
            self.__gameDisplay.blit(text, (310, 100))
            self.__gameDisplay.blit(text2, (200, 400))
            pygame.display.update()
            self.__clock.tick(7)

    def __continueGame(self):
        play = True
        score = self.__allUsers[self.__user[0]][-1]
        sendBack = False
        while play:
            score -= 5
            spins = self.__gameLoop(score)
            originalScore = score
            score = self.__addScore(score, spins[0], spins[1], spins[2])
            if score - 5< 0:
                play = self.__welcomeLoop("Game Over! Play again?")
                if play:
                    sendBack = True
                    play = False
            elif score > originalScore:
                play = self.__endGame("You Won!", score)

            else:
                play = self.__endGame("You Lost!", score)
        ##### ADD TO THE TOTAL SCORE #####
        self.__user[-1] = score
        self.__allUsers[self.__user[0]] = self.__user
        pickle.dump(self.__allUsers, open("users.dat", "wb"))
        ##################################
        return sendBack


    def __main(self):
        playAgain = self.__welcomeLoop("Welcome to The Slot Machines!")
        while playAgain:
            playAgain = self.__continueGame()


