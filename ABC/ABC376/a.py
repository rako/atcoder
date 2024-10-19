n,c = map(int, input().split())
t = list(map(int, input().split()))

#print(n,c)
count = 1
tmp = t[0]
for i in range(len(t) - 1):
    if t[i+1] - tmp >= c:
        count += 1
        tmp = t[i+1]

print(count)