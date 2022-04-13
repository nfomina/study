import turtle

def triangle(side):
  for _ in range(3):
    turtle.forward(side)
    turtle.left(120)

side = int(input())

triangle(side)