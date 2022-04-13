import turtle
from math import cos,sin,pi


turtle.hideturtle()
a = 2*pi
t = 0
turtle.fillcolor("red")

turtle.begin_fill()
while t < a:
  x = 128 * sin(t)**3
  y = 8 * (13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t)-5)
  turtle.goto(x,y)
  t += 0.01
turtle.end_fill()