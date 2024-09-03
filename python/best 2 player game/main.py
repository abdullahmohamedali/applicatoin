import pygame

pygame.font.init()

WIDTH,HIGHT = 800, 500
bullets_vel = 7
WHITE = (255,255,255)
vel = 5
FPS = 100
max_bullets = 1000000000000
yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2
RED = (255,0, 0)
YELLOW = (255,255,0)

font = pygame.font.SysFont('comicsans',40)

player_width,player_hight = 55,40
screen = pygame.display.set_mode((WIDTH,HIGHT))
black = (0,0,0)
pygame.display.set_caption("shooter")

yelow_player_image = pygame.image.load("yellow.png").convert_alpha()
yellow_player  =pygame.transform.rotate(pygame.transform.scale(yelow_player_image,(player_width,player_hight)),90)
border = pygame.Rect(WIDTH//2 -5,0, 10 , HIGHT)
bg = pygame.transform.scale(pygame.image.load("space.png"), (WIDTH,HIGHT)).convert_alpha()

red_player_image = pygame.image.load("red.png").convert_alpha()
red_player = pygame.transform.rotate(pygame.transform.scale(red_player_image,(player_width,player_hight)),270)
def yellow_move(keys,yellow):
        if keys[pygame.K_a] and  yellow.x - vel > 0 :
            yellow.x -= vel
        if keys[pygame.K_d] and yellow.x + vel + yellow.width < border.x :
            yellow.x += vel
        if keys[pygame.K_w] and yellow.y - vel > 0:
            yellow.y -= vel
        if keys[pygame.K_s] and yellow.y + vel + yellow.height < HIGHT - 17:
            yellow.y += vel
def red_move(keys,red):
        if keys[pygame.K_LEFT] and  red.x - vel > border.x + border.width :
            red.x -= vel
        if keys[pygame.K_RIGHT] and red.x + vel + red.width < WIDTH:
            red.x += vel
        if keys[pygame.K_UP] and red.y - vel > 0:
            red.y -= vel
        if keys[pygame.K_DOWN] and red.y + vel + red.height < HIGHT - 17:
            red.y += vel





def draw_widow(red,yellow,yellow_bulletsb,red_bullets, red_helth, yellow_helth):
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,black, border)
    red_health_text = font.render("Health: " + str(red_helth), 1, WHITE)
    yellow_health_text = font.render("Health: " + str(yellow_helth), 1, WHITE)
    screen.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    screen.blit(yellow_health_text, (10, 10))
    screen.blit(yellow_player,(yellow.x,yellow.y))
    screen.blit(red_player,(red.x,red.y))
    pygame.display.update()
    for bullet in red_bullets:
        pygame.draw.rect(screen, YELLOW, bullet)
        pygame.display.update()
    for bullet in yellow_bulletsb:
        pygame.draw.rect(screen, RED, bullet)
        pygame.display.update()

def handel_bullets(yellow_bulletsb,red_bullets,red,yellow):
     for bullet in yellow_bulletsb:
        bullet.x += bullets_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bulletsb.remove(bullet)


     for bullet in red_bullets:
        bullet.x -= bullets_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)
def draw_winner(text):
    draw_text = font.render(text, 1, WHITE)
    screen.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
 



def main():

    red = pygame.Rect(700, 300 ,player_width,player_hight)
    yellow = pygame.Rect(100, 300 ,player_width,player_hight)


    clock = pygame.time.Clock()


    red_bullets = []
    yellow_bulletsb = []
    red_helth = 5
    yellow_helth = 5
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type ==  pygame.KEYDOWN:
                 if event.key == pygame.K_LSHIFT and len(yellow_bulletsb) <  max_bullets:
                      bullets = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5)
                      yellow_bulletsb.append(bullets)
                 if event.key == pygame.K_RSHIFT and len(red_bullets) <  max_bullets:
                      bullets = pygame.Rect(red.x, red.y + red.height//2 -2, 10, 5)
                      red_bullets.append(bullets)

            if event.type == red_hit:
                red_helth -= 1
            if event.type == yellow_hit:
                yellow_helth -=1
            winner_text = ""
            if red_helth <=0:
                winner_text = "yellow wins!"
            if yellow_helth <0:
                winner_text = "red wins!"
            if winner_text != "":
                draw_winner(winner_text)
                break


        
        draw_widow(red, yellow,red_bullets,yellow_bulletsb,red_helth,yellow_helth)
        keys = pygame.key.get_pressed()
        yellow_move(keys,yellow)
        red_move(keys,red)
        handel_bullets(yellow_bulletsb,red_bullets,red,yellow)
        


    pygame.quit()

if __name__ == "__main__":
    main()
