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

import random

class Barriers:
    def __init__(self, displayWidth, displayHeight, blockSize):
        # start at -50 so that images are more likely to appear
        # on the left side of the screen
        self.__randX = round(random.randrange(-50, displayWidth) / 10.0) * 10.0
        self.__randWidth = round(random.randrange(displayWidth // 4,
                                                  displayWidth // 3) / 10.0) * 10.0
        if self.__randX + self.__randWidth > displayWidth:
            self.__randX = displayWidth - self.__randWidth
        self.__randY = 10
        

    def moveY(self):
        self.__randY += 10

    def getX(self):
        return self.__randX

    def getY(self):
        return self.__randY

    def getWidth(self):
        return self.__randWidth
    
    def __str__(self):
        return ("Random x: " + str(self.__randX) +
                "\nRandom width: " + str(self.__randWidth) +
                "\nRandom y: " + str(self.__randY))

    
