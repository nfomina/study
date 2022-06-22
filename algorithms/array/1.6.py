A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

for i, item in enumerate(B):
    if item == 0:
        A[i] = -A[i]

def fish(A):
    ans = []
    for new in A:
        while ans and new < 0 < ans[-1]:
            if ans[-1] < -new:
                ans.pop()
                continue
            elif ans[-1] == -new:
                ans.pop()
            break
        else:
            ans.append(new)
    return len(ans)

print(fish(A))