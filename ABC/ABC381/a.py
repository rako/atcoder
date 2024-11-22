n = int(input())
s = input()

exist = True

for i in range(n):
    if i < n//2:
        if s[i] != "1":
            exist = False
    elif i > n//2:
        if s[i] != "2":
            exist = False
    elif i == n//2:
        if s[i] != "/":
            exist = False
if len(s) % 2 == 0:
    exist = False
print("Yes" if exist else "No")
