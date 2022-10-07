from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f'Level: {self.level}', align=ALIGMENT, font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGMENT, font=FONT)