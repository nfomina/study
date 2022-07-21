

def print_given(*args, **kwargs):
    if args:
        for item in args:
            print(item, type(item))
    if kwargs:
        for item in sorted(kwargs):
            print(item, kwargs[item], type(kwargs[item]))



print_given(1, [1, 2, 3], 'three', two=2)
print_given('apple', 'cherry', 'watermelon')
print_given(b=2, d=4, c=3, a=1)
print_given()
print_given(map, range, filter)
print_given([1, 2, 3, 4], ('a', 'b', 'c', 'd'), name='Timur', age=29, city='Moscow')
print_given({1: 1, 2: 2, 3: 3}, [1, 2, 3, 4], (0, 0), zxc=123, abc=321, asd=987, iop=765)
print(print_given())

# beauty
# def print_given(*args, **kwargs):
#     for arg in args:
#         print(arg, type(arg))
#     for name, value in sorted(kwargs.items()):
#         print(name, value, type(value))