import math
s = input()
q = int(input())
k = list(map(int, input().split()))
n = len(s)
t = s.swapcase()
ans = []
"""
for ki in k:
    x = (ki + n - 1)//n
    for log2 in range(100):
        if x <= 2**log2:
            z = log2
            break
    check = z%2
    print(ki, x, check)
    if check == 0:
        ans.append(s[ki%n - 1])
    else:
        ans.append(t[ki%n - 1])
"""
"""
for ki in k:
    for log2 in range(100000):
        if x <= 2**log2:
            z = log2
            break
    ab = 2**z - ki
    for log2 in range(100000):
        if ab <= 2**log2:
            c = log2
            break
 """   
def decompose_to_powers_of_two(n):
    powers = []
    power = 0
    while n > 0:
        if n % 2 == 1:
            powers.append(2 ** power)
        n //= 2
        power += 1
    return powers
#print(decompose_to_powers_of_two(1))
for ki in k:
    kx = ki//n
    result = decompose_to_powers_of_two(kx)
    if (result[0])%2 == 0:
        ans.append(s[ki%n])
    else:
        ans.append(t[ki%n])
print(''.join(ans))