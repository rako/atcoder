from collections import defaultdict,Counter

n,m = map(int, input().split())
h = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    if h[a] > h[b]:
        graph[a].append(b)
    elif h[b] > h[a]:
        graph[b].append(a)
    elif h[a] == h[b]:
        if (len(graph[a]) == 0):
            graph[a].append(b)
            continue
        elif (len(graph[b]) == 0):
            graph[b].append(a)
            continue

count = 0
for i in range(n):
    if len(graph[i]) >= 1:
        count += 1
print(count)
print(graph)