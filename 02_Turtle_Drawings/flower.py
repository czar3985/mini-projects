import turtle

def draw_petal(turtleElement):
    sidesDrawn = 0
    bigAngleFlag = 0
    while (sidesDrawn < 4):
        turtleElement.forward(50)
        if (bigAngleFlag == 1):
            turtleElement.right(120)
            bigAngleFlag = 0
        else: 
            turtleElement.right(60)
            bigAngleFlag = 1
        sidesDrawn = sidesDrawn + 1

def draw_flower():
    flower = turtle.Turtle()

    #draw flower petals
    flower.penup()
    flower.pendown()
    flower.color("red")
    for i in range(1,73):
        draw_petal(flower)
        flower.right(5)

    #draw stem
    flower.penup()
    flower.goto(0,-75)
    flower.pendown()
    flower.color("brown")
    flower.right(90)
    flower.forward(75)
    
def draw_art():
    window = turtle.Screen()

    draw_flower()

    window.exitonclick()

draw_art()
