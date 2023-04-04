# все отсортированные строчные буквы стоят перед заглавными буквами
# все отсортированные заглавные буквы стоят перед цифрами
# все отсортированные нечетные цифры стоят перед отсортированными четными

symbols = input()
small_letter = []
big_letter = []
even_numbers = []
odd_numbers = []
for item in sorted(symbols):
    if item in '0123456789':
        if item in '13579':
            odd_numbers.append(item)
        else:
            even_numbers.append(item)
    elif ord(item)>=97 and ord(item)<=122:
        small_letter.append(item)
    else:
        big_letter.append(item)

print(''.join(small_letter), ''.join(big_letter), ''.join(odd_numbers), ''.join(even_numbers),  sep='')

# smart
# def comparator(char):
#     if char.isalpha():
#         return 0, char.isupper(), char
#     digit = int(char)
#     return 1, digit % 2 == 0, digit
#
# string = input()
#
# print(''.join(sorted(string, key=comparator)))
