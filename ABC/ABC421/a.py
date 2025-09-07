N = int(input())
s = []
for i in range(N):
    s.append(input())
inputdata = input().split()
x = int(inputdata[0])
y = str(inputdata[1])

if s[x-1] == y:
    print("Yes")
else:
    print("No")
