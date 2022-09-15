import sys

data = list(map(str.strip, sys.stdin))
count = 0
for item in data:
    if item.startswith('#'):
        count += 1
print(count)


# in one line
# from sys import stdin
#
# print(sum(1 for row in stdin if row.lstrip().startswith('#')))
