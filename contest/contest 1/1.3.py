string_1 = input()
string_2 = input()

for element in string_1:
    string_2 = string_2.replace(element, '', 1)

print(string_2)