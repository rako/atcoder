import itertools
a,b,c = map(int, input().split())
ans = []
for n in range(1,4):
    #print(list(itertools.combinations([a,b,c], n)))
    for i in itertools.combinations([a,b,c], n):
        ans.append(sum(i))
if len(set(ans)) == 7:
    print('No')
else:
    print('Yes')