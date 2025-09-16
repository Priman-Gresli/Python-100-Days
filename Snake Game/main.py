import time
from turtle import Turtle, Screen
from Snake import Snake


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

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()













screen.exitonclick()

