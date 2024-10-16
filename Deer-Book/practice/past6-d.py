n,k = map(int, input().split())

a = list(map(int, input().split()))

newa = [0] * (n+1)

for i in range(n):
    newa[i+1] = newa[i] + a[i]

for i in range(n-k+1):
    print(newa[i + n-k] - newa[i])