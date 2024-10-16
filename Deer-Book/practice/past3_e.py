n,m,q = map(int,input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    u,v = map(int, input().split())
    U,V = u-1,v-1
    graph[U].append(V)
    graph[V].append(U)

colorlist = list(map(int, input().split()))

s = []
for i in range(q):
    s.append(list(map(int,input().split())))

#print(graph)
for si in s:
    #print(si)
    if si[0] == 1:
        print(colorlist[si[1]-1])
        colornum = colorlist[si[1] - 1]
        for j in graph[si[1]-1]:
            colorlist[j] = colornum
    elif si[0] == 2:
        print(colorlist[si[1]-1])
        colorlist[si[1]-1] = si[2]