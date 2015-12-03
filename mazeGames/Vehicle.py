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
 		pygame.draw.rect(self.__display, self.__color, [self.__leadX, self.__leadY, self.__size, self.__size])
