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

import random


class Notes:
    def __init__(self):
        # randomly generate a number to represent the note that will be used
        # 1 == blue, 2 == green, 3 == orange, 4 == red
        self.__randColor = random.randint(1, 4)

        self.__yValue = 0

    def moveY(self):
        self.__yValue += 10

    def getRandColor(self):
        return self.__randColor

    def getYValue(self):
        return self.__yValue

    def __str__(self):
        return ("Y value: " + str(self.__randY) +
                "\nY value: " + str(self.__yValue))
