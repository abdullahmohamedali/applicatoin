from turtle import Screen
from snake import Snake
from food import Food
from score_bourd import Score_bourd
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = Score_bourd()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on_on = True
while game_on_on:
    snake.move()
    time.sleep(0.1)
    screen.update()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()


    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on_on = False
        score_board.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on_on = False
            score_board.game_over()


screen.exitonclick()
