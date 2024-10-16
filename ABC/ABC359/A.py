N = int(input())

S = []
flag = 0

for i in range(N):
    Si = input()
    S.append(Si)
    if Si == "Takahashi":
        flag = flag + 1
    else:
        pass

print(flag)