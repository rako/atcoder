a,b = map(int,input().split())

count = 0

diff = abs(b-a)

for x in range(min(a,b)-diff, max(a,b)+diff+1):
    intlist = [a,b,x]
    intlist.sort()
    #Sprint(intlist)
    if (intlist[1] - intlist[0]) == (intlist[2] - intlist[1]):
        count += 1
    intlist.remove(x)

print(count)