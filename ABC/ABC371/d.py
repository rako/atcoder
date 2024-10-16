import itertools,bisect

n = int(input())
x = list(map(int, input().split()))
p = list(map(int, input().split()))
#累積和
pac = [0] + list(itertools.accumulate(p))
#print(pac)
q = int(input())
lrlist = []
ans = []
for i in range(q):
    l,r = map(int, input().split())
    lposi = bisect.bisect_left(x, l)
    rposi = bisect.bisect_right(x, r)
    ans.append(pac[rposi] - pac[lposi])
    lrlist.append([lposi, rposi])

for i in ans:
    print(i)