from collections import Counter
import itertools

n = int(input())
saikoro = {}

for i in range(n):
  query = input().split()
  k = int(query[0])
  a = list(map(int,query[1:]))
  count = Counter(a)
  saikoro[i] = (k, count)

fans = 0

for j in list(itertools.combinations([x for x in range(n)],2)):
  ans = 0
  s,t = j[0],j[1]
  if saikoro[j[0]][0] > saikoro[j[1]][0]:
    s,t = j[1],j[0]
  for k,l in saikoro[t][1].items():
    if k not in saikoro[s][1]:
      continue
    ans += (saikoro[s][1][k] / saikoro[s][0]) * (saikoro[t][1][k] / saikoro[t][0])
  fans = max(fans, ans)
print(fans)