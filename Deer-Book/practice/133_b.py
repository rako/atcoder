import math

n,d = map(int, input().split())

zahyo = []

for _ in range(n):
    zahyo.append(list(map(int, input().split())))

count = 0

for i in range(n-1):
    for j in range(i+1,n):
        x = 0
        for k in range(d):
            x += (zahyo[i][k] - zahyo[j][k]) ** 2
        if math.sqrt(x) == int(math.sqrt(x)):
            count += 1

print(count)