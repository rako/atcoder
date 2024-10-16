s = input()

big = 0
small = 0

for i in s:
    if i.isupper():
        big += 1
    else:
        small += 1

if big > small:
    print(s.upper())
else:
    print(s.lower())