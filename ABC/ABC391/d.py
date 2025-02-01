# tetris
n,w = map(int, input().split())
tetris = [[] for _ in range(w)]
for i in range(n):
  x,y = map(int, input().split())
  x -= 1
  y -= 1
  tetris[x].append([y,i+1])
q = int(input())
print(tetris)
ans = []
for j in range(q):
  t,a = map(int, input().split())
  