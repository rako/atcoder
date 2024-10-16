import math

n = int(input())
xylist = []
for i in range(n):
    x,y = map(int,input().split())
    xylist.append((x,y))

sum = 0
for i in range(n-1):
    sum += math.sqrt((xylist[i][0] - xylist[i+1][0]) ** 2 + (xylist[i][1] - xylist[i+1][1]) ** 2)
sum += math.sqrt((xylist[-1][0]) ** 2 + (xylist[-1][1]) ** 2)
sum += math.sqrt((xylist[0][0]) ** 2 + (xylist[0][1]) ** 2)
print(sum)