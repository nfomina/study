n = int(input())
matrix = []
sum = 0
for i in range(n):
    temp = [int(num) for num in input().split()]
    sum += temp[i]

print(sum)
