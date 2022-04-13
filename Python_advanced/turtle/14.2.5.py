import turtle

turtle.Screen().bgcolor('LightBlue')
turtle.penup()
turtle.shape('turtle')
turtle.stamp()
turtle.pensize(3)

for _ in range(12):
  turtle.forward(50)
  turtle.pendown()
  turtle.forward(15)
  turtle.penup()
  turtle.forward(10)
  turtle.stamp()
  turtle.backward(75)
  turtle.left(360 / 12)