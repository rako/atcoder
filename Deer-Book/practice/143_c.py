n = int(input())
s = input()

ans = []
i = 0
while i < n:
    j = i
    while j < n and s[i] == s[j]:
        j += 1
    ans.append(s[i])
    i = j

print(len(ans))