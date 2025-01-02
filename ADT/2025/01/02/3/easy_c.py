h,w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
ol = []
for i in range(h):
    for j in range(w):
        if grid[i][j] == "o":
            ol.append((i,j))
print(abs(ol[0][0] - ol[1][0]) + abs(ol[0][1] - ol[1][1]))