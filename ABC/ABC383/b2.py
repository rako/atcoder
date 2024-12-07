import sys
from itertools import combinations

H, W, D = map(int, sys.stdin.readline().split())
S = [sys.stdin.readline().strip() for _ in range(H)]

floor_cells = []
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            floor_cells.append((i, j))

max_count = 0

for humidifiers in combinations(floor_cells, 2):
    humidified = set()
    for cell in floor_cells:
        if any(abs(cell[0]-h[0]) + abs(cell[1]-h[1]) <= D for h in humidifiers):
            humidified.add(cell)
    count = len(humidified)
    if count > max_count:
        max_count = count

print(max_count)