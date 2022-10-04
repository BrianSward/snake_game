from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Ariel", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            contents = int(data.read())
            self.high_score = contents
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def goal(self):
        self.score += 1
        self.update_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_board()

    # used in older version where it just ended and didn't track high score
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)