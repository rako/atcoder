x = int(input())

q,r = divmod(x,11)
if r <= 5:
    print(2*q + 1)
elif 6 <= r:
    print(2*q + 2)
elif r == 0:
    print(2*q)