import pygame;
import sys;
from hero import Hero;

from bullets import Bullet;

# class Utility_functions(object):
# 	# @staticmethod


def check_events(screen, the_hero, game_settings, bullets, enemies):
	for event in pygame.event.get():

	# check to see if the event that occurred is the quit event
		if event.type == pygame.QUIT:
		# the user clicked the red X and the game should stop
			sys.exit();
		elif event.type == pygame.KEYDOWN:
			# what key was pressed?
			if event.key == pygame.K_SPACE:
				new_bullet = Bullet(screen, the_hero, game_settings, 'up', 'vertical');
				bullets.add(new_bullet);
			
			elif event.key == pygame.K_a:
				new_bullet = Bullet(screen, the_hero, game_settings, 'right', 'horizontal');
				bullets.add(new_bullet);
		
			elif event.key == pygame.K_RIGHT:
				the_hero.moving_right = True;
			elif event.key == pygame.K_LEFT:
				the_hero.moving_left = True;
			elif event.key == pygame.K_UP:
				the_hero.moving_up = True;
			elif event.key == pygame.K_DOWN:
				the_hero.moving_down = True;
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				the_hero.moving_right = False;
			elif event.key == pygame.K_LEFT:
				the_hero.moving_left = False;
			elif event.key == pygame.K_UP:
				the_hero.moving_up = False;
			elif event.key == pygame.K_DOWN:
				the_hero.moving_down = False;

def update_screen(screen, the_hero, game_settings, bullets, enemies):
		
	
		the_hero.draw_me();
		for bullet in bullets.sprites():
			bullet.update();
			bullet.draw_bullet();
		for enemy in enemies:
			enemy.update_me(the_hero);
			enemy.draw_me();
		# need to flip the screen, (wipe it out) so pygame can redraw
		pygame.display.flip();