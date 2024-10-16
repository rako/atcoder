n,m = map(int, input().split())

homes = [[] for _ in range(n)]
homesbool = []

for i in range(m):
    s = list(input().split())
    a = int(s[0]) - 1
    b = str(s[1])
    if homes[a].count("M") != 0:
        chonan = False
    else:
        chonan = True
    if b == "F":
        chonan = False
    homesbool.append(chonan)
    homes[a].append(b)

for i in homesbool:
    if i:
        print("Yes")
    else:
        print("No")