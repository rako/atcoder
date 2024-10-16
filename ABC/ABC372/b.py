import itertools

m = int(input())

def maxruijo(m):
    if m < 1:
        return None
    p = 1
    while p * 3 <= m:
        p *= 3
    return p

l = maxruijo(m)

ans = [0, []]
intlist = [i for i in range(0,11)]

for n in range(1,21):
    l2 = list(itertools.combinations_with_replacement(intlist, n))
    for l3 in l2:
        if sum(l3) > 10:
            break
        total = 0
        for i in l3:
            total += 3 ** i
        if total == m:
            ans[0] = n
            ans[1] = l3

print(ans)

"""
for n in range(1,21):
    tmpm = m
    for ai in range(11**n):
        a = [0] * n
        tmp = ai
        total = 0
        for i in range(n):
            a[i] = tmp % 11
            total += 3 ** a[i]
            tmp //= 11
        if total == m:
            ans[0] = n
            ans[1].append(a)
"""