import functools


def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if end < len(res):
                return res[0:start] + char*(end-start) + res[end:]
            else:
                return res[0:start] + char * (len(res)-start)
        return wrapper
    return decorator


@strip_range(3, 5)
def beegeek():
    return 'beegeek'


print(beegeek())


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'


print(beegeek())


@strip_range(20, 30)
def beegeek():
    return 'beegeek'


print(beegeek())

# so smart
# import functools
#
# def strip_range(start: int, end: int, char: str = '.'):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res[:start] + char*(min(end, len(res))-start) + res[end:]
#         return wrapper
#     return decorator
