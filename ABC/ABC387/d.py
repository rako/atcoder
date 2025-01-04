h,w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0
start = [0,0]
goal = [0,0]
for i in range(h):
    for j in range(w):
        if s[i][j] == "S":
            start = [i,j]
        elif s[i][j] == "G":
            goal = [i,j]

#深さ優先探索で、動けなくなったら戻る
stack = [start]
while stack:
    x,y = stack.pop()
    while()