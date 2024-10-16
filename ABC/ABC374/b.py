s = input()
t = input()
ls = len(s)
lt = len(t)
ans = 0
for i in range(min(ls,lt)):
    #print(i)
    if s[i] != t[i]:
        ans = i+1
        break
if ans == 0 and ls != lt:
    ans = min(ls,lt) + 1
print(ans)