n,p,q = map(int, input().split())

a = list(map(int, input().split()))

cnt = 0

#forの多重ループの際は範囲に注意
for i in range(n-4):
    for j in range(i+1,n-3):
        for k in range(j+1,n-2):
            for l in range(k+1,n-1):
                for m in range(l+1,n):
                    if (a[i] * a[j] * a[k] * a[l] * a[m]) % p == q:
                        cnt += 1
print(cnt)