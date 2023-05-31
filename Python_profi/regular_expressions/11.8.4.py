from re import sub

print(sub(r'(\w)(\w)(\w*)', r'\2\1\3', input().strip()))
