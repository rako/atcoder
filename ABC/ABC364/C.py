n, x, y = map(int, input().split())

a = map(int,input().split())

b = map(int,input().split())

ablist = []
ablist.append(a)
ablist.append(b)


for i in range(n):
    amax = int(max(a))
    aindex = a.index(amax)
    atemp = a.pop(amax)
    x = x - atemp
    y = y - b[aindex]
    b.pop(b[aindex])
    if x < 0 or y < 0:
        print(str(i))
        break