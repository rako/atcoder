n = int(input())

a = list(map(int,input().split()))

count = 0
flag = 0

while(True):
    for i in a:
        if i % 2 == 1:
            flag = 1

    if flag == 1:
        break
    
    for i in range(n):
        if a[i] % 2 == 0:    
            a[i] = a[i] // 2

    count += 1


print(count)