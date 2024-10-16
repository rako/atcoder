n,m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

##
bridge = [[] for _ in range(n)]
for ni,nv in enumerate(graph):
    if len(nv) == 1:
        bridge[ni].append(nv[0])
        bridge[nv[0]].append(ni)
    else:
        for nj,nk in enumerate(nv):
            
##全探索でその辺だけポップするとグラフとして全部の頂点に行けるか?