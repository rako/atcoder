import math

a,b = map(int, input().split())

#print(min(a//0.08, b//0.1) if min(a//1.08, b//1.1) > 0 else -1)

price = []

#x1 = int((a/0.08) - 1) + 1
x1 = math.ceil(int(100*a / 8))
#x2 = int((a+1)/0.08)
x2 = math.floor(100*(a+1)// 8)

#y1 =  int((b)/0.1 - 1) + 1
y1 = math.ceil(int(100*b / 10))
#y2 =  int((b+2)/0.1)
y2 = math.floor(100*(b+1) // 10)

for i in range(x1 , x2):
    for j in range(y1, y2):
        if i >= 1 and i >= 1:
            if i == j:
                price.append(i)

print(min(price) if len(price) != 0 else -1)