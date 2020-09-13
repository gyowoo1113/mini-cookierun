import turtle
def S(x,y):
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(y)

def move_to(a,b):
    turtle.penup()
    x,y = turtle.pos()
    turtle.goto(x+a,y+b)
    turtle.pendown()

turtle.speed(10)
move_to(-200,200)

turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(100)
turtle.left(180)
turtle.forward(50)
turtle.right(90)
turtle.forward(75)

move_to(100,0)

turtle.left(180)
turtle.forward(25)
turtle.left(90)
turtle.forward(50)
turtle.left(180)
turtle.forward(75)
turtle.right(90)
turtle.forward(25)
turtle.left(180)
turtle.forward(25)
turtle.right(90)
turtle.forward(25)
turtle.penup()

move_to(0,-50)
turtle.right(90)
S(120,35)

move_to(160,50)

turtle.right(90)
turtle.forward(100)
turtle.left(90)

move_to(-5,25)

turtle.left(45)
turtle.pendown()
turtle.forward(65)
turtle.left(90)
turtle.forward(65)
turtle.left(45)

move_to(7,-75)
turtle.circle(40)

move_to(125,25)
turtle.left(90)
turtle.pendown()
turtle.forward(100)

move_to(0,-50)
turtle.right(180)
S(100,25)

move_to(80,80)
turtle.circle(30)

turtle.exitonclick()






