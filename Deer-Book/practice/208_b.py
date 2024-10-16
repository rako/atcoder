def fac (n):
    if n != 1:
        return n * fac(n-1)
    else:
        return 1

p = int(input())

total = 0
for i in range(10): #i+1=N!
    for k in range(i):
        for j in range(100): #枚数
            p += fac(k+1) * j
            if p == 0:
                total += j
                break

print(total)
                