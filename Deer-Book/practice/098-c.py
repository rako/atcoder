n = int(input())

s = input()

silist = [0] * (n+1)

for i in range(n):
    if s[i] == "W":
        silist[i+1] = silist[i] - 1
    else:
        silist[i+1] = silist[i] + 1

print(silist)