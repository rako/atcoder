s = input()
n = len(s)

ans = []

i = 0
while i < n:
    j = i + 1
    while j < n and s[j].islower():
        j += 1
        #print(i,j)
    ans.append(s[i:j+1])
    i = j + 1

ans.sort(key=str.lower)
print("".join(ans))