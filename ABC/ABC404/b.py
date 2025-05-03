n = int(input())
s = []
for i in range(n):
    si = list(input())
    s.append(si)
t = []
for j in range(n):
    tj = list(input())
    t.append(tj)
print(s)
print(t)
# 回転を3回行ってみる
diff = 10**6
difflist = []
led = [s]
for k in range(4):
    l = [['' for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            l[b][n-1-a] = s[a][b]
    diff2 = 0
    for i in range(0,n):
        for j in range(0,n):
            if t[i][j] != l[i][j]:
                diff2 += 1
    difflist.append(diff2)
    led.append(l)

mindiff = min(difflist)
minindex = difflist.index(mindiff)
total = minindex + 1

ll = led[minindex]

for li in range(n):
    for lj in range(n):
        if ll[li][lj] != t[li][lj]:
            total += 1

print(total)