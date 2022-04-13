import turtle


def snowflake(side):
    for g in range(10):
        turtle.setheading(g * 36)
        for i in range(4):
            degree = 120 if i % 2 else 60
            turtle.forward(side)
            turtle.left(degree)


snowflake(int(input()))