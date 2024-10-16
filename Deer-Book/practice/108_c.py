n,k = map(int, input().split())

for i in range(1,n//k + 1):
    for a in range(1,i+1):
        for b in range(1,i+1):
            for c in range(1,i+1):
                if (a+b)%