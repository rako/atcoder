n = int(input())

exist = False

for i in range(n//4 + 1):
    for j in range(n//7 + 1):
        if i*4 + j*7 == n:
            exist = True

print("Yes" if exist else "No")