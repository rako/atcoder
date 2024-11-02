h,w,k = map(int, input().split())
hwlist = []
for i in range(h):
    hwlist.append(list(input()))

def is_valid(x, y, visited):
    return 0 <= x < h and 0 <= y < w and hwlist[x][y] == '.' and not visited[x][y]

def dfs(x, y, steps, visited):
    if steps == k:
        return 1
    
    visited[x][y] = True
    count = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, visited):
            count += dfs(nx, ny, steps + 1, visited)
    visited[x][y] = False
    return count

total_paths = 0
for i in range(h):
    for j in range(w):
        if hwlist[i][j] == '.':
            visited = [[False] * w for _ in range(h)]
            total_paths += dfs(i, j, 0, visited)
            #print(total_paths)

print(total_paths)