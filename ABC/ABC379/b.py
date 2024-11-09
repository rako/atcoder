n,k = map(int , input().split())
s = input()

oxlist = []
i = 0
while i < n:
    j = i
    while j < n and s[j] == s[i]:
        j += 1
    oxlist.append((s[i], j-i))
    i = j
count = 0
for l in oxlist:
    if l[1] >= k and l[0] == 'O':
        count += l[1]//k
print(count)