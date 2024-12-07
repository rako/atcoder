import copy
h, w, d = map(int, input().split())
hw = []
for i in range(h):
    hw.append(list(input()))
#print(hw)
ans = 0
countlist = []
dlist = [[[] for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        #hw2 = copy.deepcopy(hw)
        count = 0
        if hw[i][j] == "#":
            #机
            pass
        if hw[i][j] == ".":
            #床から2マス選んで、その時のマンハッタン距離がD以下でその時に限り加湿される床のマスの最大値
            for k in range(h):
                for l in range(w):
                    if abs(k - i) + abs(l - j) <= d and hw[k][l] == ".":
                        print("i",i,"j",j,"k",k,"l",l)
                        count += 1
                        dlist[i][j].append((k, l))
        for z in dlist[i][j]:
            i2, j2 = z[0], z[1]
            if len(dlist[i2][j2]) > len(dlist[i][j]):
                countlist.append((count, i, j))

countlist.sort(reverse=True)
print("countlist",countlist)


for x in range(2):
    tmp = countlist[x]
    i = tmp[1]
    j = tmp[2]
    if hw[i][j] != "H":
        hw[i][j] = "H"

for i in range(h):
    for j in range(w):
        if hw[i][j] == "H":
            ans += 1
print("dlist",dlist)
print(ans)