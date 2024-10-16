n = int(input())

s = []

for i in range(n):
    si = input()
    si.sort()
    s.append(si)

cnt = 0
for i in range(n-1):
    for j in range(i+1,n):
        if s[i] == s[j]:
            cnt += 1

print(cnt)