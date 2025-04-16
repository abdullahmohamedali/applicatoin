import pygame, sys
from settings import *
from level import Level
import time

# import debugpy
# debugpy.listen(("localhost", 5678))  # This opens a debug connection
# print("Waiting for debugger to attach...")
# debugpy.wait_for_client()  # The game will pause here until VS Code connects



class Game:
sd	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		pygame.display.set_caption('Sprout land')
		self.clock = pygame.time.Clock()
		self.level = Level()

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			dt = self.clock.tick() / 1000
			self.level.run(dt)
			pygame.display.update()
if __name__ == '__main__':
	game = Game()   
	game.run()
