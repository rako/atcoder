n1 = input().split()
n, c1, c2 = int(n1[0]), n1[1], n1[2]
s = input()
#print(n, c1, c2)
#print(s)

ans = ""
for i in s:
    if i != c1:
        ans += c2
    else:
        ans += i
print(ans)