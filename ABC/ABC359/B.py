N = int(input())

A = list(map(int, input().split()))

count = 0

for i in range(N*2-2):
    if A[i] == A[i+2]:
        count += 1
    else:
        pass

print(count)