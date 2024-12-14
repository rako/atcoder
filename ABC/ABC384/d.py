import itertools
n,s = map(int, input().split())
a = list(map(int, input().split()))
a2 = a*2
accma2 = list(itertools.accumulate(a2))

sum_a = sum(a)
nk = s % sum_a
#尺取り
r, ans, tmp = 0, 0, 1
for l in range(n*2):
    while r < n*2 and accma2[r+1] - accma2[l] < nk:
        r += 1
    print(l,r)
    if accma2[r+1] - accma2[l] == nk:
        ans = 1
        break
print("Yes" if ans == 1 else "No")