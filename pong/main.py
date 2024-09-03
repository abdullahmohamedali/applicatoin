import pygame, sys
pygame.init()

WIDTH,HIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("platformer")


bg = "white"
ball = pygame.Rect(WIDTH/2 - 15, HIGHT/2 - 15,30,30)
palyer = pygame.Rect(WIDTH- 20, HIGHT/2 - 10,10,140)
openet = pygame.Rect(10, HIGHT/2 - 70,10,140)
run =  True
clock = pygame.time.Clock()
bg_color = pygame.Color('gray12')
light_gray = (200,200,200)
ball_speed_x = 7
ball_speed_y = 7


while run:
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    screen.fill(bg)
    pygame.draw.rect(screen,light_gray,palyer)
    pygame.draw.rect(screen,light_gray,openet)
    pygame.draw.ellipse(screen,light_gray, ball)


    pygame.display.flip()
    pygame.display.update()



