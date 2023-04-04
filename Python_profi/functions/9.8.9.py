import functools


def takes(*datatypes):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            all_args = list(args) + list(kwargs.values())
            for arg in all_args:
                if type(arg) not in datatypes:
                    raise TypeError
            res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator


@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))

@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times

try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))


@takes(str)
def beegeek(word, repeat):
    return word * repeat


try:
    print(beegeek('beegeek', repeat=2))
except TypeError as e:
    print(type(e))
