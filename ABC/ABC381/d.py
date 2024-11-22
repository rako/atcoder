n = int(input())
a = list(map(int, input().split()))
#print(n,a)


setlist = []
i = 0
while i < n:
    j = i
    while j < n and a[j] == a[i]:
        j += 1
    setlist.append((a[i], j - i))
    i = j
#print(setlist)
finalcount = 0
for i in range(len(setlist)):
    anslist = {}
    count = 0
    j = i
    if setlist[i][1] == 2:
        while j < len(setlist) and setlist[j][1] == 2:
            #print(j)
            if setlist[j][0] not in anslist:
                anslist[setlist[j][0]] = setlist[j][1]
                count += 2
            else:
                break
            j += 1
    if finalcount < count:
        finalcount = count
print(finalcount)
"""
i = 0
ans = 0
if n == 1:
    print(0)
    exit()
while(i < n):
    j = i
    count = 0
    tmplist = []
    #print(i,j)
    if j + 1 >= n:
        break
    if a[j] == a[j+1]:
        while(j < n and a[j] not in tmplist and a[j] == a[j+1]):
            tmplist.append(a[j])
            #print(i,j)
            j += 2
            count += 2
        i = j
    else:
        i = j + 1
    if ans < count:
        ans = count
print(ans)
"""