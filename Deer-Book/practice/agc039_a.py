s = input()
k = int(input())

"""
ss = s*k
n = len(ss)
count = 0
i = 0
while i < n:
    j = i + 1
    while j < n and (ss[i] == ss[j]):
        j += 1
    print(i,j,count)
    count += ((j-i) // 2) #2,3回連続で1回で、n//2回ごとに1回だけ変えればよい
    i = j
print(ss,count)
"""

if len(s) != 1:
    count = 0
    count1 = 0
    count2 = 0
    i = 0
    n = len(s)
    while i < n:
        j = i + 1
        while j < n and (s[i] == s[j]):
            j += 1
        count1 += (j-i)//2
        i = j
    count += count1*k
    if s[0] == s[-1]:
        if s[-1] == s[-2]:
            count2 = (k-1) * 
        else:
            count2 = k-1
    count += count2
else:
    count = k//2
print(count)