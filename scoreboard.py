from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.level = 0
        self.penup()
        self.hideturtle()
        self.score_display()

    def score_display(self):
        self.goto(-250, 270)
        self.write(arg=f"Level: {self.level}", align="center", font=("Courier", 14, "normal"))

    def score_level_up(self):
        self.level += 1
        self.clear()
        self.score_display()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(arg="Game over", align="center", font=("Courier", 25, "normal"))
