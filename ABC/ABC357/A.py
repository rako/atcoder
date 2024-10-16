numbers = input().split()
hands = input().split()

N = int(numbers[0])
M = int(numbers[1])

total = 0
for n,i in enumerate(hands):
    if M <= 0:
        total = n + 1
        break
    else:
        M = M - int(i)
        
    

print(str(total))