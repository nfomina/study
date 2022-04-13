import turtle

def star(side):
  for i in range(5):
    turtle.forward(side)
    turtle.left(144)

turtle.setheading(324)
star(int(input()))