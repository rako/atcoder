def f(x):
    s_x = str(x)
    rev_s_x = s_x[::-1]
    return int(rev_s_x)

X, Y = map(int, input().split())

a = [0] * 11
a[1] = X
a[2] = Y

for i in range(3, 11):
    a[i] = f(a[i-1] + a[i-2])

print(a[10])
