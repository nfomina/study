from turtle import *

hideturtle()
Screen().bgcolor('blue')
dot(200, 'orange')
shadow = Turtle()
shadow.hideturtle()
shadow.tracer(6, 25)
shadow.up()
for i in range(200, -201, -1):
  shadow.goto(i, 0)
  shadow.clear()
  shadow.dot(200, 'blue')