import copy
n, k = map(int, input().split())
s = list(input())
ans = []
i = 0
while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i]:
        j += 1
    ans.append((s[i],j - i))
    i = j
count0 = 0
count1 = 0
list1 = []
ans1 = copy.deepcopy(ans)
print(ans)
for ax,ai in enumerate(ans):
    if ai[0] == "0":
        count0 += 1
    else:
        list1.append(ax)
        count1 += 1
        #print(count1, ai)
        if count1 == k:
            #print(tmp)
            ans1.remove(ai)
            ans1.insert(list1[-2] + 1,ai)
print(list1)
print(ans1)
result = ''.join(char * count for char, count in ans1)
print(result)