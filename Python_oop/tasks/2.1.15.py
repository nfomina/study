import functools


def recviz(func):
    global counter
    counter = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global counter
        arg = ', '.join([str(repr(a)) for a in args])
        dict_args = ', '.join(f'{k}={repr(v)}' for k, v in kwargs.items())
        if dict_args:
            print(f'{"    "*counter}-> {func.__name__}({arg}, {dict_args})')
        else:
            print(f'{"    "*counter}-> {func.__name__}({arg})')
        counter += 1
        res = func(*args, **kwargs)
        counter -= 1
        print(f'{"    "*counter}<- {repr(res)}')
        return res
    return wrapper


@recviz
def add(a, b):
    return a + b

add(1, b=2)

# -> add(1, b=2)
# <- 3

@recviz
def add(a, b, c, d, e):
    return (a + b + c) * (d + e)

add('a', b='b', c='c', d=3, e=True)

# -> add('a', b='b', c='c', d=3, e=True)
# <- 'abcabcabcabc'

@recviz
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(4)

# -> fib(4)
#     -> fib(3)
#         -> fib(2)
#         <- 1
#         -> fib(1)
#         <- 1
#     <- 2
#     -> fib(2)
#     <- 1
# <- 3

@recviz
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


fact(5)

# -> fact(5)
#     -> fact(4)
#         -> fact(3)
#             -> fact(2)
#                 -> fact(1)
#                     -> fact(0)
#                     <- 1
#                 <- 1
#             <- 2
#         <- 6
#     <- 24
# <- 120
