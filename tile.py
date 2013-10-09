import pygame
from pygame.locals import *

class Tile(object):
	def __init__(self, passable, surface):
		super(Tile, self).__init__()
		self.passable = passable
		self.x = 0
		self.y = 0
		self.position = (self.x, self.y)
		self.surface = surface
		self.rect = self.surface.get_rect()

	def setPosition(posX, posY):
		self.x = posX
		self.y = posY

	def getSurface(self):
		return self.surface

	def setPositionAndGet(self, posX, posY):
		self.x = posX
		self.y = posY
		self.rect = ((posX, posY), (self.surface.get_rect().width, self.surface.get_rect().height))
		return self.rect

	def draw(self, screen, position):
		screen.blit(self.getSurface(), position)
