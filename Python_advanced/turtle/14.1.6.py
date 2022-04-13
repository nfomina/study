import turtle


def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)


side = int(input())

for i in range(6):
    hexagon(side)
    turtle.forward(side)
    turtle.right(60)