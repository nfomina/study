def triangle(h):
    if h:
        triangle(h - 1)
        print('*' * h)

triangle(3)