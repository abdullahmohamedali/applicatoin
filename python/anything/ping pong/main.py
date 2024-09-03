from turtle import Screen, Turtle, mainloop
from paddel import Paddel
from ball import Ball
from scorebourd import Score_bourd
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)

r_paddel = Paddel((350, 0))
l_paddel = Paddel((-350, 0))
ball = Ball()
score_board = Score_bourd()




screen.listen()
screen.onkeypress(l_paddel.go_up, "w")
screen.onkeypress(l_paddel.go_down, "s")
screen.onkeypress(r_paddel.go_up, "Up")
screen.onkeypress(r_paddel.go_down, "Down")
game_is_on = True


while game_is_on:
    time.sleep(0.09)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddel) < 50 and ball.xcor() > 320 or ball.distance(l_paddel) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_p()
        score_board.l_point()
    if ball.xcor() < -380:
        ball.reset_p()
        score_board.r_point()






screen.exitonclick()

screen.mainloop()
