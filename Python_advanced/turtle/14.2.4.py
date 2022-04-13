import turtle


turtle.penup()
turtle.shape('turtle')
turtle.stamp()
for _ in range(10):
  turtle.forward(50)
  turtle.stamp()
  turtle.backward(50)
  turtle.left(360 / 10)