
numbers = [int(i) for i in input().split()]

numbers.sort(key= lambda x: sum([int(i) for i in str(x)]))

print(*numbers)