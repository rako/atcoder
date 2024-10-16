"""
from collections import Counter,defaultdict

n = int(input())

a = list(map(int, input().split()))

def setint(a):
    alist = defaultdict(int)
    for ai in a:
        alist[ai] += 1
    acount = Counter(a)
    return len(a) - acount[0]

#print(Counter(a)[1])

count = 0
while(setint(a) != 1):
    a.sort(reverse=True)
    for i in range(2):
        if a[i] != 0:
            a[i] -= 1
    count += 1
    #print(a,count)

print(count)
"""

from collections import defaultdict,Counter

n = int(input())

a = list(map(int, input().split()))

def valint(a):
    count = 0
    for i in a:
        if i >= 1:
            count += 1
    if count >= 2:
        return True
    else:
        return False
count = 0
while(valint(a)):
    a.sort(reverse=True)
    for i in range(2):
        a[i] -= 1
    count += 1
print(count)