import turtle

def square(side):
  for _ in range(4):
    turtle.forward(side)
    turtle.left(90)

side = int(input())
for i in range(3):
  turtle.setheading((i+1)*20)
  square(side)