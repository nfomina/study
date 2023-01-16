from collections import Counter

import sys

data = []
for line in sys.stdin:
    name, score = line.split()
    data.append([name, int(score)])

print(sorted(data, key=lambda x: x[1])[1][0])

