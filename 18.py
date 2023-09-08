from turtle import Turtle, Screen 
import random


is_race_on = False

screen = Screen()
# tim = Turtle("turtle")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="bet", prompt="who win:")
colors=["green","red","black","yellow","blue"]
y_position =[-70, -40, -10, 20, 50, 80]
all_turtle = []


for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on= True
    
while is_race_on:
    
    
    for turtle in all_turtle:
      randon_distance = random.randint(0, 10)    
      turtle.forward(randon_distance)

screen.exitonclick()


















































# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color=(r, g, b)
#     return color

# tim.speed("fastest")
# def draw_spirograpgh(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.circle(100)
#         tim.color(random_color())    
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograpgh(5)    
    
# screen = t.Screen()
# screen.exitonclick()    





# --------------------------------------------------------


# tim = Turtle()
# # tim.shape("turtle")
# # tim.color("green")
# colors = ["blue", "pink", "black", "red", "yellow","deepskyblue", "green"]

# def draw_shape(num_sides):
#     angle =360/num_sides
#     for _ in range(num_sides):
        
#         tim.forward(100)
#         tim.right(angle)


# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# Crated the shapdes in different colors______________________------------------___________________----------------------------------

# for r in range(4):
#     for _ in range(15):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
#     tim.forward(100)
#     tim.left(90)
     
#     # for _ in range(15):
#     #     tim.forward(10)
#     #     tim.penup()
#     #     tim.forward(10)
#     #     tim.pendown()
#     # tim.left(90)


