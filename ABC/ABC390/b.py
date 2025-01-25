n = int(input())
a = list(map(int, input().split()))
r = a[1] / a[0]
for i in range(n-1):
  if a[i+1] == a[i] * r:
    continue
  else:
    print("No")
    exit()
print("Yes")