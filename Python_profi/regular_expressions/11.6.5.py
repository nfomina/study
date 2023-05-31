from re import search, fullmatch
import sys


score = 0
for line in sys.stdin:
    if fullmatch(r'beegeek.*beegeek', line.strip()):
        score += 3
    elif fullmatch(r'beegeek.*', line.strip()) or fullmatch(r'.*beegeek', line.strip()):
        score += 2
    elif search(r'.*beegeek.*', line.strip()):
        score += 1

print(score)
