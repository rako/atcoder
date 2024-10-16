n = int(input())

minnum = 0

for i in range(0, 7):
    if 2**i <= n < 2**(i+1):
        minnum = 2**i
        break

print(minnum)