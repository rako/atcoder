s = list(input())
t = list(input())

diff = 1000 #len(t) <= len(s) <= 1000
for i in range(len(s) - len(t) + 1):
    count = 0
    for j in range(len(t)):
        if s[i+j] != t[j]:
            count += 1
    diff = min(count, diff)

print(diff)