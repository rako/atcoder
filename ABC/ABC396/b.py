q = int(input())
pile = [0] * 100
#print(pile)
ul = []
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        pile.append(x)
    elif query[0] == 2:
        y = pile.pop(-1)
        ul.append(y)
for j in ul:
    print(j)