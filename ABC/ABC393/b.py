s = input()
ans = 0
for i in range(len(s)-2):
  for j in range(i+1, len(s)-1):
    for k in range(j+1, len(s)):
      if s[i] == "A" and s[j] == "B" and s[k] == "C":
        if j - i == k - j:
          ans += 1
print(ans)