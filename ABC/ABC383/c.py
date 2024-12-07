n, m, d = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(input()))

from collections import deque

def dfs(x, y):
    visited = [[-1]*m for _ in range(n)]
    stack = deque()
    stack.append((x, y, 0))
    while stack:
        i, j, depth = stack.pop()
        if depth > d:
            continue
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < m:
                if grid[ni][nj] == '.' and visited[ni][nj] == -1:
                    visited[ni][nj] = depth + 1
                    grid[ni][nj] = 'P'  # 塗る
                    stack.append((ni, nj, depth + 1))

# 'H'から深さ優先探索を開始
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'H':
            dfs(i, j)
count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'P':
            count += 1
print(grid)
print(count)