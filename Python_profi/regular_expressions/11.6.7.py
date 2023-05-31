from re import search, I
import sys


times = 0
for line in sys.stdin:
    if search(r'beegeek', line, I):
        times += 1

print(times)

# one line
# print(sum(bool(re.search(r'beegeek', s, re.I)) for s in sys.stdin))
