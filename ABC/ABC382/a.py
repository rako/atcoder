n,d = map(int, input().split())
s = list(input())

c1 = 0
c2 = 0
for i in s:
    if i == ".":
        c1 += 1
    elif i == "@":
        c2 += 1

print(c1 + d)