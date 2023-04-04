def takes_positive(func):
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        for arg in all_args:
            if isinstance(arg, int) is False:
                raise TypeError
            elif arg <= 0:
                raise ValueError
        return func(*args, **kwargs)
    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))


# TEST_9:
@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=4))


# TEST_10:
@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
except Exception as err:
    print(type(err))


# TEST_11:
@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep='40'))
except Exception as err:
    print(type(err))


# TEST_12:
@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(11, 20.7, 10))
except Exception as err:
    print(type(err))


# TEST_13:
@takes_positive
def power(a, n):
    return a ** n


try:
    print(power(a="3", n="2"))
except Exception as err:
    print(type(err))

# a little beauty
# def takes_positive(func):
#     def wrapper(*args, **kwargs):
#         for i in [*args, *kwargs.values()]:
#             if not type(i) is int:
#                 raise TypeError
#             elif i <= 0:
#                 raise ValueError
#         return func(*args, **kwargs)
#     return wrapper
