class Settings():
	"""A class to store all settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (50,50,50)

		# Ship settings
		self.ship_speed_factor = 3.5

		# Bullet settings
		self.bullet_speed_factor = 20
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 100,255,100
		self.bullets_allowed = 10

		# # Super Bullets
		# self.super_bullet_speed_factor = 10
		# self.super_bullet_width = 20
		# self.super_bullet_height = 20
		# self.super_bullet_color = 255,50,50
		# self.super_bullets_allowed = 2