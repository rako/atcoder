s = str(input())
n = len(s)
t = list(s)

last = -1
for i in range(n + 1):
    if i == n or s[i] == '#':
        for j in range(last + 1, i):
            if t[j] == '.':
                t[j] = 'o'
                break
        last = i

print(''.join(t))
