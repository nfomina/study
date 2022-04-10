mapping = {'G': 'C',
           'C': 'G',
           'T': 'A',
           'A': 'U'}

for letter in input():
    print(mapping.get(letter), end='')
