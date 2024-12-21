h,w,x,y = map(int,input().split())
x -= 1
y -= 1
grid = [list(input()) for _ in range(h)]
t = list(input())
T = len(t)
#print(grid)
gridbool = [[False]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if grid[i][j] == "@":
            gridbool[i][j] = True

def check(x,y):
    if 0 <= x < h and 0 <= y < w:
        return True
    else:
        return False

count = 0
"""
def move(x,y):
    if grid[x][y] == "#":
        return 
    elif grid[x][y] == ".":
        continue
    elif grid[x][y] == "@":
        if gridbool[x][y]:
            gridbool[x][y] = False
            count += 1
"""
for k in t:
    #print(x,y)
    if k == "U":
        if check(x-1,y):
            if grid[x-1][y] == "#":
                continue
            elif grid[x-1][y] == ".":
                x = x-1
            elif grid[x-1][y] == "@":
                if gridbool[x-1][y]:
                    gridbool[x-1][y] = False
                    count += 1
                x = x-1
    elif k == "D":
        if check(x+1,y):
            if grid[x+1][y] == "#":
                continue
            elif grid[x+1][y] == ".":
                x = x+1
            elif grid[x+1][y] == "@":
                if gridbool[x+1][y]:
                    gridbool[x+1][y] = False
                    count += 1
                x = x+1
    elif k == "L":
        if check(x,y-1):
            if grid[x][y-1] == "#":
                continue
            elif grid[x][y-1] == ".":
                y = y-1
            elif grid[x][y-1] == "@":
                if gridbool[x][y-1]:
                    gridbool[x][y-1] = False
                    count += 1
                y = y-1
    elif k == "R":
        if check(x,y+1):
            if grid[x][y+1] == "#":
                continue
            elif grid[x][y+1] == ".":
                y = y+1
            elif grid[x][y+1] == "@":
                if gridbool[x][y+1]:
                    gridbool[x][y+1] = False
                    count += 1
                y = y+1

print(x+1,y+1,count)