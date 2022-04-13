import turtle


def olympic_rings(r=int(input('Radius of ring: '))):
    turtle.speed(10)
    turtle.pensize(r / 15)
    d = {
        'black': (0, 0),
        'cyan': (0 - 2 * r, 0),
        'red': (0 + 2 * r, 0),
        'yellow': (0 - r, 0 - r * 1.3),
        'chartreuse': (0 + r, 0 - r * 1.3),
    }

    for k, v in d.items():
        turtle.up()
        turtle.goto(v)
        turtle.pencolor(k)
        turtle.down()
        turtle.circle(r)


olympic_rings()