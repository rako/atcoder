n = int(input())
a = list(map(int, input().split()))

#尺取り法
# rが
r, ans = 0, 0
for l in range(n):
    while r < n and a[l] > a[r] // 2:
        r += 1
    ans += n - r
print(ans)