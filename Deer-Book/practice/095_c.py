a,b,c,x,y = map(int, input().split())

total = 0
#2c <= a+bの時で、x,yから小さい方を無くなるように買い、
#残ったx,yのうち2x,2yよりもcが小さければx,yを直接買う
if 2*c <= a+b:
    total += 2*c*min(x,y)
    alpha,beta = min(x,y), max(x,y)
    beta -= alpha
    alpha -= alpha
    if x >= y:
        if 2*c <= a:
            total += 2*c*beta
        else:
            total += a*beta
    else:
        if 2*c <= b:
            total += 2*c*beta
        else:
            total += b*beta
#そうでないならa,b共に直接買った方が安い
else:
    total += (a*x + b*y)

print(total)