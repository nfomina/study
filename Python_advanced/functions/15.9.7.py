print('YES' if all([(any(map(lambda x: x[1] == '5', [input().split() for j in range(int(input()))]))) for _ in range(int(input()))]) else 'NO')

# unbelievable
# print(('NO', 'YES')[all([any(['5' in input() for _ in 'k'*int(input())]) for _ in 'n'*int(input())])])