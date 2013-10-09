import pygame
from pygame.locals import *
from tile import Tile

class tileSet(object):

	def __init__(self, tileset):
		super(tileSet, self).__init__()
		self.tileset = tileset
		self.dictTileSet =  dict()
		self.dicttTile = dict()

	def load_tile_table(self, width, height):
		image = pygame.image.load(self.tileset).convert_alpha()
		image_width, image_height = image.get_size()

		i=0

		for tile_x in range(0, image_width/width):
			for tile_y in range(0, image_height/height):
				rect = (tile_x*width, tile_y*height, width, height)
				self.dictTileSet[i]=(image.subsurface(rect))
				i = i+1

	def genererDicoTile(self):
		self.dicttTile[0] = Tile(False, self.dictTileSet[26])
		self.dicttTile[1] = Tile(True, self.dictTileSet[22])
		self.dicttTile[4] = Tile(False, self.dictTileSet[36])

		return self.dicttTile