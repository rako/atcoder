k = int(input())
s = input()
t = input()
sn = len(s)
tn = len(t)

#1 S 中の (先頭や末尾を含む) 任意の位置に、任意の文字を 1 つ挿入する。
#2 S 中の文字を 1 つ選び、削除する。
#3 S 中の文字を 1 つ選び、別の 1 つの文字に変更する。

#ソートしたら全部ダメかも
#長さが同じ時は、3番のみ適用できるので、それを考える。
#長さが異なる(1文字違い)時は、1番か2番のどちらかを適用する。
#長さが異なる(2文字以上違い)時は、絶対にダメ

#置換するのが一文字より多い場合はダメ
if abs(sn - tn) > 1:
    print("No")
    exit()

#sn == tnの場合。長さが同じ時
elif sn == tn:
    flag = 0
    for i in range(sn):
        if s[i] != t[i]:
            flag += 1
    if flag <= 1:
        print("Yes")
        exit()
    else:
        print("No")
        exit()

#abs(sn - tn) == 1の場合。長さが異なる(1文字違い)時
elif abs(sn - tn) == 1:
    flag = 0
    if sn < tn: #tの方が長い
        i,j = 0,0
        while i < sn: #sの方が短い時に、別の文字となったら
            while j < tn:
                #print("i=" + str(i),"j=" + str(j))
                if s[i] == t[j]: #同じ文字があったら次の文字へ
                    break
                if s[i] != t[j]: #違う文字があったら
                    j += 1
                    flag += 1
            i += 1
            j += 1
    else: #sの方が長い
        i,j = 0,0
        while i < tn:
            while j < sn:
                #print("i=" + str(i),"j=" + str(j))
                if t[i] == s[j]:
                    break
                if t[i] != s[j]:
                    j += 1
                    flag += 1
            i += 1
            j += 1
    #print(flag)
    if flag > 1:
        print("No")
        exit()
    else:
        print("Yes")
        exit()