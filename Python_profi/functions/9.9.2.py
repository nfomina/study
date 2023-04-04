from functools import lru_cache
import sys


@lru_cache(typed=False)
def sort_letter(word):
    return ''.join(sorted(word))


for line in sys.stdin:
    print(sort_letter(line.strip()))
