n = int(input())
a = list(map(int, input().split()))
adict = {}
ans = []
for j,i in enumerate(a):
    if i in adict:
        ans.append(adict[i])
        adict[i] = j+1
    else:
        ans.append(-1)
        adict[i] = j+1
    #print(adict)
    #print(ans)
print(*ans)