
class GameStats:

	"""Track statistics of Game"""

	def __init__(self, ai_game):
		"""initialize statistics"""
		self.settings = ai_game.settings

		self.reset_stats()



	def reset_stats (self):
		"""Initialize stats that change during the game"""
		self.ship_left=self.settings.ship_limit

