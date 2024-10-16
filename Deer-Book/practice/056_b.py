n = int(input())

graph = [0] * n

for i in range(n):
    a = int(input())
    a -= 1
    graph[i] = a

x = graph[0]

count = 1

print(graph)

while (True):
    if graph[x] == 1:
        count += 1
        break
    else:
        x = graph[x]
        count += 1

print(count)