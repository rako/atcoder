n = int(input())
xylist = [list(map(int, input().split())) for _ in range(n)]
s = input()
for i in range(n):
    xylist[i].append(s[i])
#yが同じで、xが違うものを探す
#より小さい方のxがRで、より大きい方のxがLならば、衝突する
xylist.sort(key=lambda x: x[1])
#print(xylist)
i = 0
existlist = []
while(i < n):
    eqlist = [] #初期化
    j = i
    while(j < n):
        if xylist[i][1] != xylist[j][1]:
            break
        eqlist.append(xylist[j])
        j += 1
    print(eqlist)
    tmplist = []
    for k in range(len(eqlist)):
        #print(eqlist[k])
        print(tmplist)
        if len(tmplist) == 0:
            tmplist.append(eqlist[k][2])
        elif eqlist[k][2] == "R":
            tmplist.append(eqlist[k][2])
        elif eqlist[k][2] == "L":
            if tmplist[-1] == "R":
                tmplist.pop(-1)
                print("Yes")
                exit()
            else:
                tmplist.append(eqlist[k][2])
    existlist.append(True if len(tmplist) != len(eqlist) else False)
    i = j
#print(existlist)
print("Yes" if any(existlist) else "No")