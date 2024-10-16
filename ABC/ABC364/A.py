N = int(input())

S = []
for n in range(N):
    S.append(input())

flag = 0
for i, j in enumerate(S):
    if (1 <= i) and (i < N - 1):
        if S[i-1] == S[i]:
            if j == "sweet":
                flag = 1
                break
            elif j == "salty":
                flag = 0
        else:
            flag = 0

if flag == 0:
    print("Yes")
elif flag == 1:
    print("No")
