n = int(input())
s = []
for i in range(n):
    sn = input().strip()
    s.append(sn)
s.sort(key=len)
print("".join(s))