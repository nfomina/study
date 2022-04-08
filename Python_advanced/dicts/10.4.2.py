word1 = input()
word2 = input()

dict1 = {}
for letter in word1:
    if letter in dict1:
        dict1[letter] = dict1.get(letter, 0) + 1
    else:
        dict1[letter] = 0

dict2 = {}
for letter in word2:
    if letter in dict2:
        dict2[letter] = dict2.get(letter, 0) + 1
    else:
        dict2[letter] = 0

if dict1 == dict2:
    print('YES')
else:
    print('NO')

# smart
# d = {}
# for c in input().lower():
#     d[c] = d.get(c, 0) + 1
# for c in input().lower():
#     d[c] = d.get(c, 0) - 1
#
# print(('NO', 'YES')[set(d.values()) == {0}])