n, q = map(int, input().split())
x = list(map(int, input().split()))
nl = [0 for _ in range(n)]
ans = []

for xi in x:
    if xi >= 1:
        nl[xi-1] += 1
        ans.append(xi)
    elif xi == 0:
        minnum = min(nl)
        for i, ni in enumerate(nl):
            if ni == minnum:
                nl[i] += 1
                ans.append(i+1)
                break

print(*ans)