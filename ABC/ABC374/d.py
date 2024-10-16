import math

n,s,t = map(int, input().split())

zl = []
fl = []

for i in range(n):
    a,b,c,d = map(int, input().split())
    fl.append([a,b,c,d])
    zl.append([a,b])
    zl.append([c,d])

#初期位置
x,y = 0,0

ans = 0

#print(fl)

usedlist = []
while (True):
    if len(usedlist) == n:
        break
    #探し出す操作
    minnum = 10**9
    flag = 13
    for j in zl:
        if ((j[0] - x)** 2 + (j[1] - y) ** 2) < minnum:
            minnum = (j[0] - x)** 2 + (j[1] - y) ** 2
            flag = zl.index(j)
    #探し終わってから実際に照射しないで動く時間と照射して動く時間を計算
    n,m = flag//2, 2*(flag%2)
    #print(n,m)
    ans += (math.sqrt(((fl[n][m] - x) ** 2 + (fl[n][m+1] - y) ** 2)) / t)
    ans += (math.sqrt(((fl[n][(m+1)//2] - fl[n][m]) ** 2 + (fl[n][(m+2)//2] - fl[n][m+1]) ** 2)) / t)
    x,y = fl[n][(m+1)//2],fl[n][(m+2)//2]
    usedlist.append(n)
print(ans)