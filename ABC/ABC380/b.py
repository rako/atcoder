s = list(input())
ans = []
i = 1
while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i] == "-":
        j += 1
    ans.append(j - i)
    i = j + 1
print(*ans, sep=" ")