n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(t) for t in input()])

def find_way(matrix, n):
    m = len(matrix)
    memo = [[0 for j in range(n)] for i in range(m)]
    memo[0][0] = matrix[0][0]
    for i in range(1, m):
        if matrix[i][0] == 0:
            break
        else:
            memo[i][0] = memo[i - 1][0] + matrix[i][0]
    for j in range(1, n):
        if matrix[0][j] == 0:
            break
        else:
            memo[0][j] = memo[0][j - 1] + matrix[0][j]
    for i in range(1, m):
        for j in range(1, n):
            if memo[i - 1][j] != 0 and memo[i][j - 1] != 0 and matrix[i][j] != 0:
                memo[i][j] = min(memo[i - 1][j], memo[i][j - 1]) + matrix[i][j]
            elif memo[i - 1][j] == 0 and matrix[i][j] != 0 and memo[i][j - 1] != 0:
                memo[i][j] = memo[i][j - 1] + matrix[i][j]
            elif memo[i][j - 1] == 0 and matrix[i][j] != 0 and memo[i - 1][j] != 0:
                memo[i][j] = memo[i - 1][j] + matrix[i][j]
            else:
                memo[i][j] = 0
    return memo

def draw_way(ways, n):
    i = n-1
    j = n-1
    flag = 1
    ways[i][j] = '#'
    while i > 0 or j > 0:
        if ways[i-1][j] != 0 and ways[i][j-1] != 0 and ways[i-1][j] != '#' and ways[i][j-1] != '#':
            if ways[i-1][j] < ways[i][j-1]:
                if i > 0:
                    ways[i-1][j] = '#'
                    i -= 1
                else:
                    print('Impossible')
                    flag = 0
                    break
            else:
                if j > 0:
                    ways[i][j - 1] = '#'
                    j -= 1
                else:
                    print('Impossible')
                    flag = 0
                    break
        elif (ways[i-1][j] == 0 or ways[i-1][j] == '#') and j > 0:
            ways[i][j - 1] = '#'
            j -= 1
        else:
            ways[i - 1][j] = '#'
            i -= 1
    if flag == 1:
        for i in range(n):
            for j in range(n):
                if ways[i][j] != '#':
                    ways[i][j] = '-'
        for line in ways:
            print(''.join(line))

if matrix[0][0] == 0 or matrix[n-1][n-1] == 0:
    print('Impossible')
else:
    ways = find_way(matrix, n)
    if matrix[0][0]+matrix[n-1][n-1] > ways[n-1][n-1]:
        print('Impossible')
    else:
        draw_way(ways, n)

