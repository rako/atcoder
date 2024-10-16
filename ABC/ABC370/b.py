n = int(input())

glist = []

for i in range(n):
    glist.append(list(map(int, input().split())))

i = 0
for j in range(n):
    if i >= j:
        i = glist[i][j] - 1
    else:
        i = glist[j][i] - 1

print(i + 1)