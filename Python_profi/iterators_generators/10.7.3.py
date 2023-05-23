def filter_names(names, ignore_char, max_names):
    for item in names:
        if item[0].lower() not in ignore_char.lower() and item.isalpha():
            max_names -= 1
            if max_names >= 0:
                yield item



data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))

data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123', 'Geo000000r']

print(*filter_names(data, 'A', 100))

#  with generators
# def filter_names(names, ignore_char, max_names):
#     ignore_char = ignore_char.lower()
#     filtred_char = (name for name in names if not name.lower().startswith(ignore_char))
#     filtred_dig = (name for name in filtred_char if name.isalpha())
#     return (name for idx, name in enumerate(filtred_dig) if idx < max_names)
