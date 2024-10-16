from collections import defaultdict

n = int(input())

a = list(map(int, input().split()))

adict = defaultdict(int)

for ai in a:
    adict[ai] += 1

m = len(adict)

adictl = list(adict.items())

ans = 0
for i in range(m-1):
    for j in range(i+1, m):
        ans += (adictl[i][1] * adictl[j][1])

print(ans)