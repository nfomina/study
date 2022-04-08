str1, str2, str3 = input().split()

print(['NO', 'YES'][set(str1) == set(str2) and set(str2) == set(str3)])