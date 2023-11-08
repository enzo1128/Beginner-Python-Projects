from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

game = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")

while game:
    screen.update()
    sleep(0.1)
    snake.move()
    #Detect if snake eats food
    if snake.all_segs[0].distance(food) < 15:
        food.refresh()
        board.point()
        snake.add_seg(snake.all_segs[-1].pos())
        snake.grow()
    #collide with wall?
    if snake.all_segs[0].xcor() > 280 or snake.all_segs[0].xcor() < -280 or snake.all_segs[0].ycor() > 240 or snake.all_segs[0].ycor() < -280:
        game = False
        board.game_over()
    for seg in snake.all_segs[1:]:
        if snake.all_segs[0].distance(seg) < 10:
            game = False
            board.game_over()
screen.exitonclick()
