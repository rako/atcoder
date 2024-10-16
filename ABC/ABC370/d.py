h,w,q = map(int, input().split())

glid = [["#" for _ in range(w)] * h]

def destroy(r,c):
    if r != 0:
        glid[r-1][c] = ""
    if r != h-1:
        glid[r+1][c] = ""
    if c != 0:
        glid[r][c-1] = ""
    if c != w-1:
        glid[r][c+1] = ""

for i in range(q):
    r,c = map(int, input().split())
    r -= 1
    c -= 1
    if glid[r][c] == "#":
        glid[r][c] = ""
    else:
        destroy(r,c)

count = 0

for i in range(h):
    for j in range(w):
        if glid[i][j] == "#":
            count += 1

print(count)