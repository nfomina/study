import turtle

n = int(input())

turtle.shape('triangle')
turtle.dot(15)


def line(side):
    turtle.forward(side)
    turtle.stamp()
    turtle.backward(side)


for i in range(n):
    turtle.setheading(i * (360 / n))
    line(50)