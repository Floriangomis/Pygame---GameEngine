import pygame
from pygame.locals import *
from tile import Tile

class tileMap(object):
	"""docstring for tileMap"""
	def __init__(self, listMatrix, dicoTile, fenetre):
		super(tileMap, self).__init__()
		self.tileMap = listMatrix
		self.dicoTile = dicoTile
		self.screen = fenetre
		
		for x in range(len(self.tileMap)):
			for height in range(len(self.tileMap[x])):
				for width in range(len(self.tileMap[x][height])):
					if self.tileMap[x][height][width] == '0':
						surfaceC = self.dicoTile[0].getSurface().copy()
						tile = Tile(False, surfaceC)
						self.tileMap[x][height][width] = tile
					elif self.tileMap[x][height][width] == '1':
						surfaceC = self.dicoTile[1].getSurface().copy()
						tile = Tile(True, surfaceC)
						self.tileMap[x][height][width] = tile
					elif self.tileMap[x][height][width] == '4':
						surfaceC = self.dicoTile[4].getSurface().copy()
						tile = Tile(False, surfaceC)
						self.tileMap[x][height][width] = tile		

	def mapRender(self):
		for x in range(len(self.tileMap)):
			for height in range(len(self.tileMap[x])):
				for width in range(len(self.tileMap[x][height])):
					self.tileMap[x][height][width].draw(self.screen, self.tileMap[x][height][width].setPositionAndGet(width*48, height*48))

	def getTile(self, posY, posX):
		return self.tileMap[1][posY/48][posX/48]