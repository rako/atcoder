key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

s = input()

tmp = s.index("A")
last = s.index("Z")
count = 1
ans = 0
while (True):
    if count == 26:
        break
    else:
        ans += abs(s.index(key[count]) - tmp)
        tmp = s.index(key[count])
        count += 1

#for i in range(26):
    #ans += s.index(key[i]) - tmp

print(ans)