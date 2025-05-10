#import itertools
n = int(input())
a = list(map(int, input().split()))

total = 0

"""
for i in a:
    for j in a:
        total += i*j

for k in a:
    total -= k*k

total //= 2


comblist = list(itertools.combinations(a, 2))
for numlist in comblist:
    total += numlist[0] * numlist[1]
"""
tmpsum = sum(a)
for i in range(n-1):
    #print("total", total)
    #print("i", i)
    tmpsum -= a[i]
    total += a[i] * tmpsum

print(total)