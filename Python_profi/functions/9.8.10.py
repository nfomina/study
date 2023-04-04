import functools


def add_attrs(**attrs):
    def decorator(func):
        for attr in attrs:
            func.__dict__[attr] = attrs[attr]

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator


@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)

# short and smart
# def add_attrs(**kwargs):
#     return lambda fun: [fun.__dict__.update(kwargs), fun][1]
