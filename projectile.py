import pygame
from pygame.locals import *

class Projectile(object):
	"""docstring for Projectile"""
	def __init__(self, rectPerso, damage, screen, stringPosition, bulletArray): 
		super(Projectile, self).__init__()

		self.projectileSurface = pygame.image.load("./ressources/images/Banana.png").convert_alpha()
		self.projectileRect = rectPerso
		self.enCour = True
		self.vitesse = 6
		self.damage = damage
		self.screen = screen

		self.bulletArray = bulletArray
		self.direction = stringPosition

	def update(self, camera, tileMap):
		if self.direction == "droite":
			self.projectileRect = self.projectileRect.move(self.vitesse,0)
			if tileMap.getTile(self.projectileRect.top, self.projectileRect.left+12).passable == False and tileMap.getTile(self.projectileRect.top+16, self.projectileRect.left+12).passable == False:
				self.vitesse = 0
				bulletArray = []
				self.enCour = False
		if self.direction == "gauche":
			self.projectileRect = self.projectileRect.move(-self.vitesse,0)
			if tileMap.getTile(self.projectileRect.top, self.projectileRect.left-1).passable == False and tileMap.getTile(self.projectileRect.top+16, self.projectileRect.left+1).passable == False:
				self.vitesse = 0
				bulletArray = []
				self.enCour = False
		if self.direction == "haut":
			self.projectileRect = self.projectileRect.move(0, -self.vitesse)
			if tileMap.getTile(self.projectileRect.top-1, self.projectileRect.left).passable == False and tileMap.getTile(self.projectileRect.top-1, self.projectileRect.left+16).passable == False:
				self.vitesse = 0
				bulletArray = []
				self.enCour = False
		if self.direction == "bas":
			self.projectileRect = self.projectileRect.move(0, self.vitesse)
			if tileMap.getTile(self.projectileRect.top+12, self.projectileRect.left).passable == False and tileMap.getTile(self.projectileRect.top+12, self.projectileRect.left+16).passable == False:
				self.vitesse = 0
				bulletArray = []
				self.enCour = False

		if self.enCour == True:
			self.screen.blit(self.projectileSurface, camera.apply(self.projectileRect))
		