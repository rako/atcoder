n,q = map(int ,input().split())

cl = [""] * n
cl[0] = "L"
cl[1] = "R"

ans = 0
for i in range(q):
    query = list(input().split())
    hi = str(query[0])
    ti = int(query[1]) - 1
    lindex = cl.index("L")
    rindex = cl.index("R")
    #print(hi,ti,lindex,rindex)
    if hi == "L":
        count = lindex
        tmptotalp = 0
        while True:
            count += 1
            #print(count)
            if cl[(count + 100) % 100] == "R":
                #tmptotalp = -100
                break
            elif count == ti:
                break
            else:
                tmptotalp += 1
        count = lindex
        tmptotalm = 0
        while True:
            count -= 1
            #print(count)
            if cl[(count + 100) % 100] == "R":
                #tmptotalm = -100
                break
            elif count == ti:
                break
            else:
                tmptotalm += 1
        print(tmptotalp,tmptotalm)
        ans += max(tmptotalp,tmptotalm)
        cl[lindex] = ""
        cl[ti] = "L"
    if hi == "R":
        count = rindex
        tmptotalp = 0
        while True:
            count += 1
            #print(count)
            if cl[(count + 100) % 100] == "L":
                #tmptotalp = -100
                break
            elif count == ti:
                break
            else:
                tmptotalp += 1
        count = rindex
        tmptotalm = 0
        while True:
            count -= 1
            #print(count)
            if cl[(count + 100) % 100] == "L":
                #tmptotalm = -100
                break
            elif count == ti:
                break
            else:
                tmptotalm += 1
        print(tmptotalp,tmptotalm)
        ans += max(tmptotalp,tmptotalm)
        cl[rindex] = ""
        cl[ti] = "R"
    print(cl)
print(ans)
#print(cl)