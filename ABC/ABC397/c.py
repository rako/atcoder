n = int(input())
a = list(map(int, input().split()))
total = 0
"""
for i in range(1, n):
    pre = len(set(a[:i]))
    aft = len(set(a[i:]))
    print("pre", pre, "aft", aft)
    total = max(total, pre + aft)"
"""
pre = set()
aft = set()
for i in range(n//2 + 1):
    #print(i, n-i-1)
    #print(len(set(a[:i])), len(set(a[i:])))
    
    if i == n//2:
        total = len(set(a[:i])) + len(set(a[i:]))
        break
    
    if a[i] in pre:
        total = len(set(a[:i])) + len(set(a[i:]))
        break
    if a[n-i-1] in aft:
        total = len(set(a[:i])) + len(set(a[i:]))
        break
    else:
        pre.add(a[i])
        aft.add(a[n-i-1])
        continue

print(total)