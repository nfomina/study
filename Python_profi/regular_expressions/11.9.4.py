import re


a, b = map(int, input().split())
print(sum([int(num) for num in re.findall(r'\d*', input()[a:b]) if num.isdigit()]))

# with compile
# import re
#
# pos, endpos = map(int, input().split())
# text = input()
# pattern_obj = re.compile(r"\d+")
# print(sum(map(int, pattern_obj.findall(text, pos, endpos))))