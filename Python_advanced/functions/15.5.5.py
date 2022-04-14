def add3(x):
    return x + 3


def mul7(x):
    return x * 7


def func_apply(func, value):
    results = []
    for item in value:
        results.append(func(item))
    return results


print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))


# short
# def func_apply(func, arr):
#     return [func(x) for x in arr]