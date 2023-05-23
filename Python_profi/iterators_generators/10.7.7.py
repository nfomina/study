def txt_to_dict():
    with open('planets.txt', 'r', encoding='utf-8') as file:
        lines = {}
        for i, line in enumerate(file):
            if i % 5 == 0 and i != 0:
                yield lines
                lines = {}
            if line.strip():
                name, value = line.strip().split(' = ')
                lines[name] = value
    if lines:
        yield lines


planets = txt_to_dict()

print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))

planets = txt_to_dict()

print(*planets)

# from teacher with love
# def planet_features(file):
#     features = {}
#     for _ in range(4):
#         key, value = file.readline().strip().split(' = ')
#         features[key] = value
#     return features
#
# def txt_to_dict():
#     with open('planets.txt') as file:
#         line = 'lets some yield'
#         while line:
#             yield planet_features(file)
#             line = file.readline()
