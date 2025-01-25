h,w = map(int,input().split())
grid = [list(input()) for _ in range(h)]
## #:黒, .:白, ?:任意
imin, imax, jmin, jmax = h-1, 0, w-1, 0 #ここは逆にしておく
for i in range(h):
  for j in range(w):
    if grid[i][j] == "#":
      imin = min(imin, i)
      jmin = min(jmin, j)
      imax = max(imax, i)
      jmax = max(jmax, j)
i,j = 0,0
for i in range(imin, imax+1):
  for j in range(jmin, jmax+1):
    if grid[i][j] == ".":
      print("No")
      exit()
print("Yes")
#print(imin, jmin, imax, jmax)