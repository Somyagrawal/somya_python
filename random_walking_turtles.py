import random
from turtle import Turtle,Screen

scrn=Screen()
scrn.setup(600,600)
scrn.bgcolor("black")

colors = ["cyan","yellow","green","red"]

all_turtles = []
for i in range(4):
    tomjerry=Turtle()
    tomjerry.shape("turtle")
    tomjerry.color(colors[i])
    all_turtles.append(tomjerry)
    
while True:
    for cartoon in all_turtles:
        random_move = random.randint(10,100)
        random_turn = random.randint(0,360)

        cartoon.setheading(random_turn)
        cartoon.forward(random_move)


        if cartoon.xcor() >280:
            cartoon.setheading(180)
            cartoon.forward(100)


        if cartoon.ycor() >280:
            cartoon.setheading(270)
            cartoon.forward(100)


        if cartoon.xcor() <-280:
            cartoon.setheading(0)
            cartoon.forward(100)

        if tomjerry.ycor() <-280:
            tomjerry.setheading(90)
            tomjerry.forward(100)
            

