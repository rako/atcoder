n,m = map(int, input().split())

a = list(map(int, input().split()))

ca = [0] * (n+1)

for i in range(n):
    ca[i+1] = ca[i] + a[i]

ans = 0
for k in range(n):
    ans += ca[k] - ca[k]