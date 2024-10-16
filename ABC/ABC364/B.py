h, w = map(int, input().split())

si, sj = map(int, input().split()) 

c2dlist = []
for i in range(h):
    c2dlist.append(list(input()))

move = list(input())

#リストが0から始まるから
si = si - 1
sj = sj - 1
#print(str(si) + "," + str(sj))

for k in move:
    if k == "L":
        if (sj - 1 < 0):
            pass
        else:    
            if (c2dlist[si][sj - 1] == "."):
                sj -= 1
                #print(str(si) + "," + str(sj))
    elif k == "R":
        if (w - 1 < sj + 1):
            pass
        else:    
            if (c2dlist[si][sj + 1] == "."):
                sj += 1
                #print(str(si) + "," + str(sj))
    elif k == "U":
        if (si - 1 < 0):
            pass
        else:    
            if (c2dlist[si - 1][sj] == "."):
                si -= 1
                #print(str(si) + "," + str(sj))
    elif k == "D":
        if (h - 1 < si + 1):
            pass
        else:    
            if (c2dlist[si + 1][sj] == "."):
                si += 1
                #print(str(si) + "," + str(sj))

#print(c2dlist)
#print(move)
print(str(si + 1) + " " + str(sj + 1))