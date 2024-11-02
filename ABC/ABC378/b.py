anslist = []
n = int(input())
qrlist = []
for i in range(n):
    q,r = map(int, input().split())
    qrlist.append([q,r])
q = int(input())
ablist = []
for i in range(q):
    a,b = map(int, input().split())
    a2 = b // qrlist[a-1][0]
    b2 = b % qrlist[a-1][0]
    #print("a2",a2,"b2",b2)
    ans = 0
    if b2 <= qrlist[a-1][1]:
        ans = a2 * qrlist[a-1][0] + qrlist[a-1][1]
    else:
        ans = (a2 + 1) * (qrlist[a-1][0]) + qrlist[a-1][1]
    #print(ans)
    anslist.append(ans)
for i in anslist:
    print(i)