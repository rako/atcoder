import copy
ll = []
for i in range(8):
    ll.append(list(input()))
    #ll2.append(list(input()))
#print(ll)
ll2 = [[] for i in range(8)]
for i in range(8):
    for j in range(8):
        ll2[i].append("")
#print(ll2)
for i in range(8):
    for j in range(8):
        if ll[i][j] == "#":
            ll2[i] = ["#"]*8
            for k in range(8):
                ll2[k][j] = "#"
        #print(i,j)
count = 0
for i in range(8):
    for j in range(8):
        if ll2[i][j] == "":
            count += 1
#print(ll)
#print(ll2)
print(count)