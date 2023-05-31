import re

print(re.sub(r'\b(\w+)(?:\W+\1\b)+', r'\1', input()))
