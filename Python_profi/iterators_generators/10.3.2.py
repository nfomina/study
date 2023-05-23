def is_iterable(obj):
    return True if '__iter__' in dir(obj) else False


# TEST_1:
print(is_iterable(18731))

# TEST_2:
print(is_iterable('18731'))

# TEST_3:
objects = [(1, 13), 7.0004, [1, 2, 3]]

for obj in objects:
    print(is_iterable(obj))

# TEST_4:
for element in [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]:
    print(element, 'iterable: ', is_iterable(element))

# shorter
# def is_iterable(obj):
#     return '__iter__' in dir(obj)
