import pygame
from pygame.locals import *
from projectile import Projectile

class Perso(object):

	def __init__(self, img_droite, img_gauche, img_haut, img_bas, positionX, positionY, fenetre):
		super(Perso, self).__init__()
		#On recupere la surface sur laquelle on blittera le personnage
		self.screen = fenetre

		# On charge les images pour les differentes positions
		self.img_droite = pygame.image.load(img_droite).convert_alpha()
		self.img_gauche = pygame.image.load(img_gauche).convert_alpha()
		self.img_haut = pygame.image.load(img_haut).convert_alpha()
		self.img_bas = pygame.image.load(img_bas).convert_alpha()

		#imageDirection par defaut
		self.imageDirection = self.img_droite
		self.stringPosition = "droite"

		#Position du personnage en cases et en pixels
		self.rectPerso = self.imageDirection.get_rect()
		self.rectPerso = self.rectPerso.move(positionX, positionY)

		#Caracteristique du personnage
		self.atk = 0.5*2
		self.force = 4
		self.vitalite = 4
		self.Hp = self.vitalite*10

		# Le projectile lie au hero
		self.bullets_array = []
		self.maxBullet = 1

	def event(self, tileMap, camera):
		for event in pygame.event.get():
			if event.type == QUIT:
				continuer = 0
		
		keys = pygame.key.get_pressed()
		#if tileMap.getTile(self.rectPerso.top+3, self.rectPerso.left).passable != False:            ->>> Collision Test 		
		if keys[K_RIGHT]:
			self.imageDirection = self.img_droite 
			self.stringPosition = "droite"
			if tileMap.getTile(self.rectPerso.top, self.rectPerso.left+33).passable == True and tileMap.getTile(self.rectPerso.top+30, self.rectPerso.left+33).passable == True:
				self.rectPerso = self.rectPerso.move(3,0)
				self.screen.blit(self.imageDirection,  camera.apply(self.rectPerso))
		if keys[K_LEFT]:
			self.imageDirection = self.img_gauche
			self.stringPosition = "gauche"
			if tileMap.getTile(self.rectPerso.top, self.rectPerso.left-3).passable == True and tileMap.getTile(self.rectPerso.top+30, self.rectPerso.left-3).passable == True:
				self.rectPerso = self.rectPerso.move(-3,0)
				self.screen.blit(self.imageDirection,  camera.apply(self.rectPerso))
		if keys[K_UP]:
			self.imageDirection = self.img_haut
			self.stringPosition = "haut"
			if tileMap.getTile(self.rectPerso.top-3, self.rectPerso.left).passable == True and tileMap.getTile(self.rectPerso.top-3, self.rectPerso.left+30).passable == True:
				self.rectPerso = self.rectPerso.move(0,-3)
				self.screen.blit(self.imageDirection,  camera.apply(self.rectPerso))
		if keys[K_DOWN]:
			self.imageDirection = self.img_bas
			self.stringPosition = "bas"
			if tileMap.getTile(self.rectPerso.top+33, self.rectPerso.left).passable == True and tileMap.getTile(self.rectPerso.top+33, self.rectPerso.left+30).passable == True:
				self.rectPerso = self.rectPerso.move(0,3)
				self.screen.blit(self.imageDirection,  camera.apply(self.rectPerso))

		if keys[K_SPACE]:
			if len(self.bullets_array) < self.maxBullet:
				proj = Projectile(self.rectPerso, self.atk, self.screen, self.stringPosition, self.bullets_array)
				self.bullets_array.append(proj)

		for bullet in self.bullets_array:
			if bullet.enCour == True:
				bullet.update(camera, tileMap)
			else:
				self.bullets_array = []


		self.screen.blit(self.imageDirection, camera.apply(self.rectPerso))
