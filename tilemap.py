import pygame
from pygame.locals import *
from tile import Tile

class tileMap(object):
	"""docstring for tileMap"""
	def __init__(self, arrayMap, dicoTile, fenetre):
		super(tileMap, self).__init__()
		self.tileMap = arrayMap
		self.dicoTile = dicoTile
		self.screen = fenetre
		
		for height in range(len(self.tileMap)):
			for width in range(len(self.tileMap[height])):
				if self.tileMap[height][width] == '0':
					surfaceC = self.dicoTile[0].getSurface().copy()
					tile = Tile(False, surfaceC)
					self.tileMap[height][width] = tile
				elif self.tileMap[height][width] == '1':
					surfaceC = self.dicoTile[1].getSurface().copy()
					tile = Tile(True, surfaceC)
					self.tileMap[height][width] = tile
				elif self.tileMap[height][width] == '4':
					surfaceC = self.dicoTile[4].getSurface().copy()
					tile = Tile(False, surfaceC)
					self.tileMap[height][width] = tile		

	def mapRender(self):
		for height in range(len(self.tileMap)):
			for width in range(len(self.tileMap[height])):
				#print self.tileMap[height][width], height , width, self.tileMap[height][width].getSurface()
				self.tileMap[height][width].draw(self.screen, self.tileMap[height][width].setPositionAndGet(width*48, height*48))

	def getTile(self, posY, posX):
		return self.tileMap[posY/48][posX/48]