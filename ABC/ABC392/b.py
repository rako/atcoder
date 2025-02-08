n,m = map(int,input().split())
a = list(map(int,input().split()))
ans = []
for i in range(1,n+1):
  ans.append(i)
for j in a:
  ans.remove(j)
print(len(ans))
print(*ans)