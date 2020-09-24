import pygame


class Ship:

	"""create a ship"""
	def __init__ (self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		self.image = pygame.image.load('ship.bmp')
		self.rect=self.image.get_rect()

		self.rect.midbottom=self.screen_rect.midbottom

		#Movement flag
		self.moving_right=False
		self.moving_left=False

		self.settings = ai_game.settings

		self.x = float(self.rect.x)


	def update(self):
		"""UPdate Ship position based on the flag"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x+=self.settings.ship_speed

		elif self.moving_left and self.rect.left > 0:
			self.x-=self.settings.ship_speed

		self.rect.x = self.x

	def blitme (self):

		"""Draw ship at its current location"""
		self.screen.blit(self.image, self.rect)
