n = int(input())

a = list(map(int,input().split()))

a.sort(reverse=True)

total = 0
for i in range(len(a)):
    if i % 2 == 0:
        total += a[i]
    else:
        total -= a[i]

print(total)