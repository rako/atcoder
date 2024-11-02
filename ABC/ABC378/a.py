from collections import Counter
i = list(input().split())
i = Counter(i)
ans = 0
for j in i.values():
    if j == 2:
        ans += 1
    elif j == 4:
        ans += 2
    elif j == 3:
        ans += 1
print(ans)

