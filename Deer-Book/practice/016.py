n = int(input())
a,b,c = map(int,input().split())
# 1 <= a,b,c,n <= 10**9

amin,bmin,cmin = 9999,9999,9999
for aa in range(min(10000, n//a + 1)):
    for bb in range(min(10000, n//b + 1)):
        if aa + bb <= 9999:
            for cc in range(min(10000 - aa - bb, n//c + 1)):
                if a*aa + b*bb + c*cc == n:
                    amin,bmin,cmin = min(amin,aa),min(bmin,bb),min(cmin,cc)

print(amin+bmin+cmin)