import itertools
n,s = map(int, input().split())
a = list(map(int, input().split()))
a2 = a*2
accma2 = list(itertools.accumulate(a2))
accma2set = set(accma2) #累積和のリストをセットに変換しておく。これをしておかないと、for文の中で値を探すために毎回リストを探すことになり、計算量が増える。

s %= sum(a) #sがsum(a)を超える場合の処理です

#尺取り法
#print(s)
ans = 0
for i in accma2:
    if i + s in accma2set: #累積和の中にi+sがあるかどうか。このsをsum_aにしていたのが間違いだと思う。
        ans = 1
        print("Yes")
        exit()
    else:
        continue
print("No")