n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
print(a)
print(b)
"""
for i in range(n-2):
    if max(a) < max(b):
        maxindexa = a.index(max(a))
        maxindexb = b.index(max(b))
        a.pop(maxindexa)
        b.pop(maxindexb)

#print(a,b)
if min(a) > min(b):
    print(-1)
elif max(a) < max(b):
    print(min(a))
else:
    print(max(a))
"""

exist = 0
flag = 0
for i in range(-1,-n+1,-1):
    if flag == 0:
        if a[i] <= b[i]:
            pass
        else:
            flag = 1
    else:
        exist = 1

if exist == 0:
    if a[0] > b[0]:
        print(-1)
    elif a[1] < b[0]:
        print(a[0])
    else:
        print(a[1])
else:
    print(-1)