import turtle

turtle.shape('turtle')

def forward():
    turtle.setheading(90)
    turtle.forward(50)

def left():
    turtle.setheading(180)
    turtle.forward(50)

def right():
    turtle.setheading(-90)
    turtle.forward(50)

def down():
    turtle.setheading(0)
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.onkey(forward, 'w')
turtle.onkey(left, 'a')
turtle.onkey(right, 's')
turtle.onkey(down, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen() 
