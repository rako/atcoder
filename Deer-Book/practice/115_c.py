n, k = map(int, input().split())

h = []

for _ in range(n):
    h.append(int(input()))

h.sort()

minlist = []
for i in range(n-k+1):
    minlist.append(h[i+k-1] - h[i])

print(min(minlist))