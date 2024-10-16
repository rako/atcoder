n = int(input())

mg = int(input())
g = [[] for _ in range(n)]
for i in range(mg):
    ui,vi = map(int, input().split())
    ui -= 1
    vi -= 1
    g[ui].append(vi)
    g[vi].append(ui)

h = [[] for _ in range(n)]
mh = int(input())
for i in range(mh):
    ai,bi = map(int, input().split())
    ai -= 1
    bi -= 1
    h[ai].append(bi)
    h[bi].append(ai)

alist = []
for i in range(n-1):
    alist.append(list(map(int, input().split())))

print(g,h)
count = 0
ans = 0
while(True):
    if (g == h) or (count > n*(n-1)/2):
        break
    elif (count < n):
        """
        tmpminuslist = list(set(h[count]) - set(g[count]))
        for ti in tmpminuslist:
            h[count].remove(ti)
            h[ti].remove(count)
            ans += alist[count][ti - 1]
        print(g,h)
        tmppluslist = list(set(g[count]) - set(h[count]))
        for ti in tmppluslist:
            h[count].append(ti)
            h[ti].append(count)
            ans += alist[count][ti - 1]
        """
        min_value = min(min(row) for row in alist)
        for i, row in enumerate(alist):
            if min_value in row:
                j = row.index(min_value)
        ans += alist[i][j]
        j += 1
        if j in h[i]:
            h[i].remove(j)
        else:
            h[i].append(j)
    count += 1

print(ans)