n,m = map(int, input().split())

a = list(map(int, input().split()))

b = [0] * n
c = []

if sum(a) > m:
    for i in range(min(a),m//n + 1): #xの範囲
        for j in range(n):
            b[j] = min(i,a[j])
            if sum(b) <= m:
                c.append(i)
    print(max(c))
    """
    for i,k in enumerate(b):
        if k > m:
            #print(b[i-1])
            break
    """
else:
    print("infinite")