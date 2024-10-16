s = input()
n = len(s)

#Rが続くと一番右のRに偏って、Lが続くと一番左のLに偏る
#偶奇で偶数の時に決まるかと思ったけど違いそう
#Rの場合で一番右のRには、自身を除いたRの数(Rの続いた数-1)+1=（つまり、Rの続いた数）
#Lの場合は逆に、一番左のLに自身を除いたLの数（Lの続いた数-1）=(つまり、Lの続いた数)

#RLが続いて、LからRに変わるときにセットが変わる。
#そのセットの中で、RとLの数の差で2以上で偶数であればRL変換点で合計数の1/2がそれぞれに入る。
#奇数であれば、合計数//2した数が変換点にそれぞれ入った後に、大きい方の数字が偶数であればそちらの方の変換点に+1で奇数であれば反対の方に+1


slist = []
i = 0
while i < n:
    j = i + 1
    while j < n and s[i] == s[j]:
        j += 1
    slist.append([s[i],j-i])
    i = j
#print(slist)

ans = [0] * n
itotal = 0
for i in range(len(slist) - 1):
    itotal += slist[i][1]
    if slist[i][0] == "R":
        difftotal = slist[i][1] + slist[i+1][1]
        if difftotal % 2 == 0:
            ans[itotal-1] = (difftotal)//2
            ans[itotal] = (difftotal)//2
        else:
            if slist[i][1] > slist[i+1][1]:
                if slist[i][1] % 2 == 0:
                    ans[itotal-1] = (difftotal)//2
                    ans[itotal] = (difftotal)//2 + 1
                else:
                    ans[itotal-1] = (difftotal)//2 + 1
                    ans[itotal] = (difftotal)//2
            else:
                if slist[i+1][1] % 2 == 0:
                    ans[itotal-1] = (difftotal)//2 + 1
                    ans[itotal] = (difftotal)//2
                else:
                    ans[itotal-1] = (difftotal)//2
                    ans[itotal] = (difftotal)//2 + 1
print(*ans)