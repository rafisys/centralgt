# step1------------------------------Set screen and snake
# step2------------------------------make sure snake runs
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)
starting_position = [(0,0),(-20, 0),(-40,0)]

segments= []

for position in starting_position:
    New_segment = Turtle("square")
    New_segment.color("white")
    New_segment.penup()
    New_segment.goto(position)
    segments.append(New_segment)

screen.update()

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    
    for seg_num in range(start=  ,)
   





screen.exitonclick()










