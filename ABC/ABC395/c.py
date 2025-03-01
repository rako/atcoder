n = int(input())
a = list(map(int, input().split()))
"""
c = Counter(a)
searchlist = []
for key, value in c.items():
  if value >= 2:
    index = a.index(key)
    searchlist.append(index)
if len(searchlist) == 0:
  print(-1)
  exit()
#print(searchlist)
"""
ans = 10**6
searchlist = {}
for i, val in enumerate(a):
  if val in searchlist:
    ans = min(ans, i - searchlist[val] + 1)
  searchlist[val] = i
print(ans if ans != 10**6 else -1)