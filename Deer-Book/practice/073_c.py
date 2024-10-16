from collections import defaultdict

n = int(input())

intdic = defaultdict(int)

for i in range(n):
    ii = int(input())
    if intdic[ii] != 0:
        intdic[ii] -= 1
    elif intdic[ii] == 0 or ii not in intdic:
        intdic[ii] = 1

ans = 0
for i in intdic.values():
    if i != 0:
        ans += 1

print(ans)