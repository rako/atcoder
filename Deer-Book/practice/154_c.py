n = int(input())

a = set(list(map(int, input().split())))

if len(a) == n:
    print("YES")
else:
    print("NO")