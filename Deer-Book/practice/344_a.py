s = input()

count = 0

ans = []
for si in s:
    if si == "|":
        count += 1
        continue
    elif count == 0 or count == 2:
        ans.append(si)

print(*ans, sep="")