import itertools
n,s = map(int, input().split())
a = list(map(int, input().split()))
a2 = a*2
accma2 = list(itertools.accumulate(a2))

s %= sum(a) #sがsum(a)を超える場合の処理です。これを忘れるとWAになります。

#尺取り法
#print(sum_a)
ans = 0
for i in accma2:
    if i + s in accma2: #累積和の中にi+sがあるかどうか。このsをsum_aにしていたのが間違いだと思う。
        ans = 1
        break
    else:
        continue
print("Yes" if ans == 1 else "No")