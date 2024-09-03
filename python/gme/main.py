import pygame
from sys import exit
import time
pygame.init()
def display_score():
	current_time = int(pygame.time.get_ticks() / 1000)
	score_surf = font.render(f'Score: {current_time}',False,(64,64,64))
	score_rect = score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("dino game")
font = pygame.font.Font('font/Pixeltype.ttf', 50)
clock = pygame.time.Clock()
game_acive = True
sky_surfas = pygame.image.load('assets/Sky.png').convert_alpha()
ground_surface = pygame.image.load('assets/ground.png').convert_alpha()

over_surf = font.render('game over',False,'black')
over_rect = over_surf.get_rect(midbottom = (400,200))




player_surface = pygame.image.load('assets/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

snail_surf = pygame.image.load('assets/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20

    if game_acive:
        screen.blit(sky_surfas,(0,0))
        screen.blit(ground_surface,(0,300))
        display_score()



        snail_rect.x -= 5
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surf,snail_rect) 




        player_gravity +=1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surface,player_rect)
        if snail_rect.colliderect(player_rect):
            game_acive = False
    else:

        screen.blit(over_surf, over_rect)
    pygame.display.update()
    clock.tick(60)
