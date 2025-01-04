l,r = map(int, input().split())
ans = 0

ll = str(l)
rl = str(r)

if len(ll) == len(rl):
    pass
elif len(ll) < len(rl):
    tmpr = rl[0]
    rl2 = ""
    rl2 += tmpr
    for i in range(1,len(rl)):
        if int(tmpr) - 1 >= int(rl[i]):
            rl2 += rl[i]
        else:
            rl2 += str(int(tmpr) - 1)
    ## rは出来た。

    tmpl = ll[0]
    ll2 = ""
    ll2 += tmpl
    flag = 0
    for j in range(1,len(ll)):
        if j == 1:
            if int(ll[1]) >= int(tmpl):
                ll2 += str(int(tmpl) + 1)
                ll2 += str(0) * (len(ll) - 2)
                break
            if int(ll[j]) == (int(tmpl) - 1):
                flag = 1
            else:
                flag = 0
        else:
            if flag == 1:
                if int(ll[j]) >= int(tmpl):
                    ll2 += str(0)
                else:
                    ll2 += ll[j]
            else:
                if int(tmpl) - 1 >= int(ll[])

"""
lled = ""
for i in range(1,len(ll)):
    if int(ll[0]) <= int(ll[i]):
        lled += (int(ll[0]) - 1)
    else:
        lled += int(ll[i])

rred = ""
for j in range(1,len(rl)):
    if int(rl[0]) <= int(rl[j]):
        rred += (int(rl[0]) - 1)
    else:
        rred += int(rl[j])

if len(lled) < len(rred): #桁数が違う場合
    tmpr = 1 #初期化
    for k in range(len(rred)):
        tmpr *= (int(rred) + 1)
    ans += tmpr #最後に足し合わせる
elif len(lled) == len(rred): #同じ桁数の場合
    """"""
    for t in range(len(lled)):
        if lled[t] != rred[t]:
            keta = lled[t]
            break
    """"""
    if int(lled[0]) < int(rred[0]):
        genlled += lled[0]
        genlled += (lled[0] - 1) * (len(lled) - 1)
        intgenlled = int(genlled)
        llkake = intgenlled - int(lled)
        tmpll = 1
        for i in range(len(llkake)):
            tmpll *= (str(llkake[i]) + 1)
        ans += tmpll
    else:
        ans += 1
"""

#print(ans)