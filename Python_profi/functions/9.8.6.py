import functools


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator


# TEST_5:
@repeat(10)
def add(a, b):
    '''sum of two numbers'''
    return a + b


print(add.__name__)
print(add.__doc__)
print(add(10, b=20))

# TEST_6:
counter = 0


@repeat(11)
def change_counter():
    global counter
    counter += 1
    print(counter)


print(change_counter.__name__)
print(change_counter.__doc__)
change_counter()
print(counter)


# TEST_7:
@repeat(5)
def say(word):
    print(word)


say(word="Hey!")
