import turtle

def rectangle(width, height):
  for _ in range(4):
    turtle.pensize(7)
    turtle.dot()
    turtle.pensize(1)
    turtle.forward(width)
    turtle.left(90)
    width, height = height, width

width = int(input())
height = int(input())
rectangle(width, height)