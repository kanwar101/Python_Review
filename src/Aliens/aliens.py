import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class that represent single alien"""

	def __init__(self, ai_game):
		"""Initialize the alien and set its starting position"""
		super().__init__()
		self.screen = ai_game.screen

		#load the image
		self.image=pygame.image.load('alien.bmp')
		self.rect=self.image.get_rect()
		print (self.rect)
		self.rect.x = self.rect.width
		self.rect.y=self.rect.height

		self.x = float(self.rect.x)

