import itertools, math
n = int(input())
xylist = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for s,t in list(itertools.combinations(xylist, 2)):
    ans = max(ans, math.sqrt((t[0]-s[0])**2 + (t[1]-s[1])**2))
print(ans)