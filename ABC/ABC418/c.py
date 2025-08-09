n, q = map(int, input().split())
a = list(map(int, input().split()))
answer = []

for _ in range(q):
    b = int(input())
    if max(a) < b:
        answer.append(-1)
        continue
    max_ww = sum(min(ai, b-1) for ai in a)
    min_x = max_ww + 1  
    answer.append(max(min_x, b))
print(*answer, sep="\n")