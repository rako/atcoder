a,b,c,d = map(int, input().split())

count = 0
while(True):
    if count % 2 == 0:
        c -= b
    else:
        a -= d
    if a <= 0 or c <= 0:
        break
    count += 1

print("Yes" if a > c else "No")