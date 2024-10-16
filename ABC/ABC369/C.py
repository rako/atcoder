import itertools,math

n = int(input())
a = list(map(int, input().split()))

acsum = [0] * (n+1)
for i in range(n):
    acsum[i+1] = acsum[i] + a[i]

ans = 0

for l,r in itertools.combinations_with_replacement(range(n),2):
    l += 1
    r += 1
    #print(l,r)
    if r-l == 0 or r-l == 1:
        ans += 1
    else:
        su = False
        for i in range(1,r-l):
            if abs(acsum[l+i]-acsum[l]*(i+1)) % ((i)*(i+1)/2) == 0:
                su = True
            #print(l,r)
        if su:
            ans += 1
print(ans)