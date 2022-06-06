from itertools import product

n = int(input())


def check(my_string):
    brackets = ['()', '[]']
    while any(x in my_string for x in brackets):
        for br in brackets:
            my_string = my_string.replace(br, '')
    return not my_string


brackets = ['(', ')', '[', ']']

all_combinations = product(brackets, repeat=n)

for line in list(all_combinations):
    line_short = ''.join(line)
    if check(line_short):
        print(line_short)

