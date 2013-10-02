import pygame
class Perso(object):

	def __init__(self, img_droite, img_gauche, img_haut, img_bas):
		super(Perso, self).__init__()

		# On charge les images pour les differentes positions
		self.img_droite = pygame.image.load(img_droite).convert_alpha()
		self.img_gauche = pygame.image.load(img_gauche).convert_alpha()
		self.img_haut = pygame.image.load(img_haut).convert_alpha()
		self.img_bas = pygame.image.load(img_bas).convert_alpha()

		#Position du personnage en cases et en pixels
		self.x = 100
		self.y = 100

		#Direction par defaut
		self.direction = self.img_droite 

	def deplacer(self, direction):
		if direction == "droite":
			self.direction = self.img_droite
			self.x = self.x+3

		if direction == "gauche":
			self.direction = self.img_gauche
			self.x = self.x-3

		if direction == "haut":
			self.direction = self.img_haut
			self.y = self.y-3

		if direction == "bas":
			self.direction = self.img_bas
			self.y = self.y+3