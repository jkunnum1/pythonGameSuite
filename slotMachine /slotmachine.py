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

#initialize pygame
pygame.init()

#Set colors
white = (255,255,255)
black = (0,0,0)

#sets dimensions of screen
displayWidth = 800
displayHeight = 600
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

#Makes title
pygame.display.set_caption('Slot Machine')

#set picture
#titlePicture = pygame.image.load("slotMachine/slotMachinePicture.png")
#pygame.display.set_icon(titlePicture)

#What does this do?
clock = pygame.time.Clock()
FPS = 35

#Set font
font = pygame.font.SysFont("timesnewroman", 40)

def gameLoop():
#loop through game so it doesnt exit
    exitGame = False
    while not exitGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    exitGame = True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        #Make background/title screen
        gameDisplay.fill(white)
        text = font.render("Welcome to The Slot Machines!", False, black)
        keepPlaying = font.render("Press C to play or Q to quit", False, black)
        gameDisplay.blit(text, (150,200))
        gameDisplay.blit(keepPlaying, (150, 300))
        pygame.display.update()
        clock.tick(7)

        #Update display
        pygame.display.update()

def endGame():
    restartGame = False
    while not restartGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    restartGame = True
                elif event.key == pygame.K_q:
                    restartGame = False

        gameDisplay.fill(white)
        text = largeFont.render("Great Job!", True, black)
        text2 = smallFont.render("C for play, Q for quit", True, black)
        gameDisplay.blit(text, (150, 200))
        gameDisplay.blit(text2, (150, 300))
        pygame.display.update()
        clock.tick(7)

def gameOver():
    restartGame = False
    while not restartGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    restartGame = True
                elif event.key == pygame.K_q:
                    restartGame = False

        gameDisplay.fill(white)
        text = largeFont.render("Game Over", True, black)
        text2 = smallFont.render("C for play, Q for quit", True, black)
        gameDisplay.blit(text, (150, 200))
        gameDisplay.blit(text2, (150, 300))
        pygame.display.update()
        clock.tick(7)
        


def main():
    gameLoop()

main()
