from collections import deque
h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

dist = [[-1 for _ in range(w)] for _ in range(h)]
queue = deque()

for r in range(h):
    for c in range(w):
        if grid[r][c] == 'E':
            dist[r][c] = 0
            queue.append((r, c))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
directions = ['^', 'v', '<', '>']

while queue:
    r, c = queue.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != '#' and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            queue.append((nr, nc))

result_grid = [['' for _ in range(w)] for _ in range(h)]

for r in range(h):
    for c in range(w):
        if grid[r][c] == '#':
            result_grid[r][c] = '#'
        elif grid[r][c] == 'E':
            result_grid[r][c] = 'E'
        else:
            if dist[r][c] == -1:
                pass
            else:
                found_direction = False
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if 0 <= nr < h and 0 <= nc < w and \
                       grid[nr][nc] != '#' and dist[nr][nc] != -1 and \
                       dist[nr][nc] == dist[r][c] - 1:
                        result_grid[r][c] = directions[i]
                        found_direction = True
                        break

for r in range(h):
    print("".join(result_grid[r]))