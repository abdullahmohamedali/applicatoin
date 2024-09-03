import pygame
from sprites import *
from settings import *
import sys


class game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH,HIGHT])
        self.clock = pygame.time.Clock()
        self.running = True
    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attaks = pygame.sprite.LayeredUpdates()
        self.player = Player(self, 1, 2)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    def update1(self):
        self.all_sprites.update()
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    def main(self): 
        while self.running:
            self.events()
            self.update1()
            self.draw()
        self.running = False
    def game_over(self):
        pass
    def intro_screen(self):
        pass
g = game()
g.intro_screen()
game().new()
while g.running:
    g.main()
    g.game_over()
pygame.quit()
sys.exit()


