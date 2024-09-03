import turtle
from turtle import Turtle, Screen, mainloop
import random
screen = Screen()
colors = ["red" ,"green","blue", "yellow", "purple", "orange"]
is_race_om = False
screen.setup(500, 400)
all_turtles = []
user_bet = screen.textinput(title="make you bet", prompt="witch turtle will win the race enter a color? ")
y_i = [-70,-40, -10, 20 , 40 ,70, 90]
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-y_i[i])
    all_turtles.append(new_turtle)
    if user_bet:
        is_race_om = True
while is_race_om:
    if turtle.xcor() > 230:
        is_race_om = False
        winner = turtle.pencolor()
        if winner == user_bet:
           print(f"you won the {winner} is the winner")
        else:
           print(f"you lose the {winner} is the winner")

    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()