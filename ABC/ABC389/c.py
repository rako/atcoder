q = int(input())
ans = []
total = []
ansl = [] # i = 3用
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if len(total) == 0:
            total.append(0)
        else:
            total.append(total[-1] + ans[-1])
        ans.append(query[1])
    elif query[0] == 2:
        # ans
        tmp = ans.pop(0)

        # total
        # len(total) != 0 は保障されている
        total.pop(0)
        for t in range(len(total)):
            total[t] -= tmp
    elif query[0] == 3:
        k = query[1] - 1
        ansl.append(total[k])
    #print(ans, total)
for j in ansl:
    print(j)