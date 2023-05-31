from re import fullmatch
import sys


for line in sys.stdin:
    print(bool((fullmatch('_\d+[a-zA-Z]*_?\n?', line))))
