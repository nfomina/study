def flatten(nested_list):
    lists = []
    for elem in nested_list:
        if isinstance(elem, int):
            lists.append(elem)
        else:
            lists.extend(flatten(elem))
    yield from lists


generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)

# smart
# def flatten(nested_list):
#     for i in nested_list:
#         yield from flatten(i) if isinstance(i, list) else [i]
