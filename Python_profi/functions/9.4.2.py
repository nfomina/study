old_print = print

def new_print(*args, sep=' ', end='\n'):
    new_args = []
    for arg in args:
        if isinstance(arg, str):
            new_args.append(arg.upper())
        else:
            new_args.append(arg)
    sep = sep.upper()
    end = end.upper()
    old_print(*new_args, sep=sep, end=end)


print = new_print
print('beegeek', [1, 2, 3], 4)
print('bee', 'geek', sep=' and ', end=' wow')
words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')


#  short
# old_print = print
#
# def print(*args, sep=' ', end='\n'):
#     uppered = (arg.upper() if isinstance(arg, str) else arg for arg in args)
#     old_print(*uppered, sep=sep.upper(), end=end.upper())
