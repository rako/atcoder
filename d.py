n = int(input())
a = list(map(int, input().split()))

minus = []
# マイナスとなるのは、a[i] - (n-i)の分だけ
for i in range(n):
    tmp = a[i] - (n-(i+1)) + i #完成
    if tmp < 0:
        if n + 1 - min(minus) <= i:
            tmp -= len([x for x in minus if x <= n + 1 - min(minus)])
        minus.append(abs(tmp))
        a[i] = 0
    else:
        a[i] = tmp

for k in minus:
    for j in range(1, k+1):
        if a[-j] == 0:
            continue
        else:
            a[-j] -= 1
#print(minus)
print(*a)