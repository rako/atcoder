s = input()
ans = 0
while True:
    #print(s)
    flag = False
    i = 0
    while i < len(s):
        if i % 2 == 0:
            if s[i] == "i":
                pass
            else:
                s = s[:i] + "i" +s[i:]
                ans += 1
                flag = True
                break
        else:
            if s[i] == "o":
                pass
            else:
                s = s[:i] + "o" +s[i:]
                ans += 1
                flag = True
                break
        i += 1
    if flag == False:
        break
        
if len(s) % 2 != 0: #偶数の時
    ans += 1
print(ans)
exit()