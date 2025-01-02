n = int(input())
s = [input() for _ in range(n)]
sdict = {}
ans = []
for si in s:
    if si not in sdict:
        sdict[si] = 1
        ans.append(si)
    else:
        si2 = si + "(" + str(sdict[si]) + ")"
        sdict[si] += 1
        ans.append(si2)
for an in ans:
    print(an)