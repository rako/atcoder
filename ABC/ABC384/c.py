import itertools
a,b,c,d,e = map(int, input().split())
arrivedlist = [(a, 'A'), (b, 'B'), (c, 'C'), (d, 'D'), (e, 'E')]
ans = []

for n in range(5,0,-1):
    tmp = list(itertools.combinations(arrivedlist, n))
    #print(tmp)
    for i in tmp:
        #print(i)
        tmpsum = 0
        tmpstr = ""
        for j,k in i:
            tmpsum += j
            tmpstr += k
        ans.append((tmpsum, tmpstr))

#print(ans)
ans.sort(reverse=True, key=lambda x: x[0])
for i in ans:
    print(i[1])