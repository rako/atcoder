n, x = map(int, input().split())

l = list(map(int, input().split()))

y = 0
count = 1

for i in l:
    y += i
    if y > x:
        break
    else:
        count += 1


print(count)