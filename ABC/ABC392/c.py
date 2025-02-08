n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

pq = {}

for i in range(n):
  pq[q[i]] = p[i]

# print(pq)
ans = [0] * n

for key, value in pq.items():
  ans[key-1] = q[value-1]
print(*ans)