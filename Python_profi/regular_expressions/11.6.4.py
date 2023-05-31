from re import search
import sys

bee = 0
geek = 0
for line in sys.stdin:
    if search(r'.*(bee).*(bee).*', line.strip()):
        bee += 1
    if search(r'\bgeek\b', line.strip()):
        geek += 1
print(bee)
print(geek)
