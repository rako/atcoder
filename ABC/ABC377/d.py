import bisect
n,m = map(int, input().split())
lrlist = []
for i in range(n):
    l,r = map(int, input().split())
    lrlist.append([l,r])
minllist = sorted(lrlist, key=lambda x: x[0])
minrlist = sorted(lrlist, key=lambda x: x[1])
minl = minllist[0][0]
minr = minrlist[0][1]
print(minllist)
print(minrlist)

ans = 0
for m in range(1,m+1):
    if m <= minllist[0][0]:
        ans += minrlist[0][1]-m
        if minrlist[0][1]-m == 0 and minrlist[0][1] != minrlist[0][0]:
            ans += 1
        print(m,minrlist[0][1])
    elif m >= minllist[-1][0]:
        ans += minllist[-1][1]-m
        if minllist[-1][1]-m == 0 and minllist[-1][1] != minllist[-1][0]:
            ans += 1
        print(m,minllist[-1][1])
    else:
        #二分探索でm以上の最小のlを探す
        left = 0
        right = n-1
        while left < right:
            mid = (left+right)//2
            if minllist[mid][0] >= m:
                right = mid
            else:
                left = mid+1
        #print(right)
        #二分探索で最小のrを探す
        tmp = sorted(minllist[right:], key=lambda x: x[1])[0][1]
        ans += tmp - m
        #print(m,minllist2)
        #print(left,right)
        print(m, tmp)

print(ans)