n,m = map(int, input().split())

h = list(map(int, input().split()))

count = 0
for i,j in enumerate(h):
    if m < j:
        break
    else:
        m -= j
    count += 1

print(count)