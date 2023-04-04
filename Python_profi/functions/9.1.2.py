def convert(number):
    return format(number, 'b'), format(number, 'o'), format(number, 'X')


print(convert(15))
print(convert(-24))
print(convert(1))

# short
# def convert(n):
#     return f'{n:b}', f'{n:o}', f'{n:X}'
