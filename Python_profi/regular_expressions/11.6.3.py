from re import fullmatch
import sys


for line in sys.stdin:
    match = fullmatch(r'(\w+)\1', line.strip())
    if match:
        print(line.strip())
