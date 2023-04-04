def upper(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for item in args:
            if isinstance(item, str):
                item = item.upper()
            new_args.append(item)
        for key in kwargs:
            if isinstance(kwargs[key], str):
                kwargs[key] = kwargs[key].upper()
        func(*tuple(new_args), **kwargs)
    return wrapper


print = upper(print)


print('hi', 'there', end='!')

print('are you in trouble?')

print(111, 222, 333, sep='xxx')


# def new_print(func):
#     def wrapper(*args, sep=' ', end='\n'):
#         func(sep.join(map(str, args)).upper(), end = end.upper())
#     return wrapper
#
# print = new_print(print)
