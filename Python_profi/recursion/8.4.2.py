def linear(nested_lists):
    lists = []
    for elem in nested_lists:
        if isinstance(elem, int):
            lists.append(elem)
        else:
            lists.extend(linear(elem))
    return lists


my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))

my_list = [10, 20, 30, 40, 50]

print(linear(my_list))
