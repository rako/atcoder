n,m = map(int,input().split())

cities = []

for i in range(m):
    cities.append(list(map(int, input().split())))

cities.sort() #1番目の要素で、1番目が同じなら２番目で昇順

#for i in range(n):
    