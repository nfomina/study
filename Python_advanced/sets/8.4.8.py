str1 = input()
str2 = input()

if set(str1) == set(str2):
    print('YES')
else:
    print('NO')

# beautiful
# print(['NO', 'YES'][set(input()) == set(input())])