from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_score()

