from collections import defaultdict,Counter

s = list(input())
n = len(s)
scount = Counter(s)

print(scount)

snew=[""] * n

changecount = 1
while(len(set(snew)) != 1):
    for i in range(n):
        if s[i] in max(scount.keys(), key=lambda x: x[1]) or s[i+1] in max(scount.keys(), key=lambda x: x[1]):
            snew[i] = max(scount.keys(), key=lambda x: x[1])
        else:
            if changecount == 1:
                snew[i] = s[i]
                i += 1
            else:
                snew[i] = s[i]
print(*snew)