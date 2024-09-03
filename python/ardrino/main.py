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


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "a")
screen.onkey(move_left, "s")
screen.onkey(move_right, "d")
while True:
    a + 1

