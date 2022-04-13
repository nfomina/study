import turtle


def print_figure(side):
    for i in range(4):
        turtle.forward(side)
        turtle.left(120 - 60 * (i % 2))


print_figure(int(input()))