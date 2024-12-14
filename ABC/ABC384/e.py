h,w,x = map(int, input().split())
p, q = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(h)]
print(grid)
p -= 1
q -= 1
boolgrid = [[False]*w for _ in range(h)]
boolgrid[p][q] = True
total = grid[p][q]
while (True):
    move = [(0,1),(1,0),(-1,0),(0,-1)]
    def search():
        for dx, dy in move:
            nx, ny = p+dx, q+dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] < total * (1/x) and boolgrid[nx][ny] != True:
                boolgrid[nx][ny] = True
                total += grid[nx][ny]
                p, q = nx, ny
                search()
            movecount += 1
    if movecount == 4:
        break
print(total)