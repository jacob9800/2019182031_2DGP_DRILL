import turtle

turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()

count = 4

while count != 0:
    turtle.forward(500)
    turtle.left(90)
    count = count -1

scount = 2

while scount != 0:
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    scount = scount -1

turtle.exitonclick()    


