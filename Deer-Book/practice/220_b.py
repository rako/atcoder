k = int(input())

a,b = map(int,input().split())

A,B = 0, 0

for i in range(len(str(a))):
    A += a%10 * k**i
    a //= 10

for i in range(len(str(b))):
    B += b%10 * k**i
    b //= 10

print(A*B)