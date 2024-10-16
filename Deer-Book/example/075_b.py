h,w = map(int,input().split())

s = []

for i in range(h):
    s.append(list(input()))

for i in range(h):
    for j in range(w):
        if s[i][j] != "#":
            total = 0
            for k in range(-1,2):
                if i <= 2:
                    total += s[min(0,i+k)][max(0,j-1):min(j+2,w+1)].count("#")
                elif h -3 <= i:
                    total += s[max(h-1,i+k)][max(0,j-1):min(j+2,w+1)].count("#")
            s[i][j] = total
    print(s[i])