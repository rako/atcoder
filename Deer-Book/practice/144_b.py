n = int(input())

exist = False

for i in range(1,10):
    for j in range(1,10):
        if i*j == n:
            exist = True

print("Yes" if exist else "No")