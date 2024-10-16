N, K = map(int, input().split())

S = str(input())

for i in range(N):
    if S[i] == "?":
        for j in range(2):
            S[j] = "A"
            for k in range(2):
                S[i] = "B"
                for l in range(K):
                    if l+K <= N:
                        temp = S[l:l+K]

count = 0

for i,j in enumerate(temp):
    if j == temp[-i]:
        count += 1
    else:
        pass

print(count)