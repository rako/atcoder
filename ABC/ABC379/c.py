import itertools
n,m = map(int, input().split())
x = list(map(int, input().split())) #xがインデックス
a = list(map(int, input().split())) #xのインデックスにある石の数

#x.append(n)

#累積和
acmlist = list(itertools.accumulate(a))

blist = []

exist = True
count = 0
if sum(acmlist) < n:
    exist = False
for xi in range(1, m):
    if acmlist[xi - 1] < x[xi] - 1:
        exist = False
        break
    elif x[xi] - x[xi-1] <= a[xi-1]:
        z = x[xi] - x[xi-1] - 1
        count += z*(z+1)//2
        blist.append([xi,a[xi-1] - (x[xi] - x[xi-1])])
    else:
        t = x[xi] - x[xi-1] - a[xi-1] #足りない分
        if blist[-1][1] >= t:
            count += t * (xi - blist[-1][0]) 
            blist[-1][1] -= t
        else:
            while (t > 0):
                g = blist[-1][1]
                count += g * (xi - blist[-1][0])
                blist.pop(-1)
                t -= g
                if blist[-1][1] >= t - g:
                    blist[-1][1] -= t - g
                else:
                    blist[-1][1]
y = n - x[-1]
count += y*(y+1)//2
print(count if exist else -1)