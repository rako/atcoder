n,m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a,b,w = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append([b, w])

print(graph)