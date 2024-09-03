import pygame, sys

pygame.init()
clock = pygame.time.Clock()
PLAYER_VEL = 5

screen = pygame.display.set_mode((800,800))
player_surface = pygame.image.load('assets2/player.png').convert_alpha()
player_rect = player_surface.get_rect(midright= (0,0))
ground_surf = pygame.image.load('assets2/ground.png').convert_alpha()
ground_rect = ground_surf.get_rect()

        

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_a]:
           player_rect.x -= PLAYER_VEL
        if keys[pygame.K_d]:
            player_rect.x += PLAYER_VEL
        if keys[pygame.K_w]:
            player_rect.y -= PLAYER_VEL
        if keys[pygame.K_s]:
            player_rect.y += PLAYER_VEL
    screen.blit(ground_surf,ground_rect)
    screen.blit(player_surface,player_rect)
    pygame.display.flip()
    clock.tick(60)