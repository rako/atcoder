k,g,m = map(int, input().split())

gg,mm = 0,0
for i in range(k):
    if gg == g:
        gg = 0
    elif mm == 0:
        mm = m
    else:
        diff = min(mm, g-gg)
        gg += diff
        mm -= diff

print(gg,mm)