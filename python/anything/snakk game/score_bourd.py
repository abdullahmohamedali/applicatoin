from turtle import Turtle

class Score_bourd(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)

        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()
        self.high_score = 0

    def update_score(self):
        self.write(f"score: {self.score}high_score: {self.high_score}", False, "ALIGNMENT", ('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, "left", ('Arial', 24, 'normal'))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()