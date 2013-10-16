import pygame
from pygame.locals import *

class Npc(object):
	"""docstring for Npc"""
	def __init__(self, img_bas,positionX, positionY, fenetre, perso):
		super(Npc, self).__init__()
		self.screen = fenetre
		self.hero = perso

		self.posXInitiale = positionX
		self.boolRetour = False
		self.boolAlle = True
		# On charge les images pour les differentes positions
		self.img_bas = pygame.image.load(img_bas).convert_alpha()
		#imageDirection par defaut
		self.imageDirection = self.img_bas
		#Position du personnage en cases et en pixels
		self.rectNpc = self.imageDirection.get_rect()
		self.rectNpc = self.rectNpc.move(positionX, positionY)

		self.alive = True

	def event(self, tileMap, camera):
		if self.rectNpc.colliderect(self.hero.rectPerso):
			print "Collision"
		if len(self.hero.bullets_array) > 0:
			if self.rectNpc.colliderect(self.hero.bullets_array[0].projectileRect):
				self.alive = False

		self.animationNpc(tileMap)
		self.screen.blit(self.imageDirection, camera.apply(self.rectNpc))

	def animationNpc(self, tileMap):
		if self.boolAlle == True:
			if tileMap.getTile(self.rectNpc.top, self.rectNpc.left+33).passable == True:
				self.rectNpc = self.rectNpc.move(1,0)
				if self.rectNpc.left >= self.posXInitiale +120:
					self.boolRetour = True
					self.boolAlle = False
			else:
				self.boolRetour = True
				self.boolAlle = False
		if self.boolRetour == True:
			if tileMap.getTile(self.rectNpc.top, self.rectNpc.left-3).passable == True and tileMap.getTile(self.rectNpc.top-30, self.rectNpc.left-3).passable == True:
				self.rectNpc = self.rectNpc.move(-1,0)
				if self.rectNpc.left == self.posXInitiale-30:
					self.boolRetour = False
					self.boolAlle = True
			else:
				self.boolRetour = False
				self.boolAlle = True

