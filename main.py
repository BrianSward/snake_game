from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.body[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.goal()

    if snake.body[0].xcor() > 300 \
            or snake.body[0].xcor() < -300 \
            or snake.body[0].ycor() > 300 \
            or snake.body[0].ycor() < -300:
        scoreboard.reset()
        snake.reset()

    for piece in snake.body[1:]:
        if snake.head.distance(piece) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
