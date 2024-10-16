n,q = map(int, input().split())

s = input()

aclist = [0] * n

for i in range(1,n):
    #total[i+1] = total[i] + s[i]
    if s[i-1] == "A" and s[i] == "C":
        aclist[i] += 1

total = [0] * (n+1)
for i in range(n):
    total[i+1] = total[i] + aclist[i]

query = [[] for _ in range(q)]

#print(query)

for i in range(q):
    l,r = map(int, input().split())
    query[i] = [l,r]

#print(total)
for qi in query:
    l,r = qi[0],qi[1]
    #例外として[3:9]等の場合はtotalで境界値がCのところで数えられてしまうため、[l:r)に対しては、aclist[l+1:r]中の数値の総和
    print(total[r]-total[l])