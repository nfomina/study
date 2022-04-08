string = input().split()
for i in range(0, (len(string) if len(string) % 2 == 0 else len(string)-1), 2):
    string[i], string[i+1] = string[i+1], string[i]
print(' '.join(string))
