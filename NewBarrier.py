import random

class NewBarrier:
    def __init__(self, displayWidth, displayHeight, blockSize, moveX):
        move = random.randint(0, 1)
        if move == 0:
            self.__randX = moveX + 20
            while self.__randX >= displayWidth - displayWidth //5:
                self.__randX = moveX - 20
        else:
            self.__randX = moveX - 20
            while self.__randX < 0:
                self.__randX = moveX + 20
        self.__randWidth = displayWidth // 5
        self.__randY = blockSize

        
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

    
