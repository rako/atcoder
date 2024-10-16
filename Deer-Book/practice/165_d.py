import math

a,b,n = map(int, input().split())

ans = 0

#これで右の項はfloorが一緒の値の中でxが一番大きい値を持ってこられるようになった
#bが1でnが10**12であったらTLE
if b > n: #n//b = 0となってしまうとき、右の項は必ず0となるため、x=nとして左項のみが計算される
    ans = math.floor(a*n/b)
else:
    for x in range(1,n//b + 1):
        x = x*b - 1
        ans = max(ans, math.floor(a*x/b) - a * math.floor(x/b))
        print("x",x)

print("ans",ans)