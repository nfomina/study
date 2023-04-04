import functools


def ignore_exception(*exceptions):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as ex:
                if type(ex).__name__ in list(map(lambda a: a.__name__, exceptions)):
                    print(f'Исключение {type(ex).__name__} обработано')
                else:
                    raise ex
        return wrapper
    return decorator



@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x


f(0)

min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as e:
    print(type(e))


# without bicycle
# import functools
#
# def ignore_exception(*exceptions):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             except exceptions as e:
#                 print(f"Исключение {type(e).__name__} обработано")
#         return wrapper
#     return decorator

