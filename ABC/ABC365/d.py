n = int(input())

s = list(input())

t = [""] * n

count = 0
if n == 1:
    print(1)
else:
    for i in range(1,n-1):
        if (s[i-1] != s[i]):
            if s[i] == "R":
                t[i] = "P"
            elif s[i] == "P":
                t[i] = "S"
            elif s[i] == "S":
                t[i] = "R"
            count += 1
        else:
            """
            if t[i-1] == "R":
                t[i] = "S"
            elif t[i-1] == "P":
                t[i] = "R"
            elif t[i] == "S":
                t[i] = "P"
            """
            if s[i] != s[i+1]:
                count += 1
            
count2 = 0

for i,j in enumerate(t):
    if i == 0:
        pass
    else:
        if j == t[i-1]:
            count2 += 1

print(count)