n, y = map(int, input().split())

exist = False

for a in range(2001):
    for b in range(4001):
        c = n - a - b

        if c < 0 or c > n:
            continue

        if 10000 * a + 5000 * b + 1000 * c != y:
            continue
        else:
            A,B,C = a,b,c
            exist = True
            break

if exist == False:
    print(-1,-1,-1, sep=" ")
else:
    print(A,B,C, sep=" ")