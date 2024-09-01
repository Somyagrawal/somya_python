from turtle import Turtle,Screen

wn= Screen()
somya=Turtle()

somya.shape("turtle")

def triangle(side_lenght):
    for _ in range(3):
        somya.forward(side_lenght)
        somya.left(120)
triangle(100)

wn.exitonclick()
