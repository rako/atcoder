n,q = map(int, input().split())
s = list(input())

acl = [0] * (n+1)
for i in range(2,n+1):
    if s[i-2] == "A" and s[i-1] == "B" and s[i] == "C":
        acl[i+1] = 1
aclsum = sum(acl)
ans = []
for i in range(q):
    query = list(input().split())
    xi = int(query[0]) - 1
    ci = query[1]
    s[xi] = ci
    """
    if ci == "A" and s[xi + 1] == "B" and s[xi + 2] == "C":
        aclsum += 1
        acl[xi + 2] = 1
    elif ci == "B" and s[xi - 1] == "A" and s[xi + 1] == "C":
        aclsum += 1
        acl[xi + 1] = 1
    elif ci == "C" and s[xi - 1] == "B" and s[xi - 2] == "A":
        aclsum += 1
        acl[xi] = 1
    """
    ss = "".join(s)
    #print(ss)
    ans.append(ss.count("ABC"))
    s = list(ss)

#print(acl)
for i in ans:
    print(i)