import turtle

def triangle(side):
  for _ in range(3):
    turtle.forward(side)
    turtle.left(120)

side = 70

triangle(side)
print(turtle.pos())

turtle.penup()
turtle.goto(side, side//2)
turtle.left(180)
turtle.pendown()
triangle(side)