n,k = map(int, input().split())
a = list(map(int, input().split()))
a1 = a[-k:]
a2 = []
for i in range(k):
    a.pop(-1)
newa = a1 + a

print(*newa)