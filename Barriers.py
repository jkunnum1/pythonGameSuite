import random

class Barriers:
    def __init__(self, displayWidth, blockSize):
        self.__randX = round(random.randrange(0, displayWidth) / 10.0) * 10.0
        self.__randWidth = round(random.randrange(0, displayWidth, blockSize) / 10.0) * 10.0
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

    
