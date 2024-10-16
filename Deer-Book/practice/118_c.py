n,m = map(int, input().split())

num = [0] * 31

for i in range(n):
    query = list(map(int, input().split()))
    for j in range(query[0]):
        num[query[j+1]] += 1

cnt = 0
for i in num:
    if i == n:
        cnt += 1

print(cnt)