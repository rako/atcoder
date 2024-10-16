n = int(input())

h = list(map(int, input().split()))

#t = 0
#while(max(h) != 0):
"""
t += 1
hin = [i for i,x in enumerate(h) if x >= 1]
hindex = hin[0]
if h[hindex] >= 1:
    if t%3 == 0:
        h[hindex] -= 3
    else:
        h[hindex] -= 1
#print(h)
"""
#t += 1
total = 1
h[0] -= 1
for hi in h:
    hia = hi//3
    hib = hi%3
    if hib == 0:
        hib += 2
    total += (hia*3 + hib)
    print(hia,hib)
"""
sumh = sum(h)
sumh -= (sumh // 3) * 3
t = sumh
"""
print(total)