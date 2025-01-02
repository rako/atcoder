n,m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
#print(grid)
def tc_check(x,y): #TaK Code check, x-n, y-m回しか行わない
    existlist = []
    for i in range(9):
        for j in range(9):
            s = x + i #xは基準点、iは相対点
            t = y + j #yは基準点、jは相対点
            #print(s, t)
            if 0 <= i <= 2 and 0 <= j <= 2: #黒
                if grid[s][t] == "#":
                    return True
            elif 6 <= i <= 8 and 6 <= j <= 8:
                if grid[s][t] == "#":
                    return True
            elif 0 <= i <= 3 and j == 3: #白
                if grid[s][t] == ".":
                    return True
            elif i == 3 and 0 <= j <= 3:
                if grid[s][t] == ".":
                    return True
            elif i == 5 and 5 <= j <= 8:
                if grid[s][t] == ".":
                    return True
            elif 5 <= i <= 8 and j == 5:
                if grid[s][t] == ".":
                    return True

for a in range(n-9):
    for b in range(m-9):
        tc_check(a,b)
        #print(a,b) #ここまで行けてる
        if tc_check(a, b):
            print(a,b)