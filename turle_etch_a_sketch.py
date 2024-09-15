from turtle import Turtle,Screen

wn=Screen()

somya=Turtle()
somya.shape("turtle")

def somya_up():
    somya.setheading(90)
    somya.forward(50)
def somya_down():
    somya.setheading(270)
    somya.forward(50)
def somya_right():
    somya.setheading(0)
    somya.forward(50)
def somya_left():
    somya.setheading(180)
    somya.forward(50)
def pen_up():
    somya.penup()
def pen_down():
    somya.pendown()
    


wn.listen()
wn.onkeypress(somya_up, "Up")
wn.onkeypress(somya_down, "Down")
wn.onkeypress(somya_right, "Right")
wn.onkeypress(somya_left, "Left")
wn.onkeypress(pen_up, "w")
wn.onkeyrelease(pen_down,"w")



