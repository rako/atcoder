h,w,x,y = map(int, input().split())

s = [list(input()) for _ in range(h)]

X = x - 1
Y = y - 1

if s[X][Y] == "#":
    print(0)
    exit()
else:
    count = 1

for i in range(h//2):
    if s[X-i][Y] == ".":
        count += 1
    else:
        break

for i in range(h//2):    
    if s[X+i][Y] == ".":
        count += 1
    else:
        break

for i in range(w//2):    
    if s[X][Y-i] == ".":
        count += 1
    else:
        break

for i in range(w//2):    
    if s[X][Y+i] == ".":
        count += 1
    else:
        break

print(count)

"""
for i in range(h):
    for j in range(w):
        if i == X and j == Y and s[i][j] == "#":
            count = 0
        else:
            count = 1
            if i == X:
                if s[i][max(Y-j,0)] == "#" or s[i][min(Y+j, w-1)] == "#":
                    break
                else:
                    count += 1
            if j == Y:
                if s[max(X-i,0)][j] == "#" or s[min(Y+i,h-1)][j] == "#":
                    break
                else:
                    count += 1
            

"""

print(count)