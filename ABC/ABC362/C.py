n = int(input)

intlist = []
for i in range(n):
    intlist.append(list(map(int, input().split())))
    
#動的計画法
for j in range(n):#リストの中身取り出し
    l = intlist[j][0]
    r = intlist[j][1]
    for k in range(l,r+1):#一つ目
        for o in range():