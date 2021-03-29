from turtle import Screen
from snake import Snake
from food import Food
from score_board import score
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.tracer(0)
s=Snake()
f=Food()
sc=score()
screen.listen()
screen.onkey(fun=s.Left,key="Left")
screen.onkey(fun=s.Up,key="Up")
screen.onkey(fun=s.Down,key="Down")
screen.onkey(fun=s.Right,key="Right")
option=1
while option:
    screen.update()
    time.sleep(0.1)
    s.move()
    if s.head.distance(f)<15:
        s.extend()
        f.draw()
        sc.w()
    if s.head.xcor()>=280 or s.head.ycor()>=280 or s.head.xcor()<=-280 or s.head.ycor()<=-280:
        print("Imma out")
        sc.w()
        sc.high_score()
        sc.reset()
        s.reset()
    for segments in s.t:
        if segments==s.head:
            pass
        elif s.head.distance(segments)<15:
         sc.w()
         sc.high_score()
         sc.reset()
         s.reset()
         print("Game over")



screen.exitonclick()
