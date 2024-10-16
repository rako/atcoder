h, a = map(int, input().split())

count = 0
while (True):
    h = h - a
    count += 1
    if h <= 0:
        break

print(count)