n,m = map(int, input().split())
graph = [1] * n
for i in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  graph[a] = 0
  graph[b] = 0
  #print("a-1:", a-1, "b-1:", b-1)
print(graph.count(1))