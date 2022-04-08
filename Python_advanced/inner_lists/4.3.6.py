def chunked(string, n):
    return [string[i:i+n] for i in range(0, len(string), n)]

print(chunked(input().split(), int(input())))