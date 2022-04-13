from turtle import *
import random


def draw_snow(size, x, y):
    goto(x, y)
    pendown()
    r, g, b = random.randrange(217), random.randrange(166), random.randrange(76, 181)
    pencolor(r, g, b)
    pensize(random.choice([1, 2, 3, 4]))
    elem = size / 4
    for _ in range(8):
        forward(size)
        backward(elem)
        for _ in range(3):
            left(45)
            forward(elem)
            backward(elem)
            right(90)
            forward(elem)
            backward(elem)
            left(45)
            backward(elem)
        left(45)
    penup()


def snowfall():
    speed()
    Screen().bgcolor('cyan')
    penup()
    free_coords = 400 * 400
    set_coords = []
    while free_coords > 1000:
        x, y, size = random.randrange(-200, 201), random.randrange(-200, 201), random.randrange(10, 51)
        for coord in set_coords:
            # abs(coord[0] - x + coord[2]) <= size and abs(coord[1] - y + coord[2]) <= size:
            if abs(x - coord['x']) - coord['size'] <= size and abs(y - coord['y']) - coord['size'] <= size:
                break
        else:
            draw_snow(size, x, y)
            set_coords.append({'x': x, 'y': y, 'size': size})
            free_coords -= size ** 2


snowfall()