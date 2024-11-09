q = int(input())
daycount = 0
seedlist = []
countlist = []
for i in range(q):
    query = list(map(int, input().split()))
    order = query[0]
    count = 0
    if order == 1:
        #count += 1
        seedlist.append(0)
    elif order == 2:
        number = query[1]
        #daycount += number
        seedlist = [i + number for i in seedlist]
    elif order == 3:
        number = query[1]
        count = sum(1 for x in seedlist if x >= number)
        seedlist = [x for x in seedlist if x < number]
        countlist.append(count)
    #print(seedlist,countlist)
print(*countlist, sep='\n')