import collections

def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

wall, clear, goal = "O", ".", "X"
width = height = int(input())
grid = []
for i in range(width):
    grid.append(input())
for i, line in enumerate(grid):
    if '@' in line:
        index_start = line.index('@')
        start = (index_start, i)
        grid[i] = grid[i].replace('@', '.')
        break
path = bfs(grid, start)
if path:
    print('YES')
    for i,j in path:
        grid[j] = grid[j][:i] + '+' + grid[j][i+1:]
    grid[start[1]] = grid[start[1]][:start[0]] + '@' +grid[start[1]][start[0]+1:]
    for line in grid:
        print(line)
else:
    print('NO')