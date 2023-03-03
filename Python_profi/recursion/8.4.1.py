def recursive_sum(nested_lists, all_numbers=[]):
    if type(nested_lists) == int:
        all_numbers.append(nested_lists)
    if type(nested_lists) == list:
        for i in nested_lists:
            recursive_sum(i)
    return sum(all_numbers)


my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))

my_list = []

print(recursive_sum(my_list))

# elegant
# def recursive_sum(nested_lists):
#     total = 0
#     for elem in nested_lists:
#         if isinstance(elem, list):
#             total += recursive_sum(elem)
#         else:
#             total += elem
#     return total