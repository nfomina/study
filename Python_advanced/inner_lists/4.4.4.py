n = int(input())
matrix = []

for i in range(n):
    temp = [int(num) for num in input().split()]
    average = sum(temp)/len(temp)
    count = 0
    for item in temp:
        if item > average:
            count+=1
    print(count)

