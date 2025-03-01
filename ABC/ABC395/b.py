n = int(input())
ans = [["?" for _ in range(n)] for _ in range(n)]
for i in range(n):
  j = n + 1 - i
  if i > j:
    continue
  if i <= j:
    color = "#" if i % 2 == 1 else "."
  for r in range(i-1, j):
    for c in range(i-1, j):
      ans[r][c] = color

for row in ans:
    print("".join(row))