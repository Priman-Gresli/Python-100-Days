import time
from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

root = screen.getcanvas().winfo_toplevel()
root.lift()
root.attributes('-topmost', True)
# drop the "always on top" flag after the window is focused
root.after(200, lambda: root.attributes('-topmost', False))
root.focus_force()

snake=Snake()
food=Food()
score_board=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # eating food
    if snake.head.distance(food)<15:
        food.refresh()
        score_board.increase_score()
        snake.increase_length()

    # detect wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor() >280 or snake.head.ycor()<-280:
        is_game_on=False
        score_board.game_over()

    # detect snake collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            is_game_on=False
            score_board.game_over()














screen.exitonclick()

