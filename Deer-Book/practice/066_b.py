s = input()

for i in range(1,len(s)//2 + 1):
    ss = s[:i * (-1) * 2]
    if all(ss[i] == ss[i + len(ss)//2] for i in range(len(ss)//2)):
        print(len(ss))
        break