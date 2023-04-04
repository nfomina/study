def sort_priority(values, group):
    numbers_max = max(values)
    group_max = max(group)
    values.sort(key=lambda x: x if x in group else x + group_max + numbers_max)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)
# [2, 3, 5, 7, 1, 4, 6, 8]

numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])

print(numbers)
# [200, 300, 50, 150, 1000, 20000]

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))

print(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# so smart, so easy
# def sort_priority(numbers, group):
#     numbers.sort(key=lambda x: (x not in group, x))

