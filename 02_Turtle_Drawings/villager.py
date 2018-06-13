import turtle

def draw_villager():
    window = turtle.Screen()
    window.bgcolor("lightyellow")

    squirt = turtle.Turtle()
    squirt.shape("turtle")

    #draw face
    squirt.penup()
    squirt.goto(-50,50)
    squirt.pendown()
    squirt.color("wheat","wheat")
    squirt.begin_fill()
    for i in range (1,5):
        squirt.forward(100)
        squirt.right(90)
    squirt.end_fill()

    #draw unibrow
    squirt.penup()
    squirt.goto(-37.5,25)
    squirt.color("black")
    squirt.pendown()
    squirt.forward(75)

    #draw left eye
    squirt.penup()
    squirt.goto(-37.5,25)
    squirt.color("black","white")
    squirt.pendown()
    squirt.begin_fill()
    for i in range (1,5):
        squirt.forward(25)
        squirt.right(90)
    squirt.end_fill()

    #draw right eye
    squirt.penup()
    squirt.goto(12.5,25)
    squirt.pendown()
    squirt.begin_fill()
    for i in range (1,5):
        squirt.forward(25)
        squirt.right(90)
    squirt.end_fill()

    #draw left pupil
    squirt.color("green")
    squirt.penup()
    squirt.goto(-17.5,25)
    squirt.begin_fill()
    squirt.pendown()
    for i in range (1,3):
        squirt.forward(5)
        squirt.right(90)
        squirt.forward(25)
        squirt.right(90)
    squirt.end_fill()

    #draw right pupil
    squirt.penup()
    squirt.goto(12.5,25)
    squirt.begin_fill()
    squirt.pendown()
    for i in range (1,3):
        squirt.forward(5)
        squirt.right(90)
        squirt.forward(25)
        squirt.right(90)
    squirt.end_fill()

    #draw mouth
    squirt.penup()
    squirt.goto(-25,-20.5)
    squirt.color("saddlebrown","saddlebrown")
    squirt.begin_fill()
    squirt.pendown()
    for i in range (1,3):
        squirt.forward(50)
        squirt.right(90)
        squirt.forward(9)
        squirt.right(90)
    squirt.end_fill()

    #draw nose
    squirt.penup()
    squirt.goto(-12.5,0)
    squirt.color("burlywood","burlywood")
    squirt.begin_fill()
    squirt.pendown()
    for i in range (1,3):
        squirt.forward(25)
        squirt.right(90)
        squirt.forward(50)
        squirt.right(90)
    squirt.end_fill()
    squirt.penup()
    squirt.goto(-200,200)

    window.exitonclick()

draw_villager()
