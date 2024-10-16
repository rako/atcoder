s = input()
n = len(s)

ans = []
i = 0
while i < n:
    j = i
    while j < n and s[i] == s[j]:
        j += 1
    ans.append(s[i] + str(j-i))
    i = j
print("".join(ans))