from turtle import Turtle, Screen, mainloop
a = 0
tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()








screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(clear, "space")


screen.exitonclick()
