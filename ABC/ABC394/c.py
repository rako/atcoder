s = input()
ans = ""
i = 0
while i < len(s):
    if s[i] == "W":
        start = i
        while i < len(s) and s[i] == "W":
            i += 1
        if i < len(s) and s[i] == "A":
            count = i - start
            i += 1
            ans += "AC" + "C" * (count - 1)
        else:
            ans += s[start:i]
    else:
        ans += s[i]
        i += 1
print(ans)