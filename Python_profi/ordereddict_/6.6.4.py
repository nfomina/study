from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    temp = sorted(ordered_dict.items(), key=lambda item: item[int(by_values)])
    ordered_dict.clear()
    ordered_dict.update(temp)


data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(*data.items())

data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)

# shortly

# def custom_sort(orderd_dict, by_values = False):
#     for key, value in sorted(orderd_dict.items(), key=lambda x: x[by_values]):
#         orderd_dict.move_to_end(key)