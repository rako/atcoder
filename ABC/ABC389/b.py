x = int(input())
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
for i in range(1,21):
    if factorial(i) == x:
        print(i)
        break