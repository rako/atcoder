from collections import defaultdict,Counter

n = int(input())

"""
sdic = []

for i in range(n):
    sdic.append(input())

ss = Counter(sdic)
maxnum = max(ss.values())

ans = []
for i in ss.keys():
    if ss[i] == maxnum:
        ans.append(i)

ans.sort()

for i in range(len(ans)):
    print(ans[i])

"""
sdic = defaultdict(int)

for i in range(n):
    ss = input()
    sdic[ss] += 1

sk = []
maxnum = max(sdic.values()) #maxnumをfor文の外に出しておかないと、for文の実行回数分sdicを走査してしまう
for i in sdic.keys():
    if sdic[i] == maxnum:
        sk.append(i)

sk.sort()

print(*sk, sep="\n")
