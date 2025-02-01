n,m = map(int, input().split())
sgrid = [list(input()) for _ in range(n)]
tgrid = [list(input()) for _ in range(m)]

for si in range(n-m+1):
  for sj in range(n-m+1):
    flag = True
    for ti in range(m):
      for tj in range(m):
        if sgrid[si+ti][sj+tj] != tgrid[ti][tj]:
          flag = False
    if flag:
      print(si+1,sj+1)
      exit()