n = int(input())
t, a = map(int,input().split())

h = list(map(int,input().split()))

tempraturelist = []

for i in range(n):
    temprature = 0
    temprature = abs((t - h[i]*0.006) - a)
    tempraturelist.append([temprature, i])

tempraturelist.sort()

print(tempraturelist[0][1] + 1)