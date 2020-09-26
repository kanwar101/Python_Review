
class Settings:

	"""Class that contains variables"""

	def __init__(self):
		"""Initialize the game's settings"""
		#Screen settings

		self.screen_width=800
		self.screen_height = 600
		self.bg_color=(230,230,230)

		self.ship_speed = 1.5

		#BUllet Charactersitics

		self.bullet_speed = 1.0
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color =(60,60,60)

		self.bullets_allowed = 5

		#alien speed

		self.alien_speed = 1.0

		self.fleet_drop_speed = 100
		#fleet direction 1 = right and -1 = left

		self.fleet_direction = 1

		# Ship attribute
		self.ship_limit = 3


