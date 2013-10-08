import pygame
from pygame.locals import *

class tileMap(object):
	"""docstring for tileMap"""
	def __init__(self, arrayMap, dicoTile, fenetre):
		super(tileMap, self).__init__()
		self.arrayMap = arrayMap
		self.dicoTile = dicoTile
		self.screen = fenetre



	def mapRender(self):		

		for width in range(len(self.arrayMap)):
			for height in range(len(self.arrayMap[width])):
				if self.arrayMap[width][height] == '0':
					self.screen.blit(self.dicoTile[0].getSurface(), (height*48, (width)*48))
				if self.arrayMap[width][height] == '1':
					self.screen.blit(self.dicoTile[1].getSurface(), (height*48, (width)*48))
				if self.arrayMap[width][height] == '4':
					self.screen.blit(self.dicoTile[4].getSurface(), (height*48, (width)*48))
