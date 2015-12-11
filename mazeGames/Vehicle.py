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


class Vehicle:
    def __init__(self, display, color, size, leadX, leadY):
        self.__display = display
        self.__color = color
        self.__size = size
        self.__leadX = leadX
        self.__leadY = leadY
        self.__change = 0

    def getX(self):
        return self.__leadX

    def getY(self):
        return self.__leadY

    def moveX(self, change):
        self.__change = change

    # redraws the vehicle
    def drawVehicle(self):
        self.__leadX += self.__change
        pygame.draw.rect(self.__display, self.__color,
                         [self.__leadX, self.__leadY, self.__size,
                          self.__size])
