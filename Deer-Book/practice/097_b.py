x = int(input())

maxnum = 1

for i in range(1,100):
    for j in range(2,11):
        if 1 <= i**j <= x:
            maxnum = max(maxnum, i**j)

print(maxnum)