n, x = map(int, input().split())

m = []
for i in range(n):
    j = int(input())
    x -= j
    m.append(j)

print(n + (x // min(m)))