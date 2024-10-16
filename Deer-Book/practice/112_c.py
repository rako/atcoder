n = int(input())

zahyo = []

#h = max(h-abs(x-cx)-abs(y-cy),0) (x,y)の高度

for _ in range(n):
    zahyo.append(list(map(int, input().split())))

hzahyo = [[0]* 101] * 101

H = 0
for x in range(101):
    for y in range(101):
        cnt = 0
        for k in range(n):
            H = zahyo[k][2]+abs(zahyo[k][0]-x)+abs(zahyo[k][1]-y)
            if 0 <= H <= 10**9:
                if hzahyo[x][y] == H:
                    cnt += 1
                    if cnt == n:
                        print(x,y,hzahyo[x][y])
                        exit
                else:
                    hzahyo[x][y] = max(hzahyo[x][y],H)

#print(hzahyo)