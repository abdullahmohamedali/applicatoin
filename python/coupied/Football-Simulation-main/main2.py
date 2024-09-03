import turtle
import random

# Initialize the window
win = turtle.Screen()
win.bgcolor('white')
win.title('FIFA Game')
win.setup(width=800, height=600)

# Goalkeeper class
class Goalkeeper(turtle.Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.speed(0)
        self.color(color)
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

# Player class
class Player(turtle.Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.speed(1)
        self.color(color)
        self.shape('circle')
        self.penup()
        self.goto(x, y)

# Ball class
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(1)
        self.color('black')
        self.shape('circle')
        self.penup()
        self.goto(0, 0)

# Goal class
class Goal(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.color('black')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

# Initialize players, goalkeeper, ball, and goals
player1 = Player('red', -200, 0)
player2 = Player('blue', 200, 0)
goalkeeper1 = Goalkeeper('red', -380, 0)
goalkeeper2 = Goalkeeper('blue', 380, 0)
ball = Ball()
goal1 = Goal(-400, 0)
goal2 = Goal(400, 0)

# Function to move players
def move_player_up(player):
    y = player.ycor()
    y += 20
    if y < 290:
        player.sety(y)

def move_player_down(player):
    y = player.ycor()
    y -= 20
    if y > -290:
        player.sety(y)

# Function to shoot the ball
def shoot_ball(player, ball, goal):
    if player.xcor() < 0:
        direction = 1  # Player 1 shoots towards the right
    else:
        direction = -1  # Player 2 shoots towards the left

    ball.goto(player.xcor() + direction * 50, player.ycor())
    ball.direction = direction
    ball.goal = goal

# Function to handle player 1 controls
def player1_controls():
    move_player_up(player1)
    move_player_down(player1)
    shoot_ball(player1, ball, goal2)

# Function to handle player 2 controls
def player2_controls():
    move_player_up(player2)
    move_player_down(player2)
    shoot_ball(player2, ball, goal1)

# Keyboard bindings
win.listen()
win.onkeypress(player1_controls, 'w')
win.onkeypress(player1_controls, 's')
win.onkeypress(player1_controls, 'a')
win.onkeypress(player1_controls, 'd')
win.onkeypress(player1_controls, 'space')

win.onkeypress(player2_controls, 'Up')
win.onkeypress(player2_controls, 'Down')
win.onkeypress(player2_controls, 'Left')
win.onkeypress(player2_controls, 'Right')
win.onkeypress(player2_controls, 'Return')

# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.direction * 5)

    # Check for collisions with the goals
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0, 0)  # Reset the ball position

    # Check for goals
    if goal1.xcor() - 10 < ball.xcor() < goal1.xcor() + 10 and goal1.ycor() - 50 < ball.ycor() < goal1.ycor() + 50:
        print("Goal for Player 2!")
        ball.goto(0, 0)

    if goal2.xcor() - 10 < ball.xcor() < goal2.xcor() + 10 and goal2.ycor() - 50 < ball.ycor() < goal2.ycor() + 50:
        print("Goal for Player 1!")
        ball.goto(0, 0)

    win.update()

