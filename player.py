from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.back_to_start()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def back_to_start(self):
        self.goto(STARTING_POSITION)

    def collision_detected(self):
        self.goto(0, 0)
        self.hideturtle()
        self.write("Uh-Oh!Crashed.GAME OVER.", align="center", font=FONT)
