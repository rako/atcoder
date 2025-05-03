s = input()
al = "abcdefghijklmnopqrstuvwxyz"
for c in al:
    if c not in s:
        print(c)
        exit()