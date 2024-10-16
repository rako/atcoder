a,b = map(int, input().split())

intlist = [1,2,3]
if a != b:
    intlist.remove(a)
    intlist.remove(b)
    print(intlist[0])
else:
    print(-1)