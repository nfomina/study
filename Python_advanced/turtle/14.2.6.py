from turtle import *


shape('turtle')
Screen().bgcolor('light green')
for i in range(1, 61):
    stamp()
    penup()
    forward(i)
    pendown()
    right(20)