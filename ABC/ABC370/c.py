s = input()
t = input()
n = len(s)

x = []

count = 0
while True:
    if s == t:
        break
    if any(ord(s[i]) > ord(t[i]) for i in range(n)):
        for i in range(n):
            if ord(s[i]) > ord(t[i]):
                s = s[:i] + t[i] + s[i+1:]
                count += 1
                x.append(s)
                break
    else:
        for i in range(n):
            if s[-i] != t[-i]:
                #print(-i)
                s = s[:(-i+n)//n] + t[(-i+n)//n] + s[(-i+1+n)//n:]
                count += 1
                x.append(s)

print(count)
for i in range(count):
    print(x[i])