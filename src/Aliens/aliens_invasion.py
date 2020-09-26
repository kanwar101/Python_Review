import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from aliens import Alien


from game_stats import GameStats


class AlienInvasion:

	"""Class to manage game assets"""

	def __init__(self):
		"""initializing the class"""
		pygame.init()

		self.settings = Settings()
		

		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		print (self.settings.screen_width)
		self.settings.screen_height = self.screen.get_rect().height

		pygame.display.set_caption("Alien Invasion")

		self.stats = GameStats(self)
		
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens=pygame.sprite.Group()

		self._create_fleet()

	def _create_fleet(self):
		"""Create fleet of aliens"""
		#Make an alien
		alien = Alien (self)
		alien_width, alien_height = alien.rect.size
		ship_height = self.ship.rect.height
		
		available_space = self.settings.screen_width - (2*alien_width)
		available_space_y = self.settings.screen_height - (3*alien_height) - ship_height
		number_aliens_x = available_space // (2*alien_width)
		number_rows = available_space_y // (2*alien_height)
		

		#create first row of aliens
		for row_number in range (number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, alien_width, alien_height, row_number)

	def _create_alien(self, alien_number, alien_width, alien_height, row_number):

			alien=Alien(self)
			alien.x = alien_width+2*alien_width*alien_number
			alien.rect.x = alien.x
			alien.rect.y = alien_height + 2*alien_height*row_number
			self.aliens.add(alien)

	def _fire_bullet(self):
		"""Create a bullet and add it to the group"""
		if len(self.bullets)<self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def run_game(self):
		"""Start the main loop of the game"""
		while True:
			self._check_event()
			self.ship.update()
			self._update_bullets()
			self._update_aliens()
			self._update_screen()



	def _update_bullets(self):
		self.bullets.update()

		#Get rid of bullets

		for bullet in self.bullets.copy():
			if bullet.rect.bottom <=0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collision()
		
	def _check_bullet_alien_collision(self):
		""" Check for any bullets that hit aliens
		 if so get rid of bullet and alien """
		collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
		
		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()

		print(len(self.bullets))




	def _check_event(self):
			#watch for quit 
			for event in pygame.event.get():
				if event.type ==pygame.QUIT:
					sys.exit()

				elif event.type == pygame.KEYDOWN:
					self._check_keydown_event(event)

				elif event.type ==pygame.KEYUP:
					self._check_keyup_event(event)


	def _check_keydown_event(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True

		if event.key == pygame.K_LEFT:
			self.ship.moving_left=True

		elif event.key==pygame.K_q:
			sys.exit()

		elif event.key == pygame.K_SPACE:
			self._fire_bullet() 

	def _check_keyup_event(self, event):			
		if event.key==pygame.K_RIGHT:
			self.ship.moving_right = False

		if event.key == pygame.K_LEFT:
			self.ship.moving_left=False
	
	def _update_aliens(self):
		"""Check if fleet is at the edge the update positions of all aliens in the fleet"""
		self._check_fleet_edges()
		self.aliens.update()

		#check if ship collides with aliens

		pygame.sprite.spritecollideany(self.ship, self.aliens)

		self._ship_hit()
		
	def _ship_hit (self):

		"""Respond to the ship hot by alien"""

		self.stats.ship_left -=1

		"""get rid of remaining bullets and ships"""
		self.aliens.empty()
		self.bullets.empty()

		#Create a new fleet

		self._create_fleet()
		self.ship.center_ship()

		#pause
		sleep (0.5)



	def _check_fleet_edges(self):
		"""Respond appropriately if any aliens have reached the edge"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change fleet's direction"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction*=-1


	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		for bullet in self.bullets.sprites():

			bullet.draw_bullet()

		self.aliens.draw(self.screen)

		# Refresh the screen
		pygame.display.flip()		

if __name__ == '__main__':
		ai = AlienInvasion()
		ai.run_game()

