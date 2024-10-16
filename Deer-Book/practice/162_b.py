n = int(input())

total = 0
a = []
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        #a[i-1] = "FizzBuzz"
        pass
    elif i % 3 == 0 and i % 5 != 0:
        #a[i-1] = "Fizz"
        pass
    elif i % 3 != 0 and i % 5 == 0:
        #a[i-1] = "Buzz"
        pass
    else:
        #a[i-1] = i
        total += i

print(total)