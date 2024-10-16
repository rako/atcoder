a = [list(map(int,input().split())) for _ in range(3)]

n = int(input())

b = [int(input()) for _ in range(n)]

for j in range(3):
    for k in range(3):
        if a[j][k] in b:
            a[j][k] = "#"

exist = False
if (a[0][0] == a[0][1] == a[0][2] == "#") or (a[1][0] == a[1][1] == a[1][2] == "#") or (a[2][0] == a[2][1] == a[2][2] == "#") or (a[0][0] == a[1][0] == a[2][0] == "#") or (a[0][1] == a[1][1] == a[2][1] == "#") or (a[0][2] == a[1][2] == a[2][2] == "#") or (a[0][0] == a[1][1] == a[2][2] == "#") or (a[0][2] == a[1][1] == a[2][0]):
    exist = True

print("Yes" if exist else "No")