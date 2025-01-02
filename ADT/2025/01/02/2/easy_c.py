import itertools
p,q = map(str, input().split())
if p > q:
    p,q = q,p
strlist = ["A","B","C","D","E","F","G"]
intlist = [0,3,1,4,1,5,9]
iterlist = list(itertools.accumulate(intlist))
#print(p,q) #ソートできてるか確認
#print(iterlist)
pin = strlist.index(p)
qin = strlist.index(q)
#print(pin,qin)
print(iterlist[qin] - iterlist[pin])