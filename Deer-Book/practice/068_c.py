n,m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int, input().split()) #a<b
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

exist = False
for i in graph[0]:
    for j in graph[i]:
        if j == n-1:
            exist = True

print("POSSIBLE" if exist else "IMPOSSIBLE")