n, q = map(int, input().split())
nl = [i+1 for i in range(n)]
offset = 0
ans = []

for i in range(q):
    #print("offset", offset)
    query = list(map(int, input().split()))
    query_type = query[0]
    if query_type == 1:
        p, x = query[1], query[2]
        pp = (p-1 + offset) % n
        nl[pp] = x
    elif query_type == 2:
        p = query[1]
        pp = (p-1 + offset) % n
        ans.append(nl[pp])
    elif query_type == 3:
        k = query[1]
        offset = (offset + k) % n
        #spl_bef = nl[:offset]
        #spl_aft = nl[offset:]
        #nl = spl_aft + spl_bef
    #print("nl", nl)
        
for ansi in ans:
    print(ansi)