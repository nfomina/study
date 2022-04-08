letters = input().split()
n = int(input())

sublists = []
c = 0
for i in letters:
    sublists.append(letters[c::n])
    c+=1
    if c==n:
        break
print(sublists)

