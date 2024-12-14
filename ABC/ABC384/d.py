#import itertools
from collections import deque
n,s = map(int, input().split())
a = list(map(int, input().split()))
a2 = a*2
##accma2 = list(itertools.accumulate(a2))

#尺取り？
sum_a = sum(a)
nk = s % sum_a
"""
if sum_a <= s:
    print("Yes")
else:
    print("No")
"""
#print(nk)

#print(a2)
#print(accma2)

"""
r, ans, tmp = 0, 0, 1
for l in range(n):
    while r < n and accma2[r] - accma2[l] < s:
        r += 1
    if accma2[r] - accma2[l] == s:
        ans = 1
        break
print("Yes" if ans == 1 else "No")
ans = 0
q = deque()
p = 0
for c in a:
    q.append(c)
    p += c
    while q and p != nk:
        print(q)
        rm = q.popleft()
        p -= rm
    if p == nk:
        ans = 1
        break
print("Yes" if ans == 1 else "No")
"""

#尺取り
r, ans, tmp = 0, 0, 1
for l in range(n*2):
    while r < n*2 and sum(a2[l:r+1]) < nk:
        r += 1
    if sum(a[l:r+1]) == nk:
        ans = 1
        break
print("Yes" if ans == 1 else "No")