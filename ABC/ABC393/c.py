from copy import deepcopy
from collections import Counter
n,m = map(int,input().split())
graph = [[] for _ in range(n)]
ans = 0
for _ in range(m):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  #print("u:",u,"v:",v)
  if (u == v) or (u in graph[v]) or (v in graph[u]):
    ans += 1
  graph[u].append(v)
  # 自己ループ or 多重辺
  #print("ans:",ans)

#print(graph)

print(ans)