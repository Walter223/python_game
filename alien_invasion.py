import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# Initialize pygame, settings, and screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Mutha Fuckin' Alien Invasion")

	# Set the background color.
	bg_color = (230,230,230)

	# Make a ship.
	ship = Ship(screen)

	# Start the main loop for the game.
	while True:

		# # Watch for keyboard and mouse events.
		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		sys.exit()
		# replace the above with the next line of code:
		gf.check_events(ship)
		ship.update()

		# # Redraw the screen during each pass through the loop.
		# screen.fill(ai_settings.bg_color)
		# ship.blitme()
		# Refactored to the below code:
		gf.update_screen(ai_settings, screen, ship)

		# Make the most recently drawn screen visible.
		pygame.display.flip()

run_game()