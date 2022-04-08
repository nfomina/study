string = input().split()

new_string = []
for i, item in enumerate(string):
    if new_string:
        if new_string[-1][0] == item:
            new_string[-1].extend(item)
        else:
            new_string.append([item])
    else:
        new_string.append([item])
print(new_string)