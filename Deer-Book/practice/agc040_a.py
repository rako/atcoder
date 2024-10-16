s = input()

a = [0] * (len(s)+1)

"""
for i in range(len(s)):
    #print(i)
    if (s[i] != s[i+1]) and (s[i+1] == "<"):
        s[i] = 0
    elif (s[i] != s[i+1]) and (s[i] == ">"):
        a[i] += 1
"""

i = 0
slist = []
while(i<len(s)):
    j = i
    while j < len(s) and s[i]==s[j]:
        j += 1
    slist.append([s[i], j-i])
    i = j
slist[-1][1] += 1
#print(slist)

for i in range(len(slist) - 1):
    if (slist[i][0] == "<") and (slist[i+1][0] == ">"): #A->B
        if (slist[i][1]+1) < slist[i+1][1]:
            if True:
                pass
    else: #B->A
        pass

def facplus(n):
    if n == 0:
        return total
    else:
        total += facplus(n-1)

print(sum(a))