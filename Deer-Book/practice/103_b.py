s = input()
t = input()

eqstr = False

for i in range(len(s)):
    s = s[-1] + s[:-1]
    if s == t:
        eqstr = True

print("Yes" if eqstr else "No")