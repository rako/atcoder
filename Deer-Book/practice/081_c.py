from collections import defaultdict

n,k = map(int, input().split())

a = list(map(int, input().split()))

aa = defaultdict(int)

for i in a:
    aa[i] += 1

ans = 0

#書き換える個数が少なくなるように、大きい方からK個の和をとって、書き換えないボールの個数の最大値が分かるのでこれをNから引く
temp = sorted(aa.items(), key=lambda x: x[1])

repnum = len(temp) - k

"""
if len(temp) > k:
    for i in range(k):
        ans += temp[i][1]
    print(n-ans)
else:
    print(0)
"""

for i in range(repnum):
    ans += temp[i][1]

print(ans)