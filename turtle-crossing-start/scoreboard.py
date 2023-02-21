from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("blue")
        self.penup()
        self.goto(-270, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Your turtle was run over! Game Over", align="center", font=FONT)

    def add_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

