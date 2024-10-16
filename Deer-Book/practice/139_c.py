n = int(input())

h = list(map(int, input().split()))

count = 0
i = 0
while i < n:
    j = i + 1
    while j < n and h[j-1] >= h[j]:
        j += 1
    count = max(count, j-i-1)
    #print(i,j)
    i = j

print(count)