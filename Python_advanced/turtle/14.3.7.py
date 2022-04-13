import turtle, random

turtle.speed()
turtle.penup()


def star():
    size = random.randint(15, 40)
    turtle.left(random.randint(0, 360))

    color = tuple(random.randint(0, 255) for _ in '123')
    turtle.fillcolor(color)

    y = random.randint(-150, 150)
    x = random.randint(-150, 150)
    turtle.goto(x, y)

    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.left(144)
    turtle.end_fill()


for _ in range(random.randint(10, 50)):
    star()