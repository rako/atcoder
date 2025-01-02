n = int(input())
s = input()
t  = input()

def check(x,y):
    existlist = []
    for i in range(n):
        exist = False
        if x[i] == y[i]:
            exist = True
        if (x[i] == "1" and y[i] == "l") or (y[i] == "1" and x[i] == "l"):
            exist = True
        if (x[i] == "0" and y[i] == "o") or (y[i] == "0" and x[i] == "o"):
            exist = True
        #print(i, x[i], y[i], exist)
        existlist.append(exist)
    #print(existlist)
    return all(existlist)
#check(s,t)
print("Yes" if check(s,t) else "No")