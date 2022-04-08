n, m = [int(a) for a in input().split()]

current_el = 1
for i in range(n):
    if i%2 == 0:
        line = [a for a in range(current_el, current_el+m)]
    else:
        line = [a for a in range(current_el+m-1, current_el-1, -1)]
    print(*line)
    current_el += m

#
# trick
#
# n, m = map(int, input().split())
# a = [[str(j + i*m).ljust(3) for j in range(1, m+1)][::(-1)**i] for i in range(n)]
# for el in a:
#   print(*el)