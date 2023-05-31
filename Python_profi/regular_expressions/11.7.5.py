import re

needle, haystack = input(), input()
n = fr'\b{needle}\b|\b{needle.replace("our", "or")}\b'

print(len(re.findall(n, haystack, re.I)))
