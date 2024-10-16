n,m = map(int, input().split())

shoplist = []

for i in range(n):
    shoplist.append(list(map(int,input().split())))

total = 0
shoplist.sort()
rest = m
count = 0

while (rest > 0):
    #なぜcountのところを0としたらTLEになるのか
    total += shoplist[count][0] * min(shoplist[count][1], rest)
    rest -= shoplist[count][1]
    #shoplist.pop(0)
    count += 1

print(total)