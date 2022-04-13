import turtle


def line(side):
    turtle.forward(side)
    turtle.backward(side)


side = int(input())

for i in range(12):
    turtle.setheading(i * 30)
    line(side)