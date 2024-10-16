n,k = map(int, input().split())

a = list(map(int, input().split()))

graph = []

for i in range(n):
    graph.append(a[i] - 1)

visitedlist = []

count = 0

tmp,tmp2 = 0,0
while (True):
    if tmp in visitedlist:
        tmp2 = tmp
        break
    else:
        tmp = graph[tmp]
        visitedlist.append(tmp)

count,count2,checktmp = 0,0,False
while(True):
    if tmp == tmp2:
        if checkflag == False:
            count2 += 1
            checkflag = True
        else:
            break
    else:
        tmp = graph[tmp]
        count += 1

print(count + count2)