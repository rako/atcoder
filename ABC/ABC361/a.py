x = str(input())
x = x.split(" ")
n = int(x[0])
l = int(x[1])
r = int(x[2])
y = []
for i in range(n):
    y.append(i+1)
if l == r:
    pass
elif(l ==1 and r == n):
    y.sort(reverse=True)
else:
    z = y[l-1:r]
    z_inv = sorted(z, reverse=True)
    y[l-1:r] = z_inv
a = ""
for j in y:
    a = str(a + str(j) + " ")
print(a)