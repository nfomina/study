import re

word = input().strip()[0:-2]
word_1 = word + 'se'
word_2 = word + 'ze'
string = input()
reg_exp = f'\W*({word_1})\W*|\W*({word_2})\W*'
res = re.findall(reg_exp, string, re.I | re.M)
print(len(set(res)))

# without bicycle
# import re
#
# needle, haystack = input(), input()
# n = fr'\b{needle[:-2]}[zs]e\b'
#
# print(len(re.findall(n, haystack, re.I)))
