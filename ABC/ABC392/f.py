n = int(input())
p = list(map(int, input().split()))

a = []
for i in range(n):
  a2 = a[:(p[i]-1)]
  a2.append(i+1)
  a2.append(a[p[i]:])
print(*a)