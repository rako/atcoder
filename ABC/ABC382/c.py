n,m = map(int, input().split())
a = list(map(int, input().split())) #n人
b = list(map(int, input().split())) #m個

"""
#これだとO(nm)かかる, 10^5*10^5=10^10, TLE
for bi in range(m):
    for ai in range(n):
        if b[bi] >= a[ai]:
            print(ai + 1)
            break
        elif bi < min(a):
            print(-1)
            break
"""

a_index = []
for ai,aj in enumerate(a):
    a_index.append((aj, ai+1))
#print(a_index)
a_index.sort()
#print(a_index)

ans = []

#a_indexを二分探索して、bの値以上の最小のaのindexを取得する
for bi in b:
    left = 0
    right = n
    while right - left > 1:
        mid = (left + right) // 2
        if a_index[mid][0] < bi:
            left = mid
        else:
            right = mid
    #print("bi:", bi)
    #print("left:", left)
    #print("right:", right)
    if a_index[left][0] <= bi:
        print(a_index[left][1])
    else:
        print(-1)