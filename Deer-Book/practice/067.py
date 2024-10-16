n,k = map(int, input().split())

n1 = 0
for i in range(int(str(n))):
    n1 += (n%10) * (8**i)
    n //= 10

#for i 