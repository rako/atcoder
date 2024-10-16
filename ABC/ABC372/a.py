s = input()

ans = []
for i in s:
    if i != ".":
        ans.append(i)

print(*ans, sep="")