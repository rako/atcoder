n,m = map(int, input().split())

exist = True
#def kansu()?
if m == 0:
    exist = False

ss = [10] * n

for i in range(m):
    s,c = map(int, input().split())
    if c < ss[s-1]:
        ss[s-1] = c

fint = 0
for i in range(n):
    if ss[i] == 10:
        continue
    else:
        fint += ss[i] * (10**(n-i-1))

if len(str(fint)) < n:
    exist = False

if exist == False:
    print(-1)
else:
    print(fint)