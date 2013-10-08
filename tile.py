import pygame
from pygame.locals import *

class Tile(object):
	def __init__(self, passable, surface):
		super(Tile, self).__init__()
		self.passable = passable
		self.x = 0
		self.y = 0
		self.surface = surface

	def setPosition(posX, posY):
		self.x = posX
		self.y = posY

	def getSurface(self):
		return self.surface