q = int(input())

query = [list(map(int, input().split())) for _ in range(q)]

bags = {}

for i in range(0,q):
    if query[i][0] == 1:
        if query[i][1] not in bags:
            bags[query[i][1]] = 1
        else:
            bags[query[i][1]] += 1
    elif query[i][0] == 2:
        if query[i][1] in bags and bags[query[i][1]] == 1:
            del bags[query[i][1]]
        elif query[i][1] in bags and bags[query[i][1]] >= 2:
            bags[query[i][1]] -= 1
    elif query[i][0] == 3:
        print(len(bags))