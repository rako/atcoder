n,k = map(int, input().split())
a = list(map(int, input().split()))
ansl = []
for ai in a:
    if ai % k == 0:
        ansl.append(ai//k)
print(*ansl)