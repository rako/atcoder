n,k = map(int, input().split())

l = list(map(int,input().split()))

l.sort(reverse=True)

maxtotal = 0

for i in range(k):
    maxtotal += l[i]

print(maxtotal)