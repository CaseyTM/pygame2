import pygame;
from pygame.sprite import Sprite;


class Hero(Sprite):
	# classes have props/data and methods
	def __init__(self, image, screen):
		# because this is a subclass we need to call super so the parent class can access the data
		super(Hero, self).__init__();
		self.image = pygame.image.load(image);
		self.image = pygame.transform.scale(self.image, (207,250));
		self.rect = self.image.get_rect();
		# add screen to the object so we can use/reuse it as needed 
		self.screen = screen;
		# find out the location and size of the screen
		self.screen_rect = self.screen.get_rect();
		# to put the hero on the left side, set the self.rect propersties to match those of the screen
		# accordingly
		self.rect.centery = self.screen_rect.centery;
		# set the left side of this object to the left side of the screen
		self.rect.left = self.screen_rect.left;
	def draw_me(self):
		self.screen.blit(self.image, self.rect)

	def update_me(self):
		# if user is pushin left, move my self.rect left etc
		if self.moving_right:
			# the hero moving_right booean is true, so update the hero location
			self.rect.centerx += 10 * self.speed;
		elif self.moving_left:
			self.rect.centerx -= 10 * self.speed;
		if self.moving_up:
			self.rect.centery -= 10 * self.speed;
		elif self.moving_down:
			self.rect.centery += 10 * self.speed;


		
