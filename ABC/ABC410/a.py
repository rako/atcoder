n = int(input())
a = list(map(int, input().split()))
k = int(input())

count = 0
for ai in a:
    if k <= ai:
        count += 1

print(count)