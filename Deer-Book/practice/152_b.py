a, b = map(int, input().split())

ablist = []

ablist.append(str(a)*b)
ablist.append(a*str(b))

ablist.sort()

print(str(ablist[0]))