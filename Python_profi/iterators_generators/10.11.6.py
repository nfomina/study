from itertools import groupby


def ranges(numbers):
    start = numbers[0]
    end = start
    dif = numbers[0]
    res = []
    for index, value in enumerate(groupby(numbers)):
        if value[0] - index <= dif:
            end = value[0]
        else:
            res.append((start, end))
            start = value[0]
            dif = value[0] - index
            end = value[0]
    res.append((start, numbers[-1]))
    return res


numbers = [1, 2, 3, 4, 7, 8, 10]
print(ranges(numbers))

numbers = [1, 3, 5, 7]
print(ranges(numbers))

numbers = [1, 2, 3, 4, 5, 6, 7]
print(ranges(numbers))

numbers = list(range(5, 101))
print(ranges(numbers))

numbers = list(range(10, 21)) + [30] + list(range(35, 101)) + list(range(1000, 1001))
print(ranges(numbers))

# from teacher
# from itertools import groupby
#
# def ranges(numbers):
#     result = []
#     for _, group in groupby(numbers, key=lambda n: n - numbers.index(n)):
#         group = tuple(group)
#         group = group[0], group[-1]
#         result.append(group)
#     return result
