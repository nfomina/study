

def triangle(h):
    def rec(n):
        if n > 0:
            print(f'{"*"*n}')
            rec(n - 1)

    rec(h)


triangle(7)

# best
# def triangle(h):
#     if h:
#         print('*' * h)
#         triangle(h - 1)
