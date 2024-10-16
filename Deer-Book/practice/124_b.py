n = int(input())

h = list(map(int, input().split()))

count = 0

for i in range(len(h)):
    if i == 0:
        count += 1
    else:    
        if all(h[j] <= h[i] for j in range(i)):
            count += 1

print(count)