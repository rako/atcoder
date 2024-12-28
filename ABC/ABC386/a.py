tmp = list(map(int, input().split()))

from collections import Counter
"""
tmp = list(set([a,b,c,d]))
if len(tmp) == 2:
    print('Yes')
elif len(tmp) == 3:

else:
    print('No')
"""
exist = False
for i in range(1,14):
    tmp1 = tmp.copy()
    tmp1.append(i)
    c = Counter(tmp1)
    #print(c)
    flag = 0
    freq = list(c.values())
    if sorted(freq) == [2,3]:
        exist = True
print('Yes' if exist else 'No')