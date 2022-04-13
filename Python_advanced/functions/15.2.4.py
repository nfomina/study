
def greet(name, *args):
    if args:
        return f'Hello, {name} and {" and ".join([arg for arg in args])}!'
    else:
        return f'Hello, {name}!'



print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))


# Hello, Timur!
# Hello, Timur and Roman!
# Hello, Timur and Roman and Ruslan!

# short
# def greet(name, *args):
#     return f'Hello, {" and ".join((name,) + args)}!'