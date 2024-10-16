h, w = map(int, input().split())

if h%2 == 0: #h偶
    if w%2 == 0: #w偶
        print(h//2 * w//2)
    else: #w奇
        print(h//2 * (w//2 + 1))
else: #h奇
    if w%2 == 0: #w偶
        print((h//2 + 1) * w//2)
    else: #w奇
        print((h//2 + 1) * (w//2 + 1))