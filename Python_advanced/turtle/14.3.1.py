import turtle

turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()

turtle.fillcolor('DeepSkyBlue')
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.left(90)
turtle.end_fill()
turtle.up()
turtle.goto(-65, 50)
turtle.down()
turtle.fillcolor('peru')
turtle.begin_fill()
turtle.left(90)
turtle.left(180)
turtle.forward(130)
for i in range(2):
    turtle.right(240)
    turtle.forward(130)
turtle.end_fill()

turtle.done()