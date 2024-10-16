s = input()
t = input()

eqstr = False

if "".join(s) == t:
    eqstr = True

for i in range(len(s)-1):
    L = list(s) #入力時点ではなく、この行でlist化するとfor文ごとにsがLに入力される, immutableとmutableの違い？
    L[i],L[i+1] = L[i+1],L[i]
    if "".join(s) == t:
        eqstr = True
    #s[i],s[i+1] = s[i+1],s[i] #なぜ？
    print(s,L,id(L))

print("Yes" if eqstr else "No")