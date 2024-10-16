n,m = map(int, input().split())

#graph = [[] for _ in range(n)]

numgraph = [0] * n

for i in range(m):
    u,v,w = map(int, input().split())
    u -= 1
    v -= 1
    x = numgraph[u]
    y = numgraph[v]
    diff = y - x
    numgraph[v] = x + w - diff
    numgraph[u] = x - diff
    print("list", *numgraph)
#print(*numgraph)

if max(numgraph) > 10**18:
    diff = max(numgraph) - 10**18
    numgraph = [x - diff for x in numgraph]
elif min(numgraph) < -(10**18):
    diff = 10**18 - min(numgraph)
    numgraph = [x + diff for x in numgraph]

#print(*numgraph)