
result = dict((key, key*key) for d in range(1, 16) for key in range(1, 16))
print(result)

# simple
# result = {i: i**2 for i in range(1, 16)}