n = int(input())

a = list(map(int,input().split()))

count = 0
"""
up = 1 #
for i in range(n-1):
    if up == 1:
        if a[i] > a[i+1]:
            up = 0
    else:
        if a[i] < a[i+1]:
            up = 1
            count += 1
"""

i = 0
up = 1
count = 1
while(i<n):
    j = i + 1
    while(j<n):
        print(i,j)
        while(a[i] <= a[j] and up == 1) or (a[i] >= a[j] and up == 0):
            j += 1
    up = 0
    if i==0 and j==n-1:
        break
    else:
        count += 1
    i = j + 1

print(count)