n = int(input())
s = input()

setlist = []
i = 0
while i < n:
    j = i
    while j < n and s[j] == s[i]:
        j += 1
    setlist.append((s[i], j - i))
    i = j
count = 0
for i in range(len(setlist) - 2):
    tmp = 0
    if setlist[i][0] == "1":
        tmp = setlist[i][1]
        if setlist[i+1][0] == "/":
            if setlist[i+2][0] == "2":
                count1 = count
                count2 = min(setlist[i+2][1], tmp)
                count = max(count1, count2)
print(2*count + 1)
#print(setlist)