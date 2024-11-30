n, d = map(int, input().split())
s = list(input())

for x in range(d):
    i = -1
    while (True):
        if s[i] == "@":
            s[i] = "."
            break
        else:
            i -= 1

print("".join(s))