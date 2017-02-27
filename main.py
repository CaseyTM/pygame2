import pygame;
from game_functions import check_events, update_screen;
from hero import Hero;
from settings import Settings;
from pygame.sprite import Group, groupcollide;
import time;
from enemy import Enemy;

# from game_functions import Utility_functions;

# Utility_functions.check_events():

# Core game loop and functionality
def run_game():
	# initialize all the pygame stuff
	pygame.init();
	# create a settings object
	game_settings = Settings();
	# create a tuple for the screen size
	# screen_size = (game_settings.screen_size);
	# create a screen for our game to use
	screen = pygame.display.set_mode(game_settings.screen_size)
	# this sets the title of the window
	pygame.display.set_caption("a heroic pygame shooter")
	# make the main game loop that will permanently run_game

	# create a hero object from our hero class 
	the_hero = Hero('images/hero.png', screen);

	# make a group for the bullets to live in 
	bullets = Group();
	enemies = Group();
	game_start_time = time.time();
	print game_start_time



	while 1:
		screen.fill(game_settings.bg_color);
		game_settings.timer = (time.time() - game_start_time);
		print int(game_settings.timer);
		if (int(game_settings.timer) % 5 == 0) and game_settings.monster_count == 0:
			enemies.add(Enemy(screen,game_settings));
			game_settings.monster_count += 1;
		# pygame automatically creates an event queue like JS
		# we want to be able to patch into certain events like click, keypress etc.

		# create a tuple for the background color 256 max for rgb format
		check_events(screen, the_hero, game_settings, bullets, enemies);
		update_screen(screen, the_hero, game_settings, bullets,enemies);
run_game()