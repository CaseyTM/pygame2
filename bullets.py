import pygame;
from pygame.sprite import Sprite;
from hero import Hero;

class Bullet(Sprite):
	def __init__(self, screen, hero, game_settings, direction, bullet_type):
		super(Bullet, self).__init__();
		# get the screen so the object can use it whenever needed
		self.screen = screen;
		# create a bullet thingy from scratch 
		if bullet_type == 'vertical':
			self.rect = pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height);
		elif bullet_type == 'horizontal':
			self.rect = pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_width);
		self.rect.centerx = hero.rect.centerx;
		self.rect.centery = hero.rect.centery;
		# set the color of the bullet from game_settings
		self.color = game_settings.bullet_color;
		self.speed = game_settings.bullet_speed;
		# create an x and y property 
		self.x = self.rect.x;
		self.y = self.rect.y;
		self.direction = direction;

	def update(self):
		if self.direction == 'up':
			self.y -= self.speed;
		elif self.direction == 'down':
			self.y += self.speed;
		elif self.direction == 'left':
			self.x -= self.speed;
		elif self.direction == 'right':
			self.x += self.speed
		self.rect.y = self.y;
		self.rect.x = self.x;

	def draw_bullet(self):
		# draw rect takes 3 args, what entity, what color and what 
		pygame.draw.rect(self.screen, self.color, self.rect);