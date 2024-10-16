n = int(input()) #2 <= n
s = input()  #s = len(n)

strlistmax = 0 #N=2のときにabなどの時は0となるため
for i in range(1,n+1): #Pythonのスライス記法を復習
    x = s[:i]
    y = s[i:]
    strlist = []
    for j in range(len(x)):
        for k in range(len(y)):
            if (x[j] == y[k]) and(x[j] not in strlist):
                strlist.append(x[j])
    strlistmax = max(strlistmax, len(strlist))

print(strlistmax)