n = int(input())

playlist = []

for i in range(n):
    temp = list(input().split())
    temp[0] = int(temp[0])
    playlist.append(temp)

ans = 0

Llist = [xi[0] for xi in playlist if xi[1] == "L"]
Rlist = [xi[0] for xi in playlist if xi[1] == "R"]

for i in range(len(Llist) - 1):
    ans += abs(Llist[i+1]-Llist[i])
for i in range(len(Rlist) - 1):
    ans += abs(Rlist[i+1]-Rlist[i])

#print(Llist,Rlist)
print(ans)