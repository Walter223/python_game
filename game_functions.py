import sys

import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""Respond to keypresses."""
	if event.key in (pygame.K_RIGHT, pygame.K_d):
		ship.moving_right = True
	elif event.key in (pygame.K_LEFT, pygame.K_a):
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	# elif event.key in (pygame.K_UP, pygame.K_w):
	# 	ship.moving_up = True
	# elif event.key in (pygame.K_DOWN, pygame.K_s):
	# 	ship.moving_down = True
		
def fire_bullet(ai_settings, screen, ship, bullets):
	"""Fire a bullet if limit not reached yet."""
	# Create a new bullet and add it to the bullets group.
	if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)

def update_bullets(bullets):
	"""Update position of bullets and get rid of old bullets."""
	# Update bullet positions.
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def check_keyup_events(event,ship):
	"""Respond to keyups."""
	if event.key in (pygame.K_RIGHT, pygame.K_d):
		ship.moving_right = False
	elif event.key in (pygame.K_LEFT, pygame.K_a):
		ship.moving_left = False
	# elif event.key in (pygame.K_UP, pygame.K_w):
	# 	ship.moving_up = False
	# elif event.key in (pygame.K_DOWN, pygame.K_s):
	# 	ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

def update_screen(ai_settings, screen, ship, bullets):
	"""Update images on the screen and flip to the new screen."""

	# Redraw the screen during each pass through the loop.
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	# Make the most recently drawn screen visible.
	pygame.display.flip()

	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()