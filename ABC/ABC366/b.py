n = int(input())

ss = [] 

m = 1
for i in range(n):
    ii = input()
    for j in range(len(ii)):
        if i == 0:
            ss.append(list(ii[j]))
        elif m < len(ii):
            if m <= j:
                ss.append(list(ii[j]))
            else:
                ss[j].insert(0,ii[j])
        else:
            if j <= len(ii) - 1:
                ss[j].insert(0,ii[j])
    k = m - len(ii)
    if k > 0:
        ss[len(ii) - 1 + k].append("*")
    m = max(m, len(ii))

for i in range(m):
    print(*ss[i], sep="")