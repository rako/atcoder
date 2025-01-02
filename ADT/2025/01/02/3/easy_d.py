import collections
n = int(input())
s = [input() for _ in range(n)]
c = collections.Counter(s)
k,v = max(c.items(), key=lambda x: x[1])
print(k)