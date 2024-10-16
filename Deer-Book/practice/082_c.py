from collections import defaultdict

n = int(input())

s = list(map(int, input().split()))

ss = defaultdict(int)

for si in s:
    ss[si] += 1

sss = sorted(ss.items(), key=lambda x:x[1])

sss = dict(sss)

ans = 0
for sk,sv in sss.items():
    if sk > sv:
        ans += sv
    else:
        ans += sv-sk
print(ans)