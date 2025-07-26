from itertools import product
n,k,x = map(int, input().split())
s = []
for i in range(n):
    s.append(input())
#s.sort(key=lambda x:x[1])
#print(s)
ll = []
for index in product(range(n), repeat=k):
    tmp = "".join(s[i] for i in index)
    ll.append(tmp)
ll.sort()
print(ll[x-1])