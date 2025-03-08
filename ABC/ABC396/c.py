n,m = map(int, input().split())
b = list(map(int, input().split()))
w = list(map(int, input().split()))
b.sort(reverse=True)
w.sort(reverse=True)
# print(b)
# print(w)
maxnum = max(n,m)
ans = 0
for i in range(maxnum):
    #print("i",i)
    if i >= n and n < m: #mの方が長い時
        break
    if i >= m and m < n: #nの方が長い時
        if b[i] >= 0:
            ans += b[i]
        continue
    
    if b[i] >= 0: #bが正の時
        if w[i] >= 0: #wが正の時
            ans += b[i] + w[i]
        else: #bが正でwが負の時
            ans += b[i]
    elif b[i] < 0: #bが負の時
        if w[i] < 0: #wが負の時
            continue
        if w[i] >= 0: #wが正の時でb+wが正の時
            if b[i] + w[i] >= 0:
                ans += b[i] + w[i]
            else:
                continue
        
print(ans)