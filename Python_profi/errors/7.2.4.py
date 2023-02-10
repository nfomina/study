import sys

sum = 0
lines = 0
for line in sys.stdin:
    try:
        sum += float(line)
    except:
        lines += 1

print(int(sum) if int(sum) == float(sum) else sum)
print(lines)

