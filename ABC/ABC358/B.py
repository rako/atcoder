N, A = map(int, input().split())

T = list(map(int, input().split()))

#到着順に処理して、先着がいたら残っている時間にAの値分を加える

time = 0
diff = 0
for i in range(N):
    diff = time - T[i]
    if i != 0: #二番目以降の処理
        if (diff <= 0): #並んでいない場合
            time = time + A
            print(time)
        else: #並んでいるとする場合
            time = time + A + diff
            print(time)
    else: #一番最初の処理
        time = time + T[i] + A
        print(time)