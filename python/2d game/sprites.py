import pygame
from settings import *
import math
import random
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x , y):
        pygame.init()
        self.game = game
        self._layer = PLAYER_LAYER

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.hight = tile_size

        self.image = pygame.Surface([self.width, self.hight])
        self.image.fill(RED)

        self.rect = self.image.get_rect()

        self.rect.x  = self.x
        self.rect.y = self.y
    def update(self):
        pass
