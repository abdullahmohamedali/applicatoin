import pygame
import sys
pygame.init()

window = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
island = pygame.image.load("assets2/ground.png")


def draw():
    window.fill((21,95,217))
    window.blit(island,(0,0))



while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            pygame.quit()
            sys.exit()
    draw()
  
    pygame.display.flip()
    clock.tick(60)
