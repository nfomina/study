import sys

data = list(map(str.strip, sys.stdin))

for item in data:
    print(item[::-1])


# one line
# [sys.stdout.write(line.strip('\n')[::-1] + '\n') for line in sys.stdin]