N, T, P = map(int, input().split())

Llist = list(map(int, input().split()))

day = 0

flag = 0
while (flag != 1):
    count = 0 #条件満たす人の数の初期化
    for i, j in enumerate(Llist): #要素一つ一つ取り出し
        if j >= T: #条件を満たすか
            count += 1 #満たしたらカウントアップ
        if count >= P: #条件2が満たしたら
            flag = 1
            break
        j += 1
        Llist[i] = j
    day += 1
    #print(Llist)

print(str(day - 1))