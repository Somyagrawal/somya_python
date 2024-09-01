from turtle import Turtle,Screen

wn= Screen()
somya=Turtle()

somya.shape("turtle")

for _ in range(4):
    somya.forward(200)
    somya.left(90)



for _ in range(4):
    somya.forward(150)
    somya.left(90)




for _ in range(4):
    somya.forward(100)
    somya.left(90)

    
def square(side_lenght):
    for _ in range(4):
        somya.forward(side_lenght)
        somya.left(90)


square(100)




wn.exitonclick()
