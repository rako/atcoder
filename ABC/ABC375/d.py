from bisect import bisect, bisect_left, bisect_right
import itertools
from collections import defaultdict, Counter

s = input()

strlist = {}

for i in range(len(s)):
    if s[i] not in strlist:
        strlist[s[i]] = []
    strlist[s[i]].append(i)

#print(strlist)

count = 0
lenlist = []
"""
for k,v in strlist.items():
    if len(v) == 1:
        lenlist.append(v[0])
"""

for k1,v1 in strlist.items():
    for i in v1:
        for k2,v2 in strlist.items():
            if k1 != k2:
                #print(i,v2)
                n = len(v2)
                index = bisect(v2,i)
                #print(index)
                #print((n - index) * index)
                #if (n - index) * index > 0:
                    #print(k2)
                count += (n - index) * index
            #else:
                #n = len(v2)
                #list2.append(list(itertools.combinations(v2, 3)))
                #count += len(list(itertools.combinations(v2, 3)))
                #print(set(list(itertools.combinations(v2, 3))))
    if len(v1) >= 3:
        count += len(list(itertools.combinations(v1, 3)))



print(count)