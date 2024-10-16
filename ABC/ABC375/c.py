n = int(input())

gl = []

for i in range(n):
    tmpinputlist = list(input())
    gl.append(tmpinputlist)

for i in range(n//2):
    for j in range(i, n+1-i):
        for k in range(i, n+1-i):
            gl[j][n-i-1] = gl[i][j]

print(gl)