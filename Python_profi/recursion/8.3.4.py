def range_sum(numbers, start, end):
    if start > end:
        return 0
    else:
        return numbers[end] + range_sum(numbers, start, end-1)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0))
