import turtle
turtle.shape('turtle')
count =0
while(count<=5):
	turtle.penup()
	turtle.goto(count*100,500)
	turtle.pendown()
	turtle.goto(count*100,0)
	count=count+1

	
count =0
while(count <=5):
	turtle.penup()
	turtle.goto(0,count*100)
	turtle.pendown()
	turtle.goto(500,count*100)
	count=count+1
	
turtle.reset()
import random
count =0
while (count<=10):
	turtle.setheading(random.randint(0,360))
	turtle.forward(random.randint(100,200))
	turtle.stamp()
	count = count+1

for x,y,r in [(200,200,50),(-200,-200,30),(100,100,50)]:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(r)
    turtle.write((x,y))



	
