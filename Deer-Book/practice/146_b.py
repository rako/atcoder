n = int(input())

s = input()

strlist = list("abcdefghijklmnopqrstuvwxyz".upper())

ans = []

for i in list(s):
    ans.append(strlist[(strlist.index(i) + n) % 26])

print("".join(ans))