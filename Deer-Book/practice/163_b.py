n = int(input())

a = list(map(int,input().split()))

graph = [[] for _ in range(n)]

for i in range(n-1):
    graph[a[i]-1].append(i+1)

for i in range(n):
    print(len(graph[i]))