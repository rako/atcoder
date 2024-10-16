a, b = map(int, input().split())

count = 0

for i in range(a,b+1):
    n = i
    if i % 10 == i // 10000:
        n = i // 10
        n = n % 1000
        if n % 10 == n // 100:
            count += 1

print(count)