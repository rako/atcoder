money = 100
year = 0
x = int(input())

while (True):
    money = money + money//100
    year += 1
    if (x <= money):
        break

print(year)