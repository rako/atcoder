n = int(input())

intlist = []

for _ in range(n):
    di = int(input())
    if di not in intlist:
        intlist.append(di)

print(len(intlist))