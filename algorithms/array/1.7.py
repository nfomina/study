A = [int(i) for i in input().split()]

new_A = []

for i, item in enumerate(A):
    flag = 0
    for el in A[i:]:
        if el > A[i]:
            new_A.append(el)
            flag = 1
            break
    if flag == 0:
        new_A.append(-1)
print(*new_A)

