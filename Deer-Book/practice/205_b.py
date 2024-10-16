n = int(input())

a = list(map(int, input().split()))

a.sort()

if all(i+1 == a[i] for i in range(len(a))):
    print("Yes")
else:
    print("No")