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


class NewBarrier:
    def __init__(self, displayWidth, displayHeight, blockSize,
                 moveX, move, first=False):
        moveDirection = random.randint(0, 1)
        # need to make the first block really big
        self.__move = move
        if first:
            self.__randX = moveX - 50
            self.__randY = 0
            self.__randWidth = displayWidth // 5
            self.__height = displayHeight
        else:
            if moveDirection == 0:
                self.__randX = moveX + self.__move
                while self.__randX >= displayWidth - displayWidth // 5:
                    self.__randX = moveX - self.__move
            else:
                self.__randX = moveX - self.__move
                while self.__randX < 0:
                    self.__randX = moveX + self.__move
            self.__randY = blockSize
            self.__randWidth = displayWidth // 5
            self.__height = blockSize * 2

    def moveY(self):
        self.__randY += 20

    def getX(self):
        return self.__randX

    def getY(self):
        return self.__randY

    def getWidth(self):
        return self.__randWidth

    def getHeight(self):
        return self.__height

    def __str__(self):
        return ("Random x: " + str(self.__randX) +
                "\nRandom width: " + str(self.__randWidth) +
                "\nRandom y: " + str(self.__randY))
