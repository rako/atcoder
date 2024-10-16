h,w = map(int, input().split())

a = [list(input()) for _ in range(h)]

cutlistx = []
cutlisty = []

for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            continue
        else:
            if any("#" in a[i]):
                continue
            else:
                cutlistx.append(i)
            for k in range(h):
                if ("#" == a[k][j]):
                    continue
                else:
                    cutlisty.append(j)

for i in range(len(cutlistx)):
    a.remove(cutlistx[i])

for j in range(len(cutlisty)):
    for k in range(h):
        a[k].remove(cutlisty[j])

for i in range(h):
    print("".join(a[i]))