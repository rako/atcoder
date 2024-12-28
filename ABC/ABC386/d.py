n,m = map(int, input().split())
query = [list(input().split()) for _ in range(m)]
exist = True
for i in query:
    x,y,c = int(i[0]),int(i[1]),i[2]
    if x+y < n+1:
        if c == "B":
            continue
        elif c == "W":
            exist = False
    elif x+y > n+2:
        if c == "W":
            continue
        elif c == "B":
            exist = False
    elif x+y == n+1: #ココがポイント
        pass
print("Yes" if exist else "No")